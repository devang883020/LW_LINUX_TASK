
# import requests 
# URL = "https://www.geeksforgeeks.org/data-structures/" 
# r = requests.get(URL) 
# print(r.content) 

# soup = (response.content, 'html.parser')

import requests
from bs4 import BeautifulSoup

# URL of the GitHub repository
URL = "https://github.com/devang883020/LW_LINUX_TASK"
# Send a GET request to the URL
response = requests.get(URL)
# Parse the content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the <a> tags
a_tags = soup.find_all('a')

# Extract and print the file names
for tag in a_tags:
    # Check if the <a> tag has the 'title' attribute which usually contains the file name
    if tag.has_attr('title'):
        print(tag['title'])
        print(f"![alt text](https://github.com/devang883020/LW_LINUX_TASK/blob/main/{tag['title']})")
