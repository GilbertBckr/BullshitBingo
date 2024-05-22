from pydantic import BaseModel
from typing import Literal
import uuid


class Field(BaseModel):
    content: str
    checked: bool

class Player(BaseModel):
    name: str
    token_hash: str
    fields: list[list[Field]]
    has_bingo: bool

class CreateGame(BaseModel):
    private: bool = False
    dimensions: int = 3
    theme: str
    admin_token_hash: str
class Game(CreateGame):
    id: str = "thisIsId"
    boards: list[Player] = []
    game_state: Literal["DRAFT"] | Literal["RUNNING"] | Literal["ENDED"] = "DRAFT"
