from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import relationship, backref, Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Contact(Base):
    __tablename__ = 'contacts'
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(150), unique=True, index=True)
    phone_number: Mapped[str] = mapped_column(String(150))
    birthday: Mapped[str] = mapped_column(String(150))
    other: Mapped[str] = mapped_column(String(250))

