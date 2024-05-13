from flask import Flask, redirect, render_template, request, url_for, session
import pyrebase
# from flask_restful import Api, Resource, reqparse
import requests
# from firebase_database import get_all_books
import json

app = Flask(__name__)


app = Flask(__name__)

config ={
    'apiKey': "AIzaSyBeBudg1x-NOf-0Xg2zwo80kcAXNae2MaU",
    'authDomain': "first-fun.firebaseapp.com",
    'databaseURL': "https://first-fun-default-rtdb.firebaseio.com",
    'projectId': "first-fun",
    'storageBucket': "first-fun.appspot.com",
    'messagingSenderId': "12087997751",
    'appId': "1:12087997751:web:579545a5555db9b323d6b2",
    'measurementId': "G-3M4VL123C0",
    'databaseURL':''
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app.secret_key = 'secret'

@staticmethod
@app.route("/")
def home():
    return render_template('firstPage.html')

@staticmethod
@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        password = request.form.get('password')
        email = request.form.get('email')
        try:
            user = auth.create_user_with_email_and_password(email, password)

            # Successful sign-up logic
            session['user_id'] = user.uid  # Store user ID in session (replace with actual ID)
            return render_template(url_for('index.html'))  # Redirect to protected page

        except Exception as e:
            error_message = str(e)  # Handle specific error messages based on exception type
            return render_template('signup.html', error=error_message)

    return render_template('signup.html')



@staticmethod
@app.route('/login', methods=["GET", "POST"])
def login():
  if ('user' in session):
    return  render_template('index.html')
  if request.method == 'POST':
    password = request.form.get('password')
    email = request.form.get('email')
    # print(email)
    # print(password)
    try:
      user = auth.sign_in_with_email_and_password(email, password)
    #   print(email)
    #   print(password)
    #   print(user)
      session['user'] = email
    except:
      return 'failed to login'
  return render_template('login.html')


# @app.route("/view_books")
# def view_books():
#   all_books = get_all_books()
  
#   return render_template('view_books.html', books=all_books)


url = "https://all-books-api.p.rapidapi.com/getBooks"

headers = {
	"X-RapidAPI-Key": "1264d06dc2msh26b3d8c204f6e08p178094jsn8ad523d59962",
	"X-RapidAPI-Host": "all-books-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

# for book in response.json():
#   print(book['bookIsbn'])

@app.route("/view_Titles")
def BookTitle():
  return render_template('bookTitle.html' , name=Titles) 
Titles = []
for book in response.json():
  Titles.append(book['bookTitle'])
  # print(book['bookTitle'])
print(Titles[1])


# for i in book['bookTitle']:
#   Titles.append(i)
# print (Titles)


@app.route("/view_books")
def view_books():
    books = response.json()

    if not books:
        assert "No books"
        # return render_template("error.html", message="No books found"), 404

    return render_template("bookstable.html", books=books)


@staticmethod
@app.route('/logout')
def logout():
  session.pop('user')
  return render_template('firstPage.html')

if __name__ == '__main__':
  app.run()


# # #api try
# import requests
# response = requests.get('https://randomuser.me/api/')
# print(response.status_code)
# print(response.json())

# gender = response.json()['results'][0]['gender']
# print(gender)
# first_name = response.json()['results'][0]['name']['first']
# print(first_name)
# pic = response.json()['results'][0]['picture']
# print(pic)

