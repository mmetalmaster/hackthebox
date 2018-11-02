import requests
import base64
import json

HackboxURL = "https://www.hackthebox.eu/api/invite/generate"
JSONDATA = requests.post( HackboxURL )
print base64.b64decode(json.loads(JSONDATA.text)["data"]["code"])