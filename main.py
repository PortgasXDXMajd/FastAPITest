from fastapi import FastAPI
import app.routers.userRouter as userRouter


app = FastAPI(title="MyApp")
app.include_router(userRouter.router,tags=["User Endpoints"])