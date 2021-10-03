#!/usr/bin/python3

import cgi
import cgitb

imageURL = cgi.FieldStorage().getvalue("imageURL")

print("Content-type:application/json")
print("")
print(imageURL)
