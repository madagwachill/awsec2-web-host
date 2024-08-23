from flask import Flask, request, render_template, redirect, url_for

app = Flask (__name__)

@app.route('/')
def home():
    return "WelCome Home"

@app.route('/save_data', methods = ["GET"])
def save_data():
    regno = request.args['regno']
    name= request.args['name']
    standard = request.args['class']
    math = request.args['math']
    science = request.args['science']
    computer = request.args['computer']
    print(regno,name,standard,math,science,computer)
    
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run()