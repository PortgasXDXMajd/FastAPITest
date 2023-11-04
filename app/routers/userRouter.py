from fastapi import APIRouter,HTTPException
from app.models.user import UserIn
from app.services.user_service import UserService


router = APIRouter()


@router.get("/user")
async def GetAllUsers():
    try:
        return await UserService().GetAllUsers()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/user/{userId}")
async def GetUserById(userId: str):
    try:
        return await UserService().GetUserById(userId=userId)
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/user")
async def PostUser(user_in: UserIn):  # Assuming you are taking a Pydantic model as input
    try:
        return await UserService().CreateANewUser(user_in=user_in)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/user/{userId}")
async def PutUser(userId: str, updatedUser: UserIn):
    try:
        return await UserService().UpdateUser(userId=userId,updatedUser=updatedUser)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/user/{userId}")
async def DeleteUser(userId: str):
    try:
        return await UserService().DeleteUser(userId=userId)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
