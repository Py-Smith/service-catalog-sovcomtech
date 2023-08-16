from sqlalchemy import Column, Float, ForeignKey, Integer, String

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


class Service(Base):
    __tablename__ = "admin_panel_service"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)


class Timetable(Base):
    __tablename__ = "admin_panel_timetable"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)


class PyrusUsers(Base):
    __tablename__ = "admin_panel_pyrususers"

    id = Column(Integer, primary_key=True, index=True)
    pyrus_id = Column(Integer)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    department = Column(String)
    management = Column(String)
    divizion = Column(String)


class SystemService(Base):
    __tablename__ = "admin_panel_systemservice"

    id = Column(Integer, primary_key=True, index=True)
    plan_time = Column(Float)
    start_support_time = Column(Float)
    end_support_time = Column(Float)
    service_id = Column(Integer, ForeignKey('Service.id'))
    system_id = Column(Integer, ForeignKey('System.id'))
    timetable_id = Column(Integer, ForeignKey('Timetable.id'))
    supervizor_id = Column(Integer, ForeignKey('PyrusUsers.id'))
