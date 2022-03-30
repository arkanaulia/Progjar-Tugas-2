import requests
from requests.structures import CaseInsensitiveDict

url = "https://www.its.ac.id/"

headers = {"Content-Type": "application/json; charset=utf-8", "Accept": "application/json", "Accept-Encoding": "gzip"}


resp = requests.get(url, headers=headers)
aaa=resp.headers
aaa = str(aaa)
aaa=aaa.split(',')[11].split()[1]
aaa=aaa.strip("'")

print(aaa)
