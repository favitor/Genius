import pylast
import urllib.request

API_KEY= ''
API_SECRET = ''


network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET)
                               

user = network.get_authenticated_user();

user = network.get_user("username")
image = user.get_image()

print(image)
#Save Url in txt file
file2write=open("men.txt",'w')
file2write.write(image)
file2write.close()

#Function to save image as png
def dl_png(url, file_path, file_name):
	full_path = file_path + file_name + '.png'
	urllib.request.urlretrieve(url, full_path)

url = image
file_name = 'men'

dl_png(url,'c:/', file_name)
