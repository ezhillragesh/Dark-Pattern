from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse

terms_and_conditions_phrases = [
    "Terms of Service",
    "Terms & Conditions",
    "User Agreement",
    "Terms and Conditions of Use",
    "Terms of Use",
    "Service Agreement",
    "User Terms",
    "Conditions of Use",
    "Usage Terms",
    "Legal Terms",
    "Agreement",
    "Rules and Regulations",
    "Policy and Agreement",
    "Terms",
    "Terms of Acceptance",
    "User Guidelines",
    "Terms of Engagement",
    "Conditions of Service"
]

privacy_policy_phrases = [
    "Privacy Policy",
    "Privacy Statement",
    "Privacy Notice",
    "Data Protection Policy",
    "Confidentiality Policy",
    "Data Privacy Policy",
    "Information Protection Policy",
    "Privacy Protocol",
    "Privacy Commitment",
    "Confidentiality Agreement",
    "Privacy Terms",
    "Data Handling Policy",
    "Data Security Policy",
    "Data Usage Policy",
    "Privacy Rules",
    "Information Privacy Statement",
    "Privacy Agreement",
    "Data Protection Agreement"
]

cookie_policy_phrases = [
    "Cookie Policy",
    "Cookie Statement",
    "Cookie Usage Policy",
    "Cookie Use Policy",
    "Cookie Guidelines",
    "Cookie Disclosure",
    "Cookie Management Policy",
    "Cookie Handling Policy",
    "Cookie Agreement",
    "Cookie Terms",
    "Cookie Notice",
    "Cookie Information",
    "Cookie Protocol",
    "Cookie Rules",
    "Cookie Regulation",
    "Cookie Policy Statement",
    "Cookie Consent Policy"
]

def PrivacyPolicySearch(links : list, url : str):
    privacy_link = None
    for link in links:
        for p in privacy_policy_phrases:
            if  p.lower() in link.text.lower():
                privacy_link = link.get('href')
                if privacy_link[0:4] != 'http':
                    privacy_link = url + privacy_link
                break
    if privacy_link:
        print("Privacy Policy - ", privacy_link)
        return privacy_link
    else:
        print("Privacy Policy not found")
        return None
        
def TermsSearch(links : list, url : str):
    terms_link = None
    for link in links:
        for p in terms_and_conditions_phrases:
            if p.lower() in link.text.lower():
                terms_link = link.get('href')
                if terms_link[0:4] != 'http':
                    terms_link = url + terms_link
                break
    if terms_link:
        print("Terms - ", terms_link)
        return terms_link
    else:
        print("Terms link not found")
        return None

def CookieSearch(links : list, url : str):
    cookie_link = None
    for link in links:
        for p in cookie_policy_phrases:
            if p.lower() in link.text.lower():
                cookie_link = link.get('href')
                if cookie_link[0:4] != 'http':
                    cookie_link = url + cookie_link
                break
    if cookie_link:
        print("Cookie Policy - ", cookie_link)
        return cookie_link

    else:
        print("Cookie Policy not Found")
        return None
    
def main(weblink):
    url = weblink

    parsed_url = urlparse(url)
    base_url = parsed_url.scheme + "://" + parsed_url.netloc

    print("BASE URL - ", base_url)

    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    links = soup.find_all('a')

    print("\nLinks:\n")

    privacy_link = PrivacyPolicySearch(links, base_url) 
    terms_link = TermsSearch(links, base_url)
    cookie_link = CookieSearch(links, base_url)

    return {"Privacy Link" : privacy_link, "Terms & Conditions" : terms_link, "Cookie Policy" : cookie_link}




# privacy_policy_links = soup.find_all('a', string=lambda text: text and 'privacy policy' in text.lower())

# if privacy_policy_links:
#     # Print the link(s) to the privacy policy
#     print("Privacy Policy Link(s):")
#     for link in privacy_policy_links:
#         print(link.get('href'))
# else:
#     print("No Privacy Policy link found on the page.")