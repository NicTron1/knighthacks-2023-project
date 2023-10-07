from pymongo.server_api import ServerApi
from pymongo import MongoClient

uri = "mongodb+srv://cluster0.4mp0egz.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
client = MongoClient(uri,
                     tls=True,
                     tlsCertificateKeyFile='./cert.pem',
                     server_api=ServerApi('1'))

db = client['Knighthacks']
collection = db['User Data']

def userData(email):
    return collection.find_one({"email":email})

def createUser(name, email, age, priority): 
    collection.insert_one({
        "name": name,
        "email": email,
        "age": age,
        "priority": priority
    })
    