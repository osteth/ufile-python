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


def download(USER, KEY, SLUG):
    requests.get('https://down.uploadfiles.io/get/' + str(SLUG), auth=(str(USER), str(KEY)))
    return()
    
if __name__ == "__main__":
    main()