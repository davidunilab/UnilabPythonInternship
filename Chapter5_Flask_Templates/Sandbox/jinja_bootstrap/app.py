from flask import Flask, render_template, url_for

serverPort = 8081

app = Flask(__name__)

pages = (
    ("home", "home",),
    ("about us", "about")
)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/about_us')
def about():
    return render_template("about_us.html", pages=pages)


if __name__ == '__main__':
    app.run(port=serverPort, debug=True)
