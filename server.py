from flask import Flask, render_template, request, redirect, session
import random


app = Flask(__name__)
app.secret_key = 'the game is secure af'

@app.route('/')
def numberGuess():
    if not 'secret' in session:
        session['secret'] = random.randint(1,100)
    return render_template("index.html")

@app.route('/guess', methods = ['POST'])
def guessChecker():
    if session['secret'] > int(request.form['guess']):
        session['result'] = "Too low"
    elif session['secret'] < int(request.form['guess']):
        session['result'] = "Too high"
    else:
        session['result'] = "You win!"
    return redirect ('/')

@app.route('/clear')
def clearSecret():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)