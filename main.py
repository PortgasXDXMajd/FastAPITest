from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import app.routers.userRouter as userRouter


app = FastAPI(title="MyApp")
app.include_router(userRouter.router,tags=["User Endpoints"])


@app.get("/")
def GetHomePage():
    return HTMLResponse("<h1>Test API</h1")