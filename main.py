import requests
from bs4 import BeautifulSoup


# user_date = input("What year you would like to travel to ? type a date in YYY-MM-DD format:\n")

# request_url = f"https://www.billboard.com/charts/hot-100/{user_date}/"   # 2000-08-12
request_url = f"https://www.billboard.com/charts/hot-100/2000-08-12/"   # 2000-08-12
response = requests.get(request_url)
soup = BeautifulSoup(response.text, features="html.parser")

filtered_list = soup.select("li ul li h3")
songs_names = [song.getText(strip=True) for song in filtered_list]
print(songs_names)

