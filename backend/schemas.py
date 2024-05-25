from pydantic import BaseModel
from typing import Literal


class Field(BaseModel):
    content: str
    checked: bool


class CreatePlayer(BaseModel):
    name: str
    user_id: str


class Player(CreatePlayer):
    fields: list[list[Field]] = []
    has_bingo: bool = False
    is_ready: bool = False


class CreateGame(BaseModel):
    private: bool = False
    dimensions: int = 3
    theme: str
    admin_id: str


class Game(CreateGame):
    id: str
    players: list[Player] = []
    game_state: Literal["DRAFT"] | Literal["RUNNING"] | Literal["ENDED"] = "DRAFT"


class ChangeCellCheckedPayload(BaseModel):
    row: int
    col: int
    new_checked: bool
    user_id: str
    game_id: str
