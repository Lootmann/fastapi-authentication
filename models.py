from pydantic import BaseModel, Field

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str = Field(...)
    email: str = Field("testmail@email.com", title="your email")
    full_name: str = Field("HogeTaro", title="your fullname")
    disabled: bool = False


class UserCreate(User):
    password: str = Field(...)


class UserInDB(User):
    hashed_password: str
