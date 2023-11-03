import uuid
from fastapi import APIRouter
from helpers.passwordHelper import hash_password
from models.user import User, UserIn

router = APIRouter()

user_db: list[User] = [
    User(str(uuid.uuid4()), "Majd", "Alkayyal", "majd@gmail.com", "123456")
]

@router.get("/user")
async def GetAllUsers():
    return user_db


@router.get("/user/{userId}")
async def GetUserById(userId: str):
    return next((user for user in user_db if user.userId == userId), None)


@router.post("/user")
async def PostUser(user_in: UserIn):
    newUser = User()
    newUser.from_user_in(user_in)
    user_db.append(newUser)
    return "Done"


@router.put("/user/{userId}")
async def PutUser(userId: str, updatedUser: UserIn):
    user = next((user for user in user_db if user.userId == userId), None)
    if user:
        user.email = updatedUser.email
        user.firstname = updatedUser.firstname
        user.lastname = updatedUser.lastname
        user.password = hash_password(updatedUser.password)
    else:
        return "User not found"
    return "Done"


@router.delete("/user/{userId}")
async def DeleteUser(userId: str):
    global user_db 
    user_db = [user for user in user_db if user.userId != userId]
    return "Done"
