# Image Validator
CGI script that recieves the URL of an image file as a parameter, checks that it's below a given size and that its file type is acceptable. Useful for validating files before allowing a user to submit them. 

## Defaults
To change defaults, edit constants in `./cgi-bin/imageValidator.py`
Maximum file size: 4 MiB
Allowed file formats: jpeg, png

Check [https://docs.python.org/3/library/imghdr.html](https://docs.python.org/3/library/imghdr.html) for a list of file formats that can be detected.

## Testing
Probably not how you'd ever run this in production, but imageValidator.html is a barebones but functional front end.

To launch test environment

`python -m http.server --cgi 8000`

