#!/usr/bin/python3

import cgi
import requests
import imghdr
import io


# Many web hosts will refuse to respond to requests from a script. Sending a false UA solves this.
USER_AGENT = "Mozilla/5.0 (Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0"
MAX_FILE_SIZE_IN_BYTES = 1024 * 1024 * 4
ACCEPTABLE_IMAGE_TYPES = ["jpeg", "png"]


def main():
    print("Content-type: text/plain")
    print("")
    print(validate())


def validate():
    try:
        imageURL = cgi.FieldStorage().getvalue("imageURL")
        r = requests.get(imageURL, stream=True, headers={"User-Agent": USER_AGENT})
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
        return "Unknown error while fetching file"

    try:
        fileType = imghdr.what(io.BytesIO(content))
        if fileType in ACCEPTABLE_IMAGE_TYPES:
            return "OK"
        return "Bad file type"
    except:
        return "Unknown error while determining file type"


main()
