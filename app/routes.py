# need to transfer all apps into this one app
from app import app
from flask import redirect, render_template, url_for


@app.route('/index.html')
def home():
	return render_template('homepage.html', title_bar ='Circuit Syndicate Racing')

@app.route('/product.html')
def product():
	return render_template('product.html', title_bar ='Circuit Syndicate Racing')

@app.route('/about.html')
def about():
	return render_template('about.html', title_bar ='Circuit Syndicate Racing')
