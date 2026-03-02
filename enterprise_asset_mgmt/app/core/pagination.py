from typing import TypeVar, Generic, List
from pydantic import BaseModel, conint

T = TypeVar("T")

class Page(BaseModel, Generic[T]):
    items: List[T]
    total: int
    page: int
    size: int
    total_pages: int

def paginate(items: List[T], total: int, page: int, size: int) -> Page[T]:
    return Page(
        items=items,
        total=total,
        page=page,
        size=size,
        total_pages=(total + size - 1) // size
    )
