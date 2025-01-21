import urllib.request
import re

def get_wikipedia_content(page_title):
    url = f"https://en.wikipedia.org/wiki/{page_title}"
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')
    
    # Remove HTML tags using a regular expression
    text = re.sub(r'<[^>]+>', '', html)
    return text

# List of common Wikipedia page titles
page_titles = ["Python_(programming_language)", "Artificial_intelligence", "Machine_learning"]

# Loop through the list and print the result
for title in page_titles:
    content = get_wikipedia_content(title)
    print(f"Content for {title}:\n{content}\n")