
from flask import Flask, render_template, request
import secrets
import string

app = Flask(__name__)

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
    app.run(debug=True)
