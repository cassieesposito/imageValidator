#!/usr/bin/python3

import cgi
import cgitb

print("Content-type:text/html")
print("")
print('<img src="{}">'.format(cgi.FieldStorage().getvalue("validateMe")))
