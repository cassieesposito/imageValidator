# Image Validator
CGI script that recieves the URL of an image file as a parameter, checks the http headers to see if it's reported as below a given size and that the mime type is of an acceptable type. Then it downloads the file to the server, verifies the image is actually of that type and an acceptable size. This could be useful for validating files before allowing a user to submit them. It could be extended to non-image formats by using the python-magic library instead of built in library imghdr, but that adds additional requirements, so I haven't done that. Yet.

## Defaults
To change defaults, edit constants in `./cgi-bin/imageValidator.py`
Maximum file size: 4 MiB
Allowed file formats: jpeg, png, gif

Check [https://docs.python.org/3/library/imghdr.html](https://docs.python.org/3/library/imghdr.html) for a list of file formats that can be detected.

## Testing
Probably not how you'd ever run this in production, but imageValidator.html is a barebones but functional front end.

To launch test environment:
`python -m http.server --cgi 8000`

Then navigate to:
`http://localhost:8000/imageValidator.html`

