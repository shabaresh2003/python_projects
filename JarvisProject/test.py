import spotipy
import speech_recognition as sr
from spotipy.oauth2 import SpotifyOAuth
recognizer = sr.Recognizer()
SPOTIPY_CLIENT_ID = 'ca3e1c889df34a2ca2912dd792206351'
SPOTIPY_CLIENT_SECRET = '7df10a6f1b4e43dd9cd27abc1ea71649'
SPOTIPY_REDIRECT_URI = 'http://localhost:8080'

# Replace these with your actual Spotify API credentials

# Initialize Spotify API with a stored refresh token
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="user-library-read user-read-playback-state user-modify-playback-state",
                                               open_browser=False,  # Disable opening the browser
                                               cache_path="token.txt"))  # Cache path for refresh token

# Initialize Speech Recognition
recognizer = sr.Recognizer()

def play_music(command):
    if "play music" in command:
        # Replace 'your_playlist_id' with the actual playlist ID
        playlist_id = 'https://open.spotify.com/playlist/5kt7PQM5zn0YBErJ4BKJkR?si=a6c30ffd2b314c0a'

        # Use the Spotify API to play the specified playlist
        sp.start_playback(context_uri=f'spotify:playlist:{playlist_id}')

# Main loop
while True:
    with sr.Microphone() as source:
        print("Listening for a command...")
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print("You said: ", command)
        play_music(command)
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print(f"Error with the speech recognition service; {e}")
