from .writePDF import writePDF
import requests
import json 

def findStuff(message): 
  url = "http://api.meaningcloud.com/topics-2.0?key=4e9d9d2ab61341074dd513e4422aa47e&of=json&lang=en&ilang=en&txt=" + message

  results = requests.get("http://api.meaningcloud.com/topics-2.0", 
              params={'key': '4e9d9d2ab61341074dd513e4422aa47e', 'of': 'json', 'lang': 'en', 'ilang': 'en', 'txt': message, 'tt': 'a'})
  topKeys = []
  for concept in results.json()['concept_list']: 
    if concept['relevance'] == '100': 
      topKeys.append(concept['form'])

  for entity in results.json()['entity_list']: 
    if entity['relevance'] == '100': 
      topKeys.append(entity['form'])
  sentenceIndex = message.find(topKeys[0])
  phrase = ""
  for i in range(sentenceIndex, len(message)): 
  	if message[i] == "." or message[i] == "!" or message[i] == "?":
  		break
  	else: 
  		phrase += message[i]
  for i in range(sentenceIndex - 1, -1, -1):
    if message[i] == "." or message[i] == "!" or message[i] == "?":
    	break
    else: 
    	phrase = message[i] + phrase

  fileName = writePDF()
  return(fileName)