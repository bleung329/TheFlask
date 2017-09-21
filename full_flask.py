'''
Brian Leung, Pd 7 SoftDev
'''
#Basic setup stuff here
from flask import Flask 
app = Flask(__name__)
#Just a basic landing page
@app.route("/")
def hello_there():
	return "<b>Welcome to the flask. Visit /texted, or literally anything you put in.</b>"
#Just another basic page, but involves /texted
@app.route("/texted")
def text_print():
	return "Oh no you just got texted, tell your friends about this page to totally text them"
#This returns whatever you typed in after /
@app.route("/<randomstuff>")
def vars(randomstuff):
	return 'Hey you put in: %s' % randomstuff
#This is just running the app.
if __name__=="__main__":
	app.debug = True
	app.run()