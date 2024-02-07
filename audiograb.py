from pytube import YouTube
import sys
import time

url = ''

def download_audio(yt):
    title = yt.title
    dl_Size = yt.streams.filter(only_audio=True).first().filesize_mb

    print('Title:', title)
    print('Size:', dl_Size)

    download = False

    while(download == False):

        print('This file is ' + str(dl_Size) + ' megabytes. Do you want to download it? (y/n)')
        response = input()

        if response == 'y':
            yt.streams.filter(only_audio=True).first().download('audio')
            print('Download complete')
            download = True
        
        elif response == 'n':
            print('Download aborted')
            download = True
            time.sleep(2)
            sys.exit()

        else:
            print('Please enter a valid response')
            response = input()
            download = False
    
    return

args = sys.argv[1:]

if len(args) > 1:
    print('Usage: python file.py <url>')
    print('Can only accept one argument')
    
    print('\nPlease enter a valid url:')
    url = input()

elif len(args) == 1:
    url = sys.argv[1]

else:
    print('Please enter a valid url:')
    url = input()

yt = YouTube(url)

download_audio(yt)


