from fastapi import FastAPI
import routers.userRouter as userRouter

app = FastAPI(title="MyApp")
app.include_router(userRouter.router,tags=["User Controller"])
