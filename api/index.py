from flask import Flask, jsonify

app = Flask(__name__)

bible_verses = [
    {"reference": "john+3:16", "text": "For God so loved the world..."},
    {"reference": "Psalm 23:1", "text": "The Lord is my shepherd..."}
]

@app.route("/verses", methods=["GET"])
def get_verses():
    return jsonify(bible_verses)

@app.route("/verse/<reference>", methods=["GET"])
def get_verse(reference):
    verse = next((v for v in bible_verses if v["reference"] == reference), None)
    if verse:
        return jsonify(verse)
    else:
        return jsonify({"message": "Verse not found"}), 404

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

if __name__ == "__main__":
    app.run(debug=True)
