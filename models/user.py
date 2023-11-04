import uuid
from pydantic import BaseModel
from helpers.passwordHelper import hash_password


class UserIn(BaseModel):
    firstname: str
    lastname: str
    email: str
    password: str

class User:
    userId: str
    firstname: str
    lastname: str
    email: str
    password: str

    def __init__(self, userId = None, fn= None, ln= None, email= None, password= None):
        if userId:
            self.userId = userId
        if fn:
            self.firstname = fn
        if ln:
            self.lastname = ln
        if email:
            self.email = email
        if password:
            self.password = password
        pass

    def from_user_in(self, user_in: UserIn):
        self.userId = str(uuid.uuid4())
        self.firstname = user_in.firstname
        self.lastname = user_in.lastname
        self.email = user_in.email
        self.password = hash_password(user_in.password)
    
    def to_dict(self):
        return {
            "userId": self.userId,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "email": self.email,
            "password": self.password,
        }

class UserOut(BaseModel):
    userId: str
    firstname: str
    lastname: str
    email: str

    @classmethod
    def from_user(cls, user: User):
        return cls(
            userId=user.userId,
            firstname=user.firstname,
            lastname=user.lastname,
            email=user.age,
        )
