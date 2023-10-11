import cgi
import html

form = cgi.FieldStorage()


username = form.getfirst("name", "undefined")
age = form.getfirst("age", "undefined")

username = html.escape(username)
age = html.escape(age)

doSport = form.getvalue("doSport", "undefined")

genres = ["Novel", "Fantasy", "Detective", "Nonfiction"]
checkedGenres = []

for group in genres:
    if group in form:
        checkedGenres.append(group)


print(f"""
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Обробка форми</title>
</head>
<body>
    <p>Your name: {username}</p>
    <p>Your age: {age}</p>
    <p>Do you do sports? - {doSport}</p>
    <p>Your favorite genres of books: {", ".join(checkedGenres)}</p>
</body>
</html>
""")
