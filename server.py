from firebase import firebase
from flask import Flask
app= Flask(__name__)
firebase_in=firebase.FirebaseApplication("https://credit-card-fraud-flask-default-rtdb.firebaseio.com/")

@app.route("/")
def home():
    result=firebase_in.get("/Restaraunts",None)
    return str(result)

if __name__ =="__main__":
    app.run()