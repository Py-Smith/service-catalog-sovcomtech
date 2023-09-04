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
    method_providing_service_id = Column(Integer, ForeignKey('MethodProvidingService.id'))


class SystemServiceMainTeams(Base):
    __tablename__ = "admin_panel_systemservice_system_service_main_teams"

    id = Column(Integer, primary_key=True, index=True)
    systemservice_id = Column(Integer, ForeignKey('SystemService.id'))
    systemservicemainteams_id = Column(Integer, ForeignKey('MainTeams.id'))


class MainTeams(Base):
    __tablename__ = "admin_panel_systemservicemainteams"

    id = Column(Integer, primary_key=True, index=True)
    role_id = Column(Integer)
    role_name = Column(String)
    plan_time = Column(Float)
    pyrus_stage = Column(Integer)
    start_support_time = Column(Float)
    end_support_time = Column(Float)


class SystemServiceCompetenceTeams(Base):
    __tablename__ = "admin_panel_systemservice_system_service_competence_teams"

    id = Column(Integer, primary_key=True, index=True)
    systemservice_id = Column(Integer, ForeignKey('SystemService.id'))
    systemserviceсompetenceteams_id = Column(Integer, ForeignKey('CompetenceTeams.id'))


class CompetenceTeams(Base):
    __tablename__ = "admin_panel_systemserviceсompetenceteams"

    id = Column(Integer, primary_key=True, index=True)
    role_id = Column(Integer)
    role_name = Column(String)
    plan_time = Column(Float)
    pyrus_stage = Column(Integer)
    start_support_time = Column(Float)
    end_support_time = Column(Float)


class MethodProvidingService(Base):
    __tablename__ = "admin_panel_methodprovidingservice"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)


class PyrusForms(Base):
    __tablename__ = 'admin_panel_pyrusforms'

    id = Column(Integer, primary_key=True, index=True)
    form_id = Column(Integer)
    form_name = Column(String)


class SystemServiceForms(Base):
    __tablename__ = 'admin_panel_systemservice_forms'

    id = Column(Integer, primary_key=True, index=True)
    systemservice_id = Column(Integer, ForeignKey('SystemService.id'))
    pyrusforms_id = Column(Integer, ForeignKey('PyrusForms.id'))
