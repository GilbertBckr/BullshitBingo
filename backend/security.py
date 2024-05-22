import warnings
import uuid
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def mocked_user_token() -> str:
    warnings.warn("Using mocked tokens")
    return str(uuid.uuid4())

def get_hash(input: str) -> str:
    return pwd_context.hash(input)

def verify_hash(hashed_value: str, value: str) -> bool:
    return pwd_context.verify(value, hashed_value)
    