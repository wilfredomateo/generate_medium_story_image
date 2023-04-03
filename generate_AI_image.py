#This program will pull an article from Medium and create a AI Image from its content (keywords)
#Developer: Wilfredo Mateo
#---

import os
import openai
import argparse
import urllib.request

#Command line argument parser 
parser = argparse.ArgumentParser(description='Fetch a Medium story\'s textual contents.')
parser.add_argument('url', metavar='URL', help='A URL that points to a Medium story.')
arguments = parser.parse_args()
#---

#Function to fetch the Medium article's content from a URL
def fetch_article_content(url):
    
    #Add headers to fake a browser in order to overcome a 403 error
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
    #--

    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)

    the_page = response.read()
    return the_page
#---

print(fetch_article_content(arguments.url))

#Grab OpenAI API key
#openai.api_key = os.getenv("OPENAI_API_KEY")

#Gets 
#prompt= 
#Generate keywords
#response = openai.Completion.create(
#  model="text-davinci-003",
#  prompt="",
#  temperature=0.5,
#  max_tokens=60,
#  top_p=1.0,
#  frequency_penalty=0.8,
#  presence_penalty=0.0
#)

#print(response)
