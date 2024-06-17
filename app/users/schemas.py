from pydantic import BaseModel, EmailStr


class SUserAuth(BaseModel):
    """Модель регистрации и аутентификации пользователя."""

    email: EmailStr
    password: str