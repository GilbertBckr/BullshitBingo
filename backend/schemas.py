from pydantic import BaseModel
from typing import Literal


class Field(BaseModel):
    content: str
    checked: bool

class CreatePlayer(BaseModel):
    name: str
    token_hash: str


class Player(CreatePlayer):
    fields: list[list[Field]]
    has_bingo: bool

class CreateGame(BaseModel):
    private: bool = False
    dimensions: int = 3
    theme: str
    admin_token_hash: str

class Game(CreateGame):
    id: str = "thisIsId"
    players: list[Player] = []
    game_state: Literal["DRAFT"] | Literal["RUNNING"] | Literal["ENDED"] = "DRAFT"

"""{"theme": "Röthig", "admin_token_hash": "asdfa"}"""