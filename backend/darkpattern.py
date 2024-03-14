import pathlib
import textwrap
import google.generativeai as genai
from linkfinder import main

def gemini(link : str):
    # links  = main(link)
    links = "BLAH"
    api = 'AIzaSyCksOSutvb-69Ug3zChagVxkaVPKtVFMUc'
    genai.configure(api_key=api)
    model = genai.GenerativeModel('gemini-pro')
    # response = model.generate_content(link+ "summarise in points the data that is being collected of the user in this websites privacy policy, summarise the terms and conditions,and summarise the cookie policy")
    # print(response.text)
    # summary = response.text
    summary = "BLAH"
    with open("text1.txt", 'r') as f:
        ip = f.read()
        print(ip)
        response = model.generate_content("Identify phrases that contain Confirmshaming, Hidden Costs, Bait and Switch, Social Proof, Urgency in this content \n" + ip)
        print(response.text)
        text_mani = response.text
    f.close()
    return {"Text Manipulation" : text_mani, "Webscrape" : links, "Summary" : summary}