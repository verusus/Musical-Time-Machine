import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import pprint

user_id = YOUR_USER_ID_HERE  # the Username on the spotify account
client_id = APP_CLIENT_ID_HERE  # client_id and client_secret get them from the app created on spotify developers
# website
client_secret = APP_CLIENT_SECRET_HERE

# ----------------- Scraping billboard 100 -------------------------
user_date = input("What year you would like to travel to ? type a date in YYY-MM-DD format:\n")
year = user_date.split("-")[0]

request_url = f"https://www.billboard.com/charts/hot-100/{user_date}/"  # 2000-08-12

response = requests.get(request_url)
soup = BeautifulSoup(response.text, features="html.parser")

filtered_list = soup.select("li ul li h3")
songs_names = [song.getText(strip=True) for song in filtered_list]

# ------------------------------ Spotify authentication --------------------------------

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-read-private playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)

# ---------------------create a list of Spotify song URIs ----------------------
songs_uris = []
for song_name in songs_names:
    try:
        results = sp.search(q=f"track: {song_name} year: 2000", type="track", limit=1)
        uri = results["tracks"]["items"][0]["uri"]
    except:
        print(f"The song {song_name} does not exist on spotify!")
    else:
        songs_uris.append(uri)

# -------------------------- Create a playlist with the songs -------------------
results = sp.user_playlist_create(user=user_id, name=f"{user_date} Billboard 100", description="", public=False)
playlist_id = results["id"]

adding_tracks_r = sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=songs_uris)
print(adding_tracks_r)



# # this is another way using POST method possible (must read documentation and make changes)
# def create_playlist(user_id=client_id):
#     playlist_ep = f"https://api.spotify.com/v1/users/{user_id}/playlists"
#     header_playlist = {
#         'Authorization': f"Bearer {os.getenv('CREATE_PLAYLIST_TOKEN')}"
#     }
#
#     create_pl_parameters = {
#         'name': f"{year}-{month}-{day} BillBoard 100",
#         'public': False,
#         'description': f"Top 100 songs from the year {year}"
#     }
#
#     pl_response = requests.post(
#         url=playlist_ep,
#         headers=header_playlist,
#         json=create_pl_parameters
#     )
#
#     print(f"Playlist response: {pl_response.status_code}")
#     # print(pl_response.text)
#
#     play_id = pl_response.json()['id']
#     # print(play_id)
#
#     print(f"Playlist ID: {play_id}")
#     return play_id
