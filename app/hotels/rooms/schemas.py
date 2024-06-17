from typing import List, Optional

from pydantic import BaseModel


class SRoom(BaseModel):
    """Модель отображения комнаты."""

    id: int
    hotel_id: int
    name: str
    description: Optional[str]
    services: List[str]
    price: int
    quantity: int
    image_id: int

    class Config:
        orm_mode = True


class SRoomInfo(SRoom):
    """Модель отображения информации о комнате."""
    total_cost: int
    rooms_left: int

    class Config:
        orm_mode = True
