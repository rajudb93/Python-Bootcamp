import requests
from bs4 import BeautifulSoup

# URL of a Wikipedia page (example)
url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'

# Fetching the content from the URL
response = requests.get(url)

# Parsing the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Extract and print the first few lines of the introduction section (paragraphs before the first heading)
intro_paragraphs = []
for p in soup.select('p'):
    text = p.get_text().strip()
    if text:
        intro_paragraphs.append(text)
    if len(intro_paragraphs) >= 3:  # print first 3 paragraphs of intro
        break

print('Introduction Section:')
for para in intro_paragraphs:
    print(para)
    print()

# Extract and print few lines from the 'History' section
history_heading = soup.find(id='History')
history_content = []
if history_heading:
    for sibling in history_heading.parent.find_next_siblings():
        if sibling.name == 'h2':  # next main section
            break
        if sibling.name == 'p':
            history_content.append(sibling.get_text().strip())
        if len(history_content) >= 3:
            break

print('History Section:')
for para in history_content:
    print(para)
    print()
