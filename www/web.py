import cgi

import bottle
from bottle import get, post, request, run

import libkinkaid


@get("/")
def index():
    return """\
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>Kincode translator</title>
    <style>
        textarea {
            resize: vertical;
        }
    </style>
</head>
<body>
    <div>
        <h2>Decode</h2>
        <form method="post" action="/decode">
            <textarea name="source" cols="100" rows="5"></textarea>
            <br>
            <button type="submit">Decode</button>
        </form>
    </div>
    <div>
        <h2>Encode</h2>
        <form method="post" action="/encode">
            <textarea name="source" cols="100" rows="5"></textarea>
            <br>
            <button type="submit">Encode</button>
        </form>
    </div>
</body>
</html>
"""


def generate_result_page(result):
    result = cgi.escape(result)
    return f"""\
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <title>Kincode translator result</title>
</head>
<body>
    <a href="./">Back to home page</a>
    <hr>
    {result}
</body>
</html>
"""


@post("/decode")
def decode():
    source = request.forms.source
    result = libkinkaid.decode(source)
    return generate_result_page(result)


@post("/encode")
def encode():
    source = request.forms.source
    result = libkinkaid.encode(source)
    return generate_result_page(result)


if __name__ == "__main__":
    run(host="localhost", port=8000, reloader=True)
else:
    application = bottle.default_app()
