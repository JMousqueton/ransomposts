import requests
from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime as dt
from datetime import timezone
import json

env = Environment(
    loader=FileSystemLoader( searchpath="./templates" ),
    autoescape=select_autoescape()
)

url = "https://raw.githubusercontent.com/jmousqueton/ransomwatch/main/posts.json"
r = requests.get(url)
template = env.get_template("template.html")
ransoms = r.json()
ransoms.reverse()
with open('./docs/index.html','w') as f:
            f.write(template.render(ransoms=ransoms,fecha=dt.now(tz=timezone.utc).strftime('%d-%b-%Y %H:%M %Z')))