import urllib.request
import random
import string
import sys
import pathlib

if len(sys.argv) < 2:
    print('ERROR: Downloader requires number of images to be downloaded as argument, download directory optional')
    quit()

if int(sys.argv[1]) <= 0:
    print('ERROR: Number of images to be downloaded must be larger than 0')
    quit()

print('Random PNG File Download started')

def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

dir = 'download'

if len(sys.argv) == 3:
        dir = str(sys.argv[2])

pathlib.Path(dir).mkdir(parents=True, exist_ok=True)

for x in range(0, int(sys.argv[1])):
    try:
        x = random.randrange(100,1000)
        y = random.randrange(100,1000)
        url = 'https://picsum.photos/' + str(x) + '/' + str(y)
        urllib.request.urlretrieve(url, dir + '/' + randomString(20) + '.jpg')
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        print('ERROR: Encountered exception, dropping request')
