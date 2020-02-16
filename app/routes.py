# need to transfer all apps into this one app
from app import app
from flask import redirect, render_template, url_for


@app.route('/index.html')
def home():
	return render_template('site_homepage.html', title_bar ='Circuit Syndicate')

@app.route('/product.html')
def product():
	return render_template('site_product.html', title_bar ='Circuit Syndicate')
