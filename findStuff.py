from writePDF import writePDF
import requests
import json 
import sys
from generate_story import generate
  
def findStuff(message): 

  results = requests.get("http://api.meaningcloud.com/topics-2.0", 
              params={'key': '4e9d9d2ab61341074dd513e4422aa47e', 'of': 'json', 'lang': 'en', 'ilang': 'en', 'txt': message, 'tt': 'a'})
  prompts = []
  for concept in results.json()['concept_list']: 
    if concept['relevance'] == '100': 
      prompts.append(concept['form'])

  for entity in results.json()['entity_list']: 
    if entity['relevance'] == '100': 
      prompts.append(entity['form'])
  if len(prompts) < 7: 
    bigPrompt = ""
    for prompt in prompts: 
      bigPrompt += prompt + " "
    prompts.append(bigPrompt) 

  stories = []
  if len(prompts) > 4: 
    for prompt in prompts: 
      stories.append(generate(prompt))
      print(stories)
  else: 
    while len(prompts) < 4: 
      prompts = prompts * 2

    for prompt in prompts: 
      print(stories)
      stories.append(generate(prompt))
  print(stories)
  fileName = writePDF(stories)
  print(fileName)
  return(fileName)
