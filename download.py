from datetime import datetime

import browser_cookie3
import requests
from bs4 import BeautifulSoup


def download():
    cj = browser_cookie3.chrome(domain_name="yellowpicnic.com")

    resp = requests.get(
        "https://yellowpicnic.com/account/orders/",
        cookies=cj,
        timeout=30,
    )
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "lxml")

    link = soup.select_one('a[href*="edit_subscription_order"]')
    if not link:
        raise ValueError("Could not find 'customize this weeks meals' link on orders page")
    customize_url = link["href"]
    if customize_url.startswith("/"):
        customize_url = "https://yellowpicnic.com" + customize_url

    date_text = None
    for el in soup.find_all(string=True):
        if "Next Delivery:" in el:
            date_text = el.strip()
            break
    if not date_text:
        raise ValueError("Could not find 'Next Delivery' date on orders page")
    date_part = date_text.split("Next Delivery:")[-1].strip()
    date = datetime.strptime(date_part, "%A, %d %b %Y")
    date_str = date.strftime("%Y-%m-%d")

    resp = requests.get(customize_url, cookies=cj, timeout=30)
    resp.raise_for_status()

    return resp.text, date_str
