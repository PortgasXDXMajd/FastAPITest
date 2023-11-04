from models.user import User, UserIn,UserOut
from services.database import get_database
from helpers.response_model import ResponseModel



class UserService:
    db = None
    
    def __init__(self):
        self.db = get_database()
        pass

    async def GetAllUsers(self):
        if self.db is not None:
            users = self.db["User"].find({})

            if users is None:
                 return ResponseModel(msg='User was not found',res=404)

            return ResponseModel(body=[UserOut(**document) async for document in users])
        else:
             return ResponseModel(msg='Db is not init',res=500)
        
    async def GetUserById(self, userId: str):
        user = await self.db["User"].find_one({"userId": userId},{'_id': False})

        if user is None:
            return ResponseModel(msg='User was not found',res=404)

        return ResponseModel(body=UserOut(**user))
    

    async def CreateANewUser(self,user_in: UserIn):
        newUser = User()
        newUser.from_user_in(user_in)
        result =  await self.db["User"].insert_one(newUser.to_dict())
        return ResponseModel(body={"id": str(result.inserted_id)})
    
    async def UpdateUser(self,userId: str, updatedUser: UserIn):
        user = User()

        user.from_user_in(updatedUser)

        user.userId = userId

        await self.db["User"].find_one_and_replace({"userId": userId}, user.to_dict())

        return ResponseModel()
    
    async def DeleteUser(self, userId: str):

        deletedUser = await self.db["User"].find_one_and_delete({"userId": userId})

        if deletedUser is None:
            return ResponseModel(msg='User was not found',res=404)
        
        return ResponseModel()