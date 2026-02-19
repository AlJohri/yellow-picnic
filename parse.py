import re

from bs4 import BeautifulSoup


def parse_ingredients(card):
    el = card.select_one(".hidden-div")
    if not el:
        return None
    close_btn = el.select_one(".close-ingre")
    if close_btn:
        close_btn.decompose()
    return el.get_text(strip=True)


def parse_macros(card):
    macros = {}
    for block in card.select(".progress-block[data-goal]"):
        values = {}
        for span in block.select("span.actual_v"):
            text = span.get_text(strip=True)
            m = re.match(r"(\d+)\s*(kcal|cal|g)?$", text, re.IGNORECASE)
            if not m:
                if text:
                    print(f"Warning: unparseable macro value: {text!r}")
                continue
            label_el = span.find_previous_sibling("div", class_="label_")
            if label_el:
                values[label_el.get_text(strip=True).lower()] = int(m.group(1))
        macros[block["data-goal"]] = values
    return macros


def parse(html, date_str):
    soup = BeautifulSoup(html, "lxml")

    meals = []
    for card in soup.select("div.cui-card"):
        img = card.select_one("img.cui-image[alt]")
        if not img or not img["alt"].strip():
            continue

        desc_el = card.select_one("p.ycwc-description")

        meals.append({
            "name": img["alt"].strip(),
            "description": desc_el.get_text(strip=True) if desc_el else None,
            "ingredients": parse_ingredients(card),
            "macros": parse_macros(card),
        })

    cards = soup.select("div.cui-card")
    if cards and not meals:
        raise ValueError(
            f"Found {len(cards)} cards but parsed 0 meals; page structure may have changed"
        )

    return meals
