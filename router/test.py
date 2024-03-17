from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from database import database
from schemas import test

router = APIRouter(
    prefix="/test"
)

@router.get(
        "/",
        response_model=test.SampleSuccessResponse
    )
async def test(
    db: Session = Depends(database.get_db)
):
    return JSONResponse(
        content={
            "message": "Success",
            "data": "Hello World"
        },
        status_code=status.HTTP_200_OK
    )