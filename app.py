from flask import Flask 

app = Flask(__name__)

# use route() decorator to tell Flask what URL should trigger our function.
@app.route("/")
def index():
    return "welcome to the home page"

@app.route("/intro")
def intro():
    return "This is Siddharth"


if(__name__ == "__main__"):
    app.run(debug=True)
    #app.run(debug=True , port = 8000)
