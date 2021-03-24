import requests
from bs4 import BeautifulSoup as bs

github_user = input('\nEnter GitHub Username: ')
url = f'https://github.com/{github_user}'

my_request = requests.get(url)

soup = bs(my_request.content, 'html.parser')
profile_image = soup.find('img', {'alt': 'Avatar'})['src']

print(f"\nHere's the link to the avatar: {profile_image}")
print('\n')