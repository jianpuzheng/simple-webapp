# app.py
import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/how are you')
def hello():
    return 'I am good, how aboutuser@PC12-SALLE1:~/projet/simple-webapp$ 

if __name__ == "__main__":
    app.run()
~               
