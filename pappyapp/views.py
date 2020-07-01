from flask import Flask, render_template, url_for, request

app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
@app.route('/index/')
def index():
	return render_template('index.html')

@app.route('/result/')
def result():
	return render_template('result.html')

if __name__ == "__main__":
    app.run()