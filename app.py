from flask import Flask, render_template, request, jsonify
import pdfplumber
import os
from regex_generator import generate_regex

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"


def extract_text(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                text += t + "\n"
    return text


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        file = request.files["file"]
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)

        text = extract_text(path)

        regex = generate_regex(text)

        return jsonify({
            "text_preview": text[:1000],
            "generated_regex": regex
        })

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
