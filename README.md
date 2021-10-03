# Image Validator
CGI script that recieves the URL of an image file as a parameter, checks that it's below a given size (4 MiB by default) and that its file type is acceptable (default: jpeg or png). Useful for validating files before allowing a user to submit them. 

To change defaults, edit constants in `./cgi-bin/imageValidator.py`

Check [https://docs.python.org/3/library/imghdr.html](https://docs.python.org/3/library/imghdr.html) for a list of file formats that can be detected.


