import urllib.request
import random
import string
import sys
import pathlib
import pytube
import os
import json
import urllib.request
import string

if len(sys.argv) < 2:
    print('ERROR: Downloader requires number of videos to be downloaded as argument, download directory optional')
    quit()

if int(sys.argv[1]) <= 0:
    print('ERROR: Number of videos to be downloaded must be larger than 0')
    quit()

print('Random YouTube File Download started')

count = 50
API_KEY = '[REDACTED]'
randomObj = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))

def randomString(stringLength=10):
    letters = string.ascii_lowercase
    letters = letters + "0123456789"
    return ''.join(random.choice(letters) for i in range(stringLength))

dir = 'download'

if len(sys.argv) == 3:
    dir = str(sys.argv[2])

pathlib.Path(dir).mkdir(parents=True, exist_ok=True)

for x in range(0, int(sys.argv[1])):
    try:
        urlData = "https://www.googleapis.com/youtube/v3/search?key={}&maxResults={}&part=snippet&type=video&q={}".format(API_KEY,count,randomObj)
        webURL = urllib.request.urlopen(urlData)
        data = webURL.read()
        encoding = webURL.info().get_content_charset('utf-8')
        results = json.loads(data.decode(encoding))
        for data in results['items']:
            try:
                videoId = (data['id']['videoId'])
                print(videoId)
                #store your ids
                url = 'https://www.youtube.com/watch?v=' + videoId
                print('Downloading ' + url)
                youtube = pytube.YouTube(url)
                videos = youtube.streams.filter(subtype='mp4')
                video = random.choice(videos)
                outVideo = video.download()
                os.rename(outVideo, dir + '/' + randomString(20) + '.mp4')
            except (KeyboardInterrupt, SystemExit):
                raise
            except:
                print('ERROR: Encountered exception, dropping single video request')
                raise
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        print('ERROR: Encountered exception, dropping 50 requests')
        raise
