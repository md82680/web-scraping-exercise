import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter the URL: ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Find all span tags with class="comments"
spans = soup.find_all('span', class_='comments')

#Sum the numbers in the span tags
total= sum(int(span.contents[0]) for span in spans)
count = len(spans)

print(f"Count: {count}")
print(f"Total: {total}")
