from labtrak.models import Base
from labtrak.utils import get_hash, verify_hash, timestamp

class User(Base):

    collection = Base.db.users

    @classmethod
    def create(cls, username, email, password, firstname, lastname):
        return cls.collection.insert({
            'username': username, # pilot number
            'email': email,
            'password': get_hash(password),
            'firstname': firstname,
            'lastname': lastname,
            'last_auth': timestamp()
        })

    @classmethod
    def auth(cls, username, password):
        user = cls.collection.find_one( {'username':username} )
        if user and verify_hash(password, user['password']):
            cls.collection.update(
                {'_id': user['_id']},
                {'$set': {'last_auth': timestamp()} }
            )
            return user
