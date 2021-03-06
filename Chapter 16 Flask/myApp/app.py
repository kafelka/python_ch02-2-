from flask import Flask, render_template, request
app = Flask(__name__)

#@app.route("/")
#def hello():
#    return "<h1>Hello world2!</h1><p>test1<span style='color:blue';>blablabla</span></p><p>test2</p>"

#@app.route("/contactus")
#def firstPar():
#    return "<p>phone email address</p>"

#nie dziala ponizsze
@app.route("/greeting/<greeting>")
def randomGreeting(greeting):
    return render_template("hello.html", greeting = greeting)

#@app.route("/")
#def hello_someone():
#    return render_template("index.html")

@app.route("/")
def begin():
    return render_template("hello.html", greeting = "hello")

@app.route("/confirmation", methods=["POST"])
def confirmation():
    form_data = request.form
    email = form_data["email"]
    result="All OK"
    return render_template("confirmation.html", title="Form confirmation", **locals())

@app.route("/<name>")
def hello_someone(name):
    return render_template("hello.html", greeting = "hello", name=name.title())

#Create Heroku account, install postgres via pip
#go to the right directory / folder
#heroku login
#heroku create
#git push heroku master
#heroku ps:scale web=1
#heroku open
#in case of issues: heroku logs --tail


#playing with css but not a good idea
#@route("path/to/sheet.css")

if __name__ == '__main__':
    app.run(debug=True) 
