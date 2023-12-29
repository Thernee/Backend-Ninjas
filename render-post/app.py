from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
  return "Hello, World!"

@app.route("/about")
def about():
  brief_data = {"gender": "male", "github_url": "https://github.com/Thernee", "name": "Abubakar Sani"}
  return brief_data

if __name__ == "__main__":
  app.run(debug=True)