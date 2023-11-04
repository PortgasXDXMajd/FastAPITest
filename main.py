from fastapi import FastAPI
import routers.userRouter as userRouter
from database import get_database


app = FastAPI(title="MyApp")
app.include_router(userRouter.router,tags=["User Controller"])


@app.on_event("startup")
async def startup_db_client():
    app.db_client = get_database()

@app.on_event("shutdown")
async def shutdown_db_client():
    app.db_client.close()