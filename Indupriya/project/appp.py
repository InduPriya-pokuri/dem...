from flask import Flask,render_template,url_for

app=Flask(__name__)

@app.route('/')

def hello():
# 	return 'Welcome to Qis College'

# @app.route('/hello') # passing url
# def hello1():
# 	return '<url><i><h1 \
# 	style=color:red>welcome to \
# 	python workshop</h1></i></u>'

# @app.route('/name/<fname>/<lname>')
# def myname(fname,lname):
# 	return '<h2 style=color:yellow>My First Name is '\
# 	+fname+' <br>'' My Last Name is '\
# 	+lname+'</h2>'

# @app.route('/add/<int:num1>/<int:num2>')

# def addition(num1,num2):
# 	return '<h1 style=color:green>\
# 	Addition of %d + %d =%d'\
# 	%(num1,num2,num1+num2)+'</h1>'

# @app.route('/')
# def index():
# 	return render_template('index.html')

# @app.route('/details/<name>/<rollno>')
# def detail(name,rollno):
# 	return render_template('details.html',
# 		name=name,rollno=rollno)

# @app.route('/numbers/<int:start>/<int:end>')
# def numbers(start,end):
# 	return render_template('numbers.html',start=start,end=end)

 @app.route('/leap/<int:num1>/<int:num2>')
 def leapyear(num1,num2):
 	return render_template('leap.html',
 		num1=num1,num2=num2)

# @app.route('/table/<int:num1>/<int:num2>')
# def mul(num1,num2):
# 	return render_template('table.html',num1=num1,num2=num2)

@app.route('/register')
def register():
	return render_template('register.html')
# always last
	if __name__=="__main__":
	 # wsgi
		app.run(debug=True,
			host='localhost',
			port=5000)