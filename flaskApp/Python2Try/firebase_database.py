from firebase_admin import credentials, initialize_app, db, auth
import firebase_admin

# Initialize Firebase app
cred = credentials.Certificate('python/first-fun-firebase-adminsdk-kk62z-7f5618f2ba.json')
firebase_admin.initialize_app(cred)

# Get a reference to the database
ref = db.reference(url="https://first-fun-default-rtdb.firebaseio.com/")

def write_book_data(book_name, image_url, book_id):
  """Writes book data to the Firebase Realtime Database.

  Args:
    book_name: The name of the book.
    image_url: The URL of the book's image.
    book_id: The unique identifier of the book.
  """
  book_ref = ref.child(f"books/{book_id}")
  book_ref.set({
    "name": book_name,
    "image": image_url
  })

def write_user_data(user_name, image_url, user_password, mail, user_id):
  """Writes user data to the Firebase Realtime Database.

  Args:
    user_name: The name of the user.
    image_url: The URL of the user's image.
    password: The password of the user.
    email: The email of the user.
    user_id: The unique identifier of the user.
  """
  return auth.create_user(uid=user_id, display_name=user_name, email=mail, password=user_password, photo_url=image_url)

def get_book_data(id):
  """Gets book data from the Firebase Realtime Database.

  Args:
    id: The book id to retrieve data for.

  Returns:
    A dictionary containing the books's data, or None if not found.
  """
  book_ref = ref.child(f"books/{id}")
  data = book_ref.get()
  
  return data
  
def get_all_books():
  """Gets all book data from the Firebase Realtime Database.

  Returns:
    A list of dictionaries containing each book's data, or an empty list if none are found.
  """
  books_ref = ref.child("books")
  data: dict = books_ref.get() 

  if data is None:
    return []

  return data
