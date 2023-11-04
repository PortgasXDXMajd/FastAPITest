import uuid
from fastapi import APIRouter
from models.user import User, UserIn,UserOut
from database import get_database
from fastapi import HTTPException

router = APIRouter()


user_db: list[User] = [
    User(str(uuid.uuid4()), "Majd", "Alkayyal", "majd@gmail.com", "123456")
]

@router.get("/user")
async def GetAllUsers():
    try:
        db = get_database()

        # Attempt to find the user
        users = db["User"].find({})

        # If no user is found, return a 404 error
        if users is None:
            raise HTTPException(status_code=404, detail="User not found")


        return [UserOut(**document) async for document in users] # conver t to my model (BaseModel)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/user/{userId}")
async def GetUserById(userId: str):
    try:
        db = get_database()

        # Attempt to find the user
        user = await db["User"].find_one({"userId": userId},{'_id': False})

        # If no user is found, return a 404 error
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")


        return UserOut(**user) # conver t to my model (BaseModel)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/user")
async def PostUser(user_in: UserIn):  # Assuming you are taking a Pydantic model as input
    try:
        newUser = User()

        newUser.from_user_in(user_in)

        user_db.append(newUser)

        db = get_database()

        result = await db["User"].insert_one(newUser.to_dict())

        return {"id": str(result.inserted_id)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/user/{userId}")
async def PutUser(userId: str, updatedUser: UserIn):
    try:
        db = get_database()

        newUser = User()

        newUser.from_user_in(updatedUser)

        newUser.userId = userId

        await db["User"].find_one_and_replace({"userId": userId}, newUser.to_dict())

        return "Done"
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/user/{userId}")
async def DeleteUser(userId: str):
    try:
        db = get_database()

        # Attempt to find the user
        deletedUser = await db["User"].find_one_and_delete({"userId": userId})

        # If no user is found, return a 404 error
        if deletedUser is None:
            raise HTTPException(status_code=404, detail="User not found")


        return "Done" # conver t to my model (BaseModel)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
