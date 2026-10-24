
from flask import Flask, render_template, request, send_from_directory
import secrets
import string
import os

app = Flask(__name__)

@app.route("/robots.txt")
def robots():
    return send_from_directory(
        os.path.dirname(os.path.abspath(__file__)),
        "robots.txt"
    )

@app.route("/", methods=["GET", "POST"])
def home():
    password = ""

    if request.method == "POST":
        length = int(request.form.get("length", 12))
        length = max(4, min(length, 64))

        characters = ""

        if request.form.get("uppercase"):
            characters += string.ascii_uppercase

        if request.form.get("lowercase"):
            characters += string.ascii_lowercase

        if request.form.get("numbers"):
            characters += string.digits

        if request.form.get("symbols"):
            characters += "!@#$%&*?"

        if characters:
            password = "".join(
                secrets.choice(characters)
                for _ in range(length)
            )

    return render_template("index.html", password=password)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
