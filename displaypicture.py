from flask import Flask, render_template
import os
import logging
from flask import Flask

app = Flask(__name__)

@app.route("/")

@app.route('/home')
def pict():
   return render_template('home.html')
   

if __name__ == '__main__':
    print("This is Sai")
    app.run(debug=True,host='0.0.0.0')






