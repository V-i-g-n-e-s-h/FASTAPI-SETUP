from pydantic import BaseModel


class SampleSuccessResponse(BaseModel):
    message: str
    data: str

    class Config:
        json_schema_extra = {
            'example': {
                "message": "Success",
                "data" : "Hello World"
            }
        }