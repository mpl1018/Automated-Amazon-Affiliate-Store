import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('./key.json')
default_app = firebase_admin.initialize_app(cred)
db = firestore.client()


imagen = 'holasoyimagen.jpg'
link = 'soylink.amz'
precio = '14€'
titulo = 'mititulo'

data = {
    u'imagen': imagen,
    u'link': link,
    u'precio': precio,
    u'titulo': titulo
}

# Add a new doc in collection 'cities' with ID 'LA'
db.collection(u'productos').document().set(data)