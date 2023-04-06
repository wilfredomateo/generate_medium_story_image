#This program will pull content (article paragraphs) from Medium and create an AI Image from its keywords
#Developer: Wilfredo Mateo
#---

import os
import re
import openai
import argparse
import urllib.request

#Command line argument parser 
parser = argparse.ArgumentParser(description='Fetch a Medium story\'s textual contents.')
parser.add_argument('url', metavar='URL', help='A URL that points to a Medium story.')
arguments = parser.parse_args()
#---

#Fetch HTML (<article>) content from a URL
def fetch_article_content(url):
    
    #Add headers to fake a browser in order to overcome a 403 error
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
    #--

    #Pull webpage
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    the_page_bytes = response.read()
    
    #Convert data to utf-8
    html = the_page_bytes.decode("utf-8")

    #Extract article text from HTML code
    pattern = "<article.*?>.*?</article.*?>"
    match_results = re.search(pattern, html, re.IGNORECASE)
    paragraph = match_results.group()
    paragraph = re.sub("<.*?>", "", paragraph) #Remove HTML tags
    #---

    return paragraph
#---

#Have ChatGPT generate keywords from article
def generate_keywords(article):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=article,
        temperature=0.7,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=1
    )
    return response['choices'][0]['text'] #Return the text from dictionary
#---

#Provide keywords to AI image creator
def create_image(keywords):
    image = ''
    return image

#Grab OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

article = fetch_article_content(arguments.url)
article_keywords = generate_keywords(article)
#aricle_image = create_image(article_keywords)

print(article_keywords)
