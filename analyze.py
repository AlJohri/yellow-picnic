import pandas as pd

GOAL = "loss"

# Target ratios: 130P / 47C / 44F
TARGET_P_TO_C = 130 / 47  # 2.77
TARGET_P_TO_F = 130 / 44  # 2.95

MACRO_COLS = ["calories", "protein", "carbs", "fat"]


def analyze(meals):
    rows = [
        {"name": meal["name"], **{col: macros.get(col) for col in MACRO_COLS}}
        for meal in meals
        if (macros := meal["macros"].get(GOAL))
    ]

    df = pd.DataFrame(rows)
    df[["carbs", "fat"]] = df[["carbs", "fat"]].replace(0, float("nan"))
    df["protein_to_carbs"] = (df["protein"] / df["carbs"]).round(2)
    df["protein_to_fat"] = (df["protein"] / df["fat"]).round(2)
    df["score"] = (df["protein_to_carbs"] / TARGET_P_TO_C + df["protein_to_fat"] / TARGET_P_TO_F).round(2)

    return df.sort_values("score", ascending=False)
