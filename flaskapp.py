from flask import Flask,jsonify, request

app = Flask(__name__)

List = [
    {
        'id': 1,
        'Name': u'Raju',
        'Contact': u'9987644456', 
        'done': False
    },
    {
        'id': 2,
        'Name': u'Rahul',
        'Contact': u'9876543222', 
        'done': False
    }
]

@app.route("/")
def hello_world():
    return "Hello World!"
#Code to create a route with POST Method(refer hint1)

#code to create a contact json object(refer hint2)
    
    List.append(contact)
    return jsonify({
        "status":"success",
        "message": "Contact added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : List
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)