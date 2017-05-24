from flask import Flask,render_template
from flask_mysqldb import MySQL


app = Flask(__name__)

#@app.route("/")
#@app.route("/profile/<name>")
#@app.route("/<user>")

#def index(user=None):
#    return render_template("user.html", user=user)
#def profile(name):
 #   return render_template("profile.html",name=name)

@app.route('/example.php')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])



if __name__ == '__main__':
    app.run()
