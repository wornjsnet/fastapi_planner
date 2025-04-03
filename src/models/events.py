from pydantic import BaseModel, ConfigDict

class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: list[str]
    location: str
    created_at: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": 1,
                "title": "제목",
                "image": "path/to",
                "description": "설명",
                "tags": ["#태그", "#tag"],
                "location": "제1실습관 207호"
            }
        }
    )