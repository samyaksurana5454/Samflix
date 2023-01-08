from application import app ,db
from flask import render_template , request, json , Response
from application.models import User

moviesData =[{"Title":"1","Movies":"Big Buck Bunny","Rating":3,"Genre":"shorts"}, 
{"Title":"2","Movies":"Cloning a project into netbeans","Rating":4,"Genre":"cassandra"}, 
{"Title":"3","Movies":"Installing and starting cassandra on a mac","Rating":3,"Genre":"cassandra"}, 
{"Title":"4","Movies":"Running cassandra on a pc","Rating":3,"Genre":"cassandra"}, 
{"Title":"5","Movies":"Starting Erlang","Rating":4,"Genre":"erlang"}]

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html" , index=True )

@app.route("/login")
def login():
    return render_template("login.html" , login=True)


@app.route("/movies")
def movies():
    classes= User.objects.all()

    return render_template("movies.html",moviesData=classes , movies=True)

@app.route("/register")
def register():
    return render_template("register.html" , register= True)

@app.route("/watch_movies", methods=["GET","POST"])
def watch_movies():
    Title=request.form.get('Title')
    Movies=request.form.get('Movies')
    Genre=request.form.get('Genre')
    return render_template("watch_movies.html" , watch_movies=True, data={"Title":Title, "Movies":Movies, "Genre":Genre })


@app.route("/api/")
@app.route("/api/<idx>")
def api(idx=None):
    if(idx==None):
        jdata= moviesData
    else:
            jdata=moviesData[int(idx)]

    return Response(json.dumps(jdata), mimetype= "application/json")

class User(db.Document):
    Title    =   db.IntField( unique=True )
    Movies  =   db.StringField( max_length=50 )
    Rating   =   db.StringField( max_length=50 )
    Genre     =   db.StringField( max_length=30 )
    

@app.route("/user")
def user():
     User(Title=1, Movies="Big Buck Bunny", Rating="3", Genre="shorts").save()
     User(Title=2, Movies="Cloning a project into netbeans", Rating="4", Genre="cassandra").save()
     User(Title=3, Movies="Installing and starting cassandra on a mac", Rating="3", Genre="cassandra").save()
     User(Title=4, Movies="Running cassandra on a pc", Rating="3", Genre="cassandra").save()
     User(Title=5, Movies="	Starting Erlang", Rating="4", Genre="erlang").save()
     users = User.objects.all()
     return render_template("user.html", users=users)