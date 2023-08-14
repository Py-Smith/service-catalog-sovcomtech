from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, backref

from db.postgres import Base

 
class SystemCategory(Base):
    __tablename__ = "admin_panel_systemcategory"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)


class System(Base):
    __tablename__ = "admin_panel_system"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    category_id = Column(Integer, ForeignKey('SystemCategory.id'))