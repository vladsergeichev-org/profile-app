from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from operations.models import operation
from operations.schemas import GetOperation, CreateOperation

router = APIRouter(
    prefix="/operation",
    tags=["Users"]
)


@router.post("/get_operations")
async def get_operations(user_data: GetOperation, session: AsyncSession = Depends(get_async_session)):
    query = select(operation).where(operation.c.user_id == user_data.uid)
    print(query)
    result = await session.execute(query)
    return [r._mapping for r in result.all()]


@router.post("/create")
async def create_operation(operation_data: CreateOperation, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(operation).values(**operation_data.dict())
    print(stmt)
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
