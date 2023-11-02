import requests
from bs4 import BeautifulSoup

genius_token = "pM8yQkIdbKsn8iNlzZq4o030b-0HI9Iz_mLaXweN2yXddCtdqeui_XuAWltUHHNx"

def search_song_lyrics(song_title, artist_name):
    base_url = "https://api.genius.com"
    headers = {
        "Authorization": f"Bearer {genius_token}"
    }

    # Search for the song
    search_url = f"{base_url}/search"
    params = {
        "q": f"{song_title} {artist_name}"
    }

    response = requests.get(search_url, headers=headers, params=params)
    data = response.json()

    # Check if there are hits in the response
    if "hits" in data["response"]:
        song_url = data["response"]["hits"][0]["result"]["url"]

        # Access the URL of the song to get the lyrics
        response = requests.get(song_url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            # Try to find the lyrics in the page
            lyrics_div = soup.find("div", class_="lyrics")
            if lyrics_div:
                lyrics = lyrics_div.get_text()
                return lyrics

    return None

song_title = "Light Yagami"
artist_name = "Kira"
lyrics = search_song_lyrics(song_title, artist_name)

if lyrics:
    print(f"Lyrics for {song_title} by {artist_name}:\n")
    print(lyrics)
else:
    print("Lyrics not found.")
