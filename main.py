#pip install Flask-Uploads

from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES
import sqlite3

run = "python main.py"
storage = "100M"



# Connect to the database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS login (userid TEXT PRIMARY KEY, password TEXT NOT NULL)')
cursor.execute('CREATE TABLE IF NOT EXISTS trash (submission_id INTEGER PRIMARY KEY, type TEXT NOT NULL, amount INTEGER NOT NULL, date DATE, userid TEXT, FOREIGN KEY (userid) REFERENCES login(userid))')
conn.commit()

app = Flask(__name__)

# This is to upload photos
import tensorflow as tf

model = tf.keras.models.load_model('path/to/your/model.h5')

def loginUser(username, password):
  return 1

  

@app.route("/login")
def renderLogin():
  return render_template("login.html")

app.secret_key = 'super secret key'
photos = UploadSet('photos', IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = 'static/img/uploaded'
configure_uploads(app, photos)

@app.route("/login/post", methods=["POST"])
def login():  # Login backend
  try:
    loginstatus = loginUser(request.form["username"], request.form["password"], User)
    return redirect("/")
  except:
    try:
      createUser(request.form["username"], request.form["password"], db, User)
      return redirect("/")
    except:
      return redirect("/login")



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)
