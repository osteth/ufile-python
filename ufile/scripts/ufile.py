#!/usr/bin/python

import requests

def main():
    return

def upload(SOURCEPATH, USER, KEY):
    files = [
        ('file', open(SOURCEPATH, 'rb')),
        ('user_id', 'USER'),
        ('auth_key', 'KEY'),
    ]

    response = requests.post('https://up.uploadfiles.io/upload', files=files)
    return(response.content)


def download(USER, KEY, SLUG, PATH):
    try:
        response = requests.get('https://up.uploadfiles.io/get/' + str(SLUG), auth=(str(USER), str(KEY)), stream=True)
    except:
        response = requests.get('http://down.uploadfiles.io/get/' + str(SLUG), auth=(str(USER), str(KEY)), stream=True)
    with open(PATH, 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    return(PATH)
    
if __name__ == "__main__":
    main()