import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

client_id = "fe796063d2bf459cb927a394ce9f0065"
client_secret = "aa945af70b9947e1b42e954857a7e447"
# user_date = input("What year you would like to travel to ? type a date in YYY-MM-DD format:\n")

# # request_url = f"https://www.billboard.com/charts/hot-100/{user_date}/"   # 2000-08-12
# request_url = f"https://www.billboard.com/charts/hot-100/2000-08-12/"   # 2000-08-12
# response = requests.get(request_url)
# soup = BeautifulSoup(response.text, features="html.parser")
#
# filtered_list = soup.select("li ul li h3")
# songs_names = [song.getText(strip=True) for song in filtered_list]
# print(songs_names)

# Set up credentials

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
# sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

spOth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri="http://example.com")
spOth.get_auth_response()
# Now you can make API calls with your authenticated Spotify instance
# results = sp.current_user()
# print(results)
