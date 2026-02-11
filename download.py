import browser_cookie3
import requests

SUBSCRIPTION_ID = "MjEzMDA3"


def download():
    cj = browser_cookie3.chrome(domain_name="yellowpicnic.com")

    resp = requests.get(
        f"https://yellowpicnic.com/edit_subscription_order/?id={SUBSCRIPTION_ID}",
        cookies=cj,
        timeout=30,
    )
    resp.raise_for_status()
    return resp.text
