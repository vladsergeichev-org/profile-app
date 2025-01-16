from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from users.security import PasswordHelper
from users.models import user
from users.schemas import UserSearch, UserCreate, UserLogin

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)


@router.post("/search")
async def get_user(user_data: UserSearch, session: AsyncSession = Depends(get_async_session)):
    query = select(user).where(user.c[user_data.type.value] == user_data.value)
    result = await session.execute(query)
    row = result.one_or_none()
    return {
        "id": row[0],
        "name": row[1],
        "surname": row[2],
        "username": row[3],
        "registered_at": row[6],
        "email": row[7],
    }
    # return [r._mapping for r in result.all()]


@router.get("/all")
async def get_all_users(session: AsyncSession = Depends(get_async_session)):
    query = select(user)
    result = await session.execute(query)
    return [{
        "id": r[0],
        "name": r[1],
        "surname": r[2],
        "username": r[3],
        "registered_at": r[6],
        "email": r[7],
    } for r in result.all()]
    # return [r._mapping for r in result.all()]


@router.post("/create")
async def create_user(user_data: UserCreate, session: AsyncSession = Depends(get_async_session)):
    pwd_helper = PasswordHelper()
    data = user_data.dict()
    secrets = pwd_helper.create(data.pop("password"))
    print(secrets[0], secrets[1])
    stmt = insert(user).values(**data, hashed_password=secrets[0], salt=secrets[1])
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}


@router.post("/login")
async def login_user(user_data: UserLogin, session: AsyncSession = Depends(get_async_session)):
    query = select(user).column(user.c.hashed_password).where(user.c.username == user_data.username)
    result = await session.execute(query)
    row = result.one_or_none()
    pwd_helper = PasswordHelper(row[4], row[5])
    return {"status": "success", "password_verify": pwd_helper.verify(user_data.password)}
