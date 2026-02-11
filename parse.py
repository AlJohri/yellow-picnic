import re
from datetime import datetime

from bs4 import BeautifulSoup


def parse_date(soup):
    weekday_el = soup.select_one("span.weekday")
    if not weekday_el:
        raise ValueError("Could not find menu date")
    date_match = re.search(r":\s*(.+)$", weekday_el.get_text())
    if not date_match:
        raise ValueError("Could not parse menu date")
    date = datetime.strptime(date_match.group(1).strip(), "%A, %B %d")
    now = datetime.now()
    date = date.replace(year=now.year)
    diff = abs((date - now).days)
    if diff > 180:
        date = date.replace(year=now.year + (1 if date < now else -1))
    return date.strftime("%Y-%m-%d")


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
            m = re.match(r"(\d+)(kcal|g)", text, re.IGNORECASE)
            if not m:
                if text:
                    print(f"Warning: unparseable macro value: {text!r}")
                continue
            label_el = span.find_previous_sibling("div", class_="label_")
            if label_el:
                values[label_el.get_text(strip=True).lower()] = int(m.group(1))
        macros[block["data-goal"]] = values
    return macros


def parse(html):
    soup = BeautifulSoup(html, "lxml")
    date_str = parse_date(soup)

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

    return date_str, meals
