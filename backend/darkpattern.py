import pathlib
import textwrap
import google.generativeai as genai
from linkfinder import main

def gemini(link : str):
    # links  = main(link)
    # links = link
    api = 'AIzaSyAaNcX4qjRlX-_4LwsqvwzN-krMT54xVSs'
    genai.configure(api_key=api)
    model = genai.GenerativeModel('gemini-pro')
    # response = model.generate_content(link+ "summarise in points the data that is being collected of the user in this websites privacy policy, summarise the terms and conditions,and summarise the cookie policy")
    # print(response.text)
    # summary = response.text
    # summary = "BLAH"
    with open("text1.txt", 'r') as f:
        ip = f.read()
        print(ip)
        response = model.generate_content('''
                                          
        Identify phrases that contain Confirmshaming, Hidden Costs, Bait and Switch, Social Proof, Urgency in this content \n Examples being Confirmshaming:

    "Are you sure you don't want to save 15% off? Click cancel if you hate saving money."
    "Don't miss out on these exclusive benefits! Just select 'no' if you'd rather pay more."

    Hidden Costs:

    "Limited time offer: Only $19.99!" (Doesn't mention shipping or taxes)
    "Free trial! But you must enter your credit card information to continue."

    Bait and Switch:

    Advertise a popular product at a low price, but it's out of stock. You're pressured to buy a more expensive option.
    "Free with purchase!" (But the "purchase" requires spending a specific amount)

    Social Proof:

    "Join over 1 million satisfied customers!"
    "Limited quantities available! Don't miss out on what everyone else is loving." (Displays icons of people adding to cart)

    Urgency:

    "Only 2 left in stock! Order now before they're gone!" (Creates a sense of scarcity)
    "This offer expires in 3 hours! Don't wait - secure your spot now!" (Countdown timer)
    
    ''' + ip)
        print(response.text)
        text_mani = response.text
    f.close()
    return {"Text Manipulation" : text_mani}

def gemini_summary(link : str):
    # links  = main(link)
    links = link
    api = 'AIzaSyAaNcX4qjRlX-_4LwsqvwzN-krMT54xVSs'
    genai.configure(api_key=api)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(link+ "summarise in points the data that is being collected of the user in this websites privacy policy, summarise the terms and conditions,and summarise the cookie policy")
    # print(response.text)
    summary = response.text
    # summary = "BLAH"
    # with open("text1.txt", 'r') as f:
    #     ip = f.read()
    #     print(ip)
    #     response = model.generate_content("Identify phrases that contain Confirmshaming, Hidden Costs, Bait and Switch, Social Proof, Urgency in this content \n" + ip)
    #     print(response.text)
    #     text_mani = response.text
    # f.close()
    return {"Summary" : summary}


