import os
import openai
import argparse

#Command line argument parser 
parser = argparse.ArgumentParser(description='Fetch a Medium story\'s textual contents.')

parser.add_argument('url', 
                    metavar='URL',
                    help='A URL that points to a Medium story.')

arguments = parser.parse_args()
print(arguments.url)

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
