import lyricsgenius
import pylast

#The LastFM keys
API_KEY= '24c6a83580684f02a7f98eff7fbfc24a'
API_SECRET = '11e9b37aa5ca43b7a9d049af143c6123'
#The genius key
genius = lyricsgenius.Genius("F7oI8L-wAKEwTuQmSOAl4K6aNrARtu3NMiZRwRa7mgdqeRAZBIxv2glvHsg_HcmN")

#Your usename and password
username = 'vitorfa'
password_hash = pylast.md5('C@poeira07')

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


