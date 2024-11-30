from pydantic import BaseModel


class LinkDto(BaseModel):
    url: str