import pylast
import urllib.request

API_KEY= '24c6a83580684f02a7f98eff7fbfc24a'
API_SECRET = '11e9b37aa5ca43b7a9d049af143c6123'


network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET)
                               

user = network.get_authenticated_user();

user = network.get_user("beingvalentine")
image = user.get_image()

print(image)
file2write=open("men.txt",'w')
file2write.write(image)
file2write.close()

def dl_png(url, file_path, file_name):
	full_path = file_path + file_name + '.png'
	urllib.request.urlretrieve(url, full_path)

url = image
file_name = 'men'

dl_png(url,'c:/users/raujo/chords/', file_name)