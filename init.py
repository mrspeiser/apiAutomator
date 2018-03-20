import math
import requests
import datetime
import sys
import json

from api import Api
from processes import *


data=requests.get("http://quotes.rest/qod.json")
json=data.json();

quote=json['contents']['quotes'][0]['quote']
author=json['contents']['quotes'][0]['author']

postFormat= """{0}
- {1}"""
post=postFormat.format(quote, author);

res=requests.post("https://graph.facebook.com/me/feed", data={
	'message':post, 
	'access_token':''
	})


print(res.text)
