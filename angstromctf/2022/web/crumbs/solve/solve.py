import requests
import os

# Use environment variable for base URL, default to localhost for local testing
base_url = os.environ.get("CRUMBS_URL", "http://localhost:8080")
s = ""

while True:
    print(s)
    p = requests.get(f"{base_url}/" + s)
    if "actf" in p.text:
        print(p.text)
        break
    s = p.text.strip().split()[-1]
