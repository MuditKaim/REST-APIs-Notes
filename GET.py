''''
This file is used to send a GET request to the Spotify Downloader API to download a song from Spotify.
The song can be specified by the songId parameter in the query string.
The songId parameter should be a Spotify song URL.
The response will be a JSON object containing the download link for the song.
'''
import requests #importing requests module
import time


# Request URL
url = "https://spotify-downloader9.p.rapidapi.com/downloadSong"

headers = {
	"x-rapidapi-key": "be66b9a47emsh51482eb6cc9732ap18309cjsn51d8aa14fbef",
	"x-rapidapi-host": "spotify-downloader9.p.rapidapi.com"
}

# Query String
'''
Query parameters are appended to the request URL to pass specific data to the server. 
They are part of the URL and typically follow a ? character. Multiple parameters are separated by &
'''
# querystring = {"songId":"https://open.spotify.com/track/7jT3LcNj4XPYOlbNkPWNhU"} #Killers from the North Side
querystring = [{"songId":"https://open.spotify.com/track/27NovPIUIRrOZoCHxABJwK?si"},
               {"songId":"https://open.spotify.com/track/67BtfxlNbhBmCDR2L2l8qd?si"},
               {"songId":"https://open.spotify.com/track/0F7FA14euOIX8KcbEturGH?si"}]
# headers=headers
# params=querystring
for i in querystring:
    req=requests.get(url,headers=headers,params=i)
    print(req.json())
    time.sleep(5)

# Headers
'''
Headers in an HTTP request provide additional metadata or information about the request being sent to the server. 
'''



# Sending GET request
'''
The get() method sends a GET request to the specified url.
more info: https://www.w3schools.com/python/module_requests.asp
'''
# response = requests.get(url, headers=headers, params=querystring)



# Printing response
# print(response.json())

'''
JSON: JavaScript Object Notation
JSON is a lightweight data-interchange format that is easy for humans
 to read and write and easy for machines to parse and generate.
 It is based on a subset of the JavaScript Programming Language.
'''
