from fastapi import FastAPI

from users.router import router as router_users

app = FastAPI(title="Profile Service")

app.include_router(router_users)
