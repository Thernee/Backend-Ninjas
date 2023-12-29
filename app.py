from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
  return "Hello, World!"

@app.route("/about", methods=['GET'])
def about():
  brief_data = {
    "gender": "male",
    "github_url": "https://github.com/Thernee",
    "name": "Abubakar Sani",
    }
  return jsonify(brief_data), 200, {'Content-Type': 'application/json'}, brief_data

if __name__ == "__main__":
  app.run(debug=True)