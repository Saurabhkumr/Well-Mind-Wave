from flask import Flask, request, render_template,flash,redirect,session,abort,jsonify
from models import Model
import os

app = Flask(__name__)

#test change 

@app.route('/')
def root():
     return render_template('home.html')


@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'admin' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else :
        flash('wrong password!')
    return root()

@app.route("/log")
def logout():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        session['logged_in'] = False
        return render_template('home.html')


@app.route("/test")
def sentiment():
    return render_template("test.html")

@app.route("/doctor1")
def doc1():
    return render_template("doctor1.html")

@app.route("/doctor2")
def doc2():
    return render_template("doctor2.html")

@app.route("/doctor3")
def doc3():
    return render_template("doctor3.html")


@app.route("/aboutdes")
def aboutdes():
    return (render_template("aboutdepression.html"))

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")



@app.route('/predict', methods=["POST"])
def predict():
    answers = [request.form[f'a{i}'] for i in range(1, 15)]

    # Check if any question is unanswered
    if any(answer is None for answer in answers):
        return "Please answer all the questions."

    q1 = int(request.form['a1'])
    q2 = int(request.form['a2'])
    q3 = int(request.form['a3'])
    q4 = int(request.form['a4'])
    q5 = int(request.form['a5'])
    q6 = int(request.form['a6'])
    q7 = int(request.form['a7'])
    q8 = int(request.form['a8'])
    q9 = int(request.form['a9'])
    q10 = int(request.form['a10'])
    q11 = int(request.form['a11'])
    q12 = int(request.form['a12'])
    q13 = int(request.form['a13'])
    q14 = int(request.form['a14'])
    q15 = int(request.form['a15'])

    values = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10,q11,q12,q13,q14,q15]
    model = Model()
    classifier = model.svm_classifier()
    prediction = classifier.predict([values])
    if prediction[0] == 0:
            result = 'Your Depression test result : No Depression'
    if prediction[0] == 1:
            result = 'Your Depression test result : Mild Depression'
    if prediction[0] == 2:
            result = 'Your Depression test result : Moderate Depression'
    if prediction[0] == 3:
            result = 'Your Depression test result : Moderately severe Depression'
    if prediction[0] == 4:
            result = 'Your Depression test result : Severe Depression'
    return render_template("result.html", result=result, prediction=prediction[0])

app.secret_key = os.urandom(12)

app.run(port=5987, host='0.0.0.0', debug=True)