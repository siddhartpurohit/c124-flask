from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route("/")
def api():
    return "Welcome "

tasks = [
     {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
     },
     {
        'id': 2,
        'title': u'studying',
        'description': u'Maths,Hindi,English,Scince,SocialScince', 
        'done': False
    },
]

@app.route("/add-data" , methods = ["POST"])
def AddTasks():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
            
        } , 400)
    t = {
        'id': tasks[-1]["id"]+1,
        'title': request.json["title"],
        'description': request.json.get("description"," "), 
        'done': False
    }
    tasks.append(t)
    return jsonify({
        "status":"success",
        "message":"task added successfully"
    })

@app.route("/getdata")
def getdata():
    return jsonify({
        "data" : tasks
    })

if(__name__ == "__main__"):
 app.run(debug = True)
