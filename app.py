from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

@app.route('/')
def function():
  return render_template('mainpage.html')


@app.route('/contact')
def contact():
  return render_template('contact.html')

@app.route('/weekend')
def weekend():
  return render_template('weekend.html')

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
