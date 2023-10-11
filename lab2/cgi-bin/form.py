import cgi
import html
import http.cookies
import os

form = cgi.FieldStorage()

username = html.escape( form.getfirst("name", "Not specified") )
age = html.escape(form.getfirst("age", "Not specified"))
doSport = form.getvalue("doSport", "Not specified")

genres = ["Novel", "Fantasy", "Detective", "Nonfiction"]
checkedGenres = []

for group in genres:
    if group in form:
        checkedGenres.append(group)


cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
counterCookie = int(cookie.get("counter").value) + 1 if "counter" in cookie else 1

print(f"Set-cookie: counter={counterCookie};")
print("Content-type:text/html\r\n\r\n")

print(f"""
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form</title>
</head>
<body>
    <p>Your name: {username}</p>
    <p>Your age: {age}</p>
    <p>Do you do sports? - {doSport}</p>
    <p>Your favorite genres of books: {", ".join(checkedGenres)}</p>
    
    <p>Counter: {counterCookie}</p>

</body>
</html>
""")
