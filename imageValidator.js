getURL = async () => {
  imageURL = document.getElementById("imageURL").value
  console.log(imageURL)
  let response = await fetch('/cgi-bin/imageValidator.py?imageURL=' + imageURL)
  let text = await response.text()

  document.getElementById("imageOutput").src = imageURL
  document.getElementById("validDIV").innerHTML = text
}
