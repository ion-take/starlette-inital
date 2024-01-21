from __future__ import annotations

import asyncio
import datetime
from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy import select

from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import DateTime

from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import selectinload


class Base(AsyncAttrs, DeclarativeBase):
    """
    Base class for all Model
    """
    pass

 

#  define your models here ...

class User(Base):
    __tablename__ = 'table_name'
    _id:  Mapped[int] = mapped_column(Integer, primary_key=True)
   
    def __repr(self):
        # always return a string 
        return 'return a sting'