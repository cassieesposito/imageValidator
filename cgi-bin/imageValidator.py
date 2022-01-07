#!/usr/bin/python3

import cgi
import requests
import imghdr
import io


# Many web hosts will refuse to respond to requests from a script. Sending a false UA solves this.
USER_AGENT = "Mozilla/5.0 (Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0"
HEADERS = {"User-Agent": USER_AGENT}
MAX_FILE_SIZE_IN_BYTES = 1024 * 1024 * 4
ACCEPTABLE_MIME_TYPES = ["image/jpeg", "image/png", "image/gif"]
ACCEPTABLE_IMAGE_TYPES = ["jpeg", "png", "gif"]
IMAGE_URL = cgi.FieldStorage().getvalue("imageURL")


def main():
    print("Content-type: text/plain")
    print("")
    print(validate())


def validate():
    try:
        r = requests.head(IMAGE_URL, headers=HEADERS)
    except:
        return "Could not fetch file headers"

    try:
        if int(r.headers["Content-Length"]) > MAX_FILE_SIZE_IN_BYTES:
            return "Image header reports file too large"
    except:
        return "Image headers do not contain Content-Length"

    try:
        if r.headers["Content-Type"] not in ACCEPTABLE_MIME_TYPES:
            return "Image header reports unacceptable mime type"
    except:
        return "Image headers do not contain Content-Type"

    try:
        r = requests.get(IMAGE_URL, stream=True, headers=HEADERS)
    except:
        return "Could not fetch file"

    try:
        if r.status_code == 200:
            r.raw.decode_content = True
            content = r.raw.read(MAX_FILE_SIZE_IN_BYTES + 1)
            if len(content) > MAX_FILE_SIZE_IN_BYTES:
                return "File size is too large"
        else:
            return "HTTP Response Code: {}".format(r.status_code)
    except:
        return "Error while fetching file"

    try:
        fileType = imghdr.what(io.BytesIO(content))
        if fileType in ACCEPTABLE_IMAGE_TYPES:
            return "OK"
        return "Bad file type"
    except:
        return "Error while determining file type"


main()
