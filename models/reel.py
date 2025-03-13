from pydantic import BaseModel


class Reel(BaseModel):
    title: str
    thumbnail: str
    link: str
