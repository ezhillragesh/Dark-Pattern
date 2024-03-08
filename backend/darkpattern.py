import pathlib
import textwrap
import google.generativeai as genai
from linkfinder import main

def gemini(link : str):
    links  = main(link)
    api = 'AIzaSyCksOSutvb-69Ug3zChagVxkaVPKtVFMUc'
    genai.configure(api_key=api)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(link+ "summarise in points the data that is being collected of the user in this websites privacy policy, summarise the terms and conditions,and summarise the cookie policy")
    print(response.text)
    return {"Webscrape" : links, "Summary" : response.text}