from flask import Flask, render_template, request, redirect, url_for, flash
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRET_KEY"] = "1234"  # Add a secret key for flash messages
app.config["MONGO_URI"] = "mongodb://localhost:27017/profile"
mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
def function():
    if request.method == 'POST':
        user_data = {
            'name': request.form.get('fullname'),
        }

        mongo.db.users.insert_one(user_data)

    return render_template('mainpage.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
