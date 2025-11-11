import requests

url = "https://ebid.korail.com/"
headers = {"User-Agent": "Mozilla/5.0"}
try:
    resp = requests.get(url, headers=headers, timeout=10)
    resp.raise_for_status()
    html = resp.text
    filename = "ebid.html"
    encoding = resp.encoding or "utf-8"
    with open(filename, "w", encoding=encoding) as f:
        f.write(html)
    print("Saved HTML to", filename)
except requests.RequestException as e:
    print("Request error:", e)
requests
