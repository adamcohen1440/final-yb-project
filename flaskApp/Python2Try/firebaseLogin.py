import pyrebase
# Import database module.
from firebase_admin import db

# Get a database reference to our blog.
ref = db.reference(url="https://first-fun-default-rtdb.firebaseio.com/")

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

# email = 'test@gmail.com'
# password = '123456'

#user = auth.create_user_with_email_and_password(email, password)
#print(user)

# user = auth.sign_in_with_email_and_password(email, password)

# #info = auth.get_account_info(user['id_token'])
# #print(info)

# #auth.send_email_verification(user['id_token'])

# auth.send_password_reset_email(email)