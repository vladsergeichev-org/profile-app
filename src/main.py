from fastapi import FastAPI

from users.router import router as router_users
from operations.router import router as router_operations

app = FastAPI(title="ClientProfile Service")

app.include_router(router_users)
app.include_router(router_operations)
