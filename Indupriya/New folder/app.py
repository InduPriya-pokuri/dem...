app=Flask(__name__)# instance

@app.route('/hello/<name>')
def home2(name):




# @app.route('/add/<num1>/<num2>')
# def add (num1,num2):
# 	return '<h1> Addition of' ,num1,'+'


@app.route('/')
def home(): 
	return '<i><b><h1 style=color: #FF45F7 >Welcome to\
QIS college</h1>'

@app.route('/name/<fname>/<lname>')
def names(fname,lname):
	return "<h2 style=color:blue> My name is" +fname +\
	        '<br> Mylast name is' +lname+ "</h2>"

@app.route('/add/<int:num1>/<int:num2>')
def addition(num1,num2):
	return"<h1 style=color:pink> addition of %d + %d is %d  "%(num1,num2,num1+num2)+'</h1>'


# print range of numbers







# always last

if __name__=="__main__":
	app.run(debug=True,
		host="Localhost",
		port=5000) 


