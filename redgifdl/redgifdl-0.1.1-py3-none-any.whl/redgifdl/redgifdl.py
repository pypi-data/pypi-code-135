import sys
import traceback
import requests


def download_url(redgifs_url, filename):
    sys.stdout.reconfigure(encoding='utf-8')
    API_URL_REDGIFS = 'https://api.redgifs.com/v2/gifs/'
    try:
        print("redgifs_url = {}".format(redgifs_url))

        #Get RedGifs video ID
        redgifs_ID = redgifs_url.split('/watch/', 1)
        redgifs_ID = redgifs_ID[1]
        print("redgifs_ID = {}".format(redgifs_ID))
        
        sess = requests.Session()
        
        request = sess.get(API_URL_REDGIFS + redgifs_ID)
        print(request)
        
        if request is None:
            return
        else:
            rawData = request.json()
            #Get HD video url
            hd_video_url = rawData['gif']['urls']['hd']
            print("URL = {}".format(hd_video_url))
            
            with sess.get(hd_video_url, stream=True) as r:
                with open(filename, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192): 
                        f.write(chunk)

            return hd_video_url
    except Exception:
        traceback.print_exc()
        return