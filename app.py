from flask import Flask,render_template,request
from model import movies

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")



@app.route('/result',methods=["GET","POST"])
def res():
    if request.method=="POST":
        mov = request.form["movie_name"]
        res=movies(mov)
        if res != 0:
            return render_template("result.html",ans=res)
        else:
            return render_template("result.html",ans=0,m=mov)
        


app.run(debug=True)