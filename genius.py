import lyricsgenius
import pylast

#The LastFM keys
API_KEY= ''
API_SECRET = ''
#The genius key
genius = lyricsgenius.Genius("")

#Your usename and password
username = 'username'
password_hash = pylast.md5('password')

#Access LastFm
network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)

#Authentication
user = network.get_authenticated_user();

#Get current song in lastfm
song = user.get_now_playing()

#Get name of song
artist = network.get_artist(song)
artist1 = pylast.Artist(song.artist, artist.network)

#Search the lyrics in genius by the song's name
song = genius.search_song(song)

#Take the artists bio from lastfm
bio = artist1.get_bio_summary(language='en')

#And print everything, for some reason artist.name give the artist and song name
print('\n',artist.name, '\n')
print(song.lyrics, '\n\n')
print('SUMMARY','\n\n',bio)


