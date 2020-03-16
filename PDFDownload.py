import urllib.request
import urllib
import random
import string
import sys
import pathlib
from bs4 import BeautifulSoup
import re

if len(sys.argv) < 2:
    print('ERROR: Downloader requires number of images to be attempted to download as argument, download directory optional')
    quit()

if int(sys.argv[1]) <= 0:
    print('ERROR: Number of PDFs to be attempted to download must be larger than 0')
    quit()

print('Random PDF File Download started')

def randomString(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

dir = 'download'

if len(sys.argv) == 3:
        dir = str(sys.argv[2])

pathlib.Path(dir).mkdir(parents=True, exist_ok=True)

for x in range(0, int(sys.argv[1])):
    try:
        html_page = urllib.request.urlopen("https://dare.uva.nl/search?browse-all=yes;docsPerPage=1;startDoc=" + str(x))
        soup = BeautifulSoup(html_page, features="html.parser")
        for link in soup.findAll('a'):
            #if link.get('href').startswith('https://pure.uva.nl/ws/files/'):
            if link.get('href').endswith('.pdf'):
                print(link.get('href'))
                urllib.request.urlretrieve(link.get('href'), dir + '/' + randomString(20) + '.pdf')
    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        print('ERROR: Encountered exception, dropping request')
