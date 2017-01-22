import subprocess
import requests
import json
import re
import os
import sys

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)

def partition(context, model):
    args = "python3 story_partition.py \"" + context + "\" \"" + model + "\""
    print(args)
    return subprocess.getoutput(args)

def getValue(theContext, theSentences):
    url = "http://api.cortical.io/rest/compare"
    querystring = {"retina_name":"en_associative"}
    #payload = "[\n     { \n        \"term\": \"Pablo Picasso\" \n     },\n     {\n        \"text\": \"Gustav Klimt was born in Baumgarten, near Vienna in Austria-Hungary, the second of seven children\"\n     }\n]"
    payload = "[ {\"term\": \"" + theContext+ "\"},{\"text\": \"" + theSentences + "\"}]"
    headers = {
        'accept': "application/json",
        'origin': "http://api.cortical.io",
        'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36",
        'content-type': "application/json; charset=utf-8",
        'referer': "http://api.cortical.io/Compare.htm",
        'accept-encoding': "gzip, deflate",
        'accept-language': "en-GB,en-US;q=0.8,en;q=0.6",
        'cookie': "_ga=GA1.2.674882336.1485061533; _gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
        'cache-control': "no-cache",
        'postman-token': "58477186-0dbc-1781-560a-25352abe1f7f"
        }
    results = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    print(results)
    return results.json()["cosineSimilarity"]

def optimal(theContext, paragraph):
    return ".".join(paragraph.split(".")[2:])
    #theContext, paragraph = theContext.encode("utf-8","strict").decode("utf-8", "strict"), paragraph.encode("utf-8","strict").decode("utf-8", "strict")
    theContext = str(theContext).decode("utf-8")
    paragraph = str(paragraph).decode("utf-8")
    allTheSentences = re.split('(?<=[.!?]) +',paragraph)
    max = -0.5
    maxPhrase = ""
    for x in allTheSentences:
      currValue = getValue(theContext,re.sub(r'[^\w]', ' ', x))
      if currValue is not None:
        if currValue > max:
          maxPhrase = x
          max = currValue
    return maxPhrase


def generate(context):
    print (dname)
    print("generating....")
    story = ""

    print("generating beg")
    story += optimal(context, partition(context, dname + "/model/beg/"))

    print("generating mid")
    story += optimal(context, partition(context, dname + "/model/mid/"))

    print("generating end")
    story += optimal(context, partition(context, dname + "/model/end/"))
    return story
