from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import text, ForeignKey, BigInteger

from datetime import datetime
from infrastructure.db.base import Base
from infrastructure.db.models.orm_template_columns import intpk, created_at, updated_at


class UserOrm(Base):
    __tablename__ = 'users'

    user_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[str]
    mailing_time: Mapped[str]
    language: Mapped[str]
    canteen_id: Mapped[int]
    updated_at: Mapped[updated_at]
    created_at: Mapped[created_at]
    status: Mapped[str] = mapped_column(default="active")
