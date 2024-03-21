# import requests
# from bs4 import BeautifulSoup

# def scrape_website(url):
#   response = requests.get(url)
#   soup = BeautifulSoup(response.content, 'html.parser')
#   return soup

# # Example usage
# url = "https://www.booking.com/index.en-gb.html?label=gen173nr-1BCAEoggI46AdIM1gEaGyIAQGYAQm4AQfIAQzYAQHoAQGIAgGoAgO4Au3bx68GwAIB0gIkOWM1MTI5OTQtMDU2MS00MmYwLTgxMjktNmEwNDkyYmQ5YjVm2AIF4AIB&sid=8b1cec082ed78680427b987b53ee5660&keep_landing=1&sb_price_type=total&"  # Replace with target website
# soup = scrape_website(url)

# with open("text.txt", 'w') as f:
#   f.write(str(soup))
#   f.close()



import requests
from bs4 import BeautifulSoup

def extract_tag_content(url, tag):
  """
  Extracts the content of all tags specified by 'tag' from a website.

  Args:
      url: The URL of the website to scrape.
      tag: The HTML tag name (e.g., 'p', 'h1', 'div')

  Returns:
      A list of strings containing the content of each matching tag.
  """
  # Fetch the website content
  response = requests.get(url)
  response.raise_for_status()  # Raise an error for bad status codes

  # Parse the HTML content
  soup = BeautifulSoup(response.content, 'html.parser')

  content = []
  for i in tag:
    tags = soup.find_all(i)  
    for item in tags:
        content.append(item.text.strip().replace('\n',''))

  return content

def txtmani(target_url : str):
    text_containing_tags = [
        "p", "h1", "h2", "h3", "h4", "h5", "h6", 
        "span", "div",  
        "a",  
        "li",  
        "pre",  
        "blockquote",  
        "caption",  
        "optgroup", "option", 
        "label",
        "b", "i", "strong", "em", 
        "sub", "sup", 
        "mark",
    ]
    extracted_content =  extract_tag_content(target_url, text_containing_tags)

    # Print the extracted content
    with open("text1.txt", "w") as f: 
        for item in extracted_content:
            for i in item : 
                f.write(i)
        f.close()


        



