import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import pprint

# todo: when finished do not share my sensitive keys on github

client_id = "fe796063d2bf459cb927a394ce9f0065"
client_secret = "aa945af70b9947e1b42e954857a7e447"

# ----------------- Scraping billboard 100 -------------------------
# user_date = input("What year you would like to travel to ? type a date in YYY-MM-DD format:\n")

# request_url = f"https://www.billboard.com/charts/hot-100/{user_date}/"   # 2000-08-12
request_url = f"https://www.billboard.com/charts/hot-100/2000-08-12/"   # 2000-08-12
response = requests.get(request_url)
soup = BeautifulSoup(response.text, features="html.parser")

filtered_list = soup.select("li ul li h3")
songs_names = [song.getText(strip=True) for song in filtered_list]
print(songs_names[2])


# ------------------------------ Spotify authentication --------------------------------
spOth = SpotifyOAuth(client_id=client_id,
                     client_secret=client_secret,
                     redirect_uri="http://example.com",
                     cache_path=".cache")

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager,
                     oauth_manager=spOth,
                     auth_manager=spOth
                     )

# Now you can make API calls with your authenticated Spotify instance
# results = sp.current_user()["id"]
results = sp.search(q=f"track: {songs_names[2]} year: 2000", type="track", limit=1)
pprint.pprint(results["tracks"]["items"][0]["external_urls"]["spotify"])
# print(results)

# ---------------------create a list of Spotify song URIs ----------------------
