# app.py
from VertexAI import get_search_results, get_itinerary
from flask import Flask, render_template, request, render_template_string, redirect, url_for
from flask import session, g
import firebase_admin
from firebase_admin import credentials, firestore
import bcrypt
import os
app = Flask(__name__)
app.secret_key=os.urandom(24)

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/')
def landing_page():
    if g.user:
        return render_template("/landing_page.html")
    else:
        return redirect("/login")

@app.route('/search', methods=['POST'])
def search_destinations():
    keyword = request.form['search_keyword']
    search_results = get_search_results(keyword)
    return render_template('landing_page.html', search_results=search_results)

@app.route('/itinerary', methods=['POST'])
def itinerary():
    keyword = request.form['search_results']
    days = request.form['days']
    itinerary = get_itinerary("I want to travel " + keyword + "for " + str(days) + " days.")
    return render_template('itinerary.html', itinerary=itinerary, it=itinerary)

@app.route('/dashboard', methods=['GET'])
def dashboard():
    if g.user:
        data = db.collection('users').document(g.user)
        if data.get().exists:
            data = data.get().to_dict()
            return render_template('dashboard.html', itineries=data['itineries'])
    return redirect("/login")
@app.route('/save_itinerary', methods=['POST'])
def save_itinerary():
    if g.user:
        itinerary = request.form['itinerary']
        print(itinerary)
        data = db.collection('users').document(g.user)
        if data.get().exists:
            data = data.get().to_dict()
            data['itineries'].append(itinerary)
            db.collection('users').document(g.user).set(data)
            return redirect("/")
    return redirect("/login")
        
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        result = request.form
        username = result['username']
        name = result["name"]
        email = result["email"]
        password = result["password"].encode('utf-8')
        hashed = bcrypt.hashpw(password, bcrypt.gensalt(8))
        data = db.collection('users').document(username)
        if not data.get().exists:
            data.set({'name':name, 'Email':email, 'hashed_password':hashed, 'itineries':[]})
            return redirect('/login')
        else:
            return render_template_string("user already exists. please sign in")
    return render_template('signup.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        result = request.form
        username = result['username']
        password = result['password']
        data = db.collection('users').document(username)
        if data.get().exists:
            data = data.get().to_dict()
            if bcrypt.checkpw(password.encode('utf-8'), data['hashed_password']):
                session['user'] = username
                return redirect("/dashboard")
            else:
                return render_template_string("Wrong password")
        else:   
            return "User does not exist"
    return render_template('login.html')
@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect('/login')

@app.before_request
def before_request():
    g.user  = None
    if 'user' in session:
        g.user = session['user']

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8000,debug=True)
