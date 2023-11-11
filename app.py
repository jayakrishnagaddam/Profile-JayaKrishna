from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def function():
  return render_template('mainpage.html')


if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)
