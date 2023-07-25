from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name


class System(models.Model):
    name = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=255, null=False)
    service = models.ManyToManyField('Service')

    def __str__(self):
        return self.name
    
class SystemAlias(models.Model):
    alias = models.CharField(max_length=30, null=False)
    system = models.ManyToManyField('System')

    def __str__(self):
        return self.alias
    
class SystemService(models.Model):
    system = models.ForeignKey(System, on_delete = models.CASCADE)
    service = models.ForeignKey(Service, on_delete = models.CASCADE)
    plan_time = models.DecimalField(decimal_places=2, max_digits=5, null=False,
                                    default=0, validators=[MinValueValidator(0),
                                                           MaxValueValidator(200)])
    start_support_time = models.DecimalField(decimal_places=2, max_digits=5, null=False,
                                    default=0, validators=[MinValueValidator(0),
                                                           MaxValueValidator(24)])
    end_support_time = models.DecimalField(decimal_places=2, max_digits=5, null=False,
                                    default=24, validators=[MinValueValidator(0),
                                                           MaxValueValidator(24)])
    timetable = models.ForeignKey('TimeTable', on_delete = models.CASCADE, default=1)
    # TODO: Add supervizor_id releationships for table Users
    system_service_main_teams = models.ManyToManyField('SystemServiceMainTeams',  blank=True)
    system_service_competence_teams = models.ManyToManyField('SystemServiceСompetenceTeams',  blank=True)

    class Meta:
        verbose_name = "Система-сервис"
        verbose_name_plural = "Система-сервис"
    
    
    def __str__(self):
        return f'Service: {self.system}-{self.service} '

class SystemServiceMainTeams(models.Model):
    role_id = models.IntegerField(blank=False, null=False)
    role_name = models.CharField(max_length=30, null=False, default='no name')
    plan_time = models.DecimalField(decimal_places=2, max_digits=5, null=False,
                                    default=0, validators=[MinValueValidator(0),
                                                           MaxValueValidator(200)])
    pyrus_stage = models.IntegerField(null=False)
    start_support_time = models.DecimalField(decimal_places=2, max_digits=5, null=False,
                                    default=0, validators=[MinValueValidator(0),
                                                           MaxValueValidator(24)])
    end_support_time = models.DecimalField(decimal_places=2, max_digits=5, null=False,
                                    default=24, validators=[MinValueValidator(0),
                                                           MaxValueValidator(24)])
    

    def __str__(self):
        return f'{self.role_id} | {self.role_name} | {self.pyrus_stage}'
    

class SystemServiceСompetenceTeams(models.Model):
    role_id = models.IntegerField(blank=False, null=False)
    role_name = models.CharField(max_length=30, null=False, default='no name')
    plan_time = models.DecimalField(decimal_places=2, max_digits=5, null=False,
                                    default=0, validators=[MinValueValidator(0),
                                                           MaxValueValidator(200)])
    pyrus_stage = models.IntegerField(null=False)
    start_support_time = models.DecimalField(decimal_places=2, max_digits=5, null=False,
                                    default=0, validators=[MinValueValidator(0),
                                                           MaxValueValidator(24)])
    end_support_time = models.DecimalField(decimal_places=2, max_digits=5, null=False,
                                    default=24, validators=[MinValueValidator(0),
                                                           MaxValueValidator(24)])
    

    def __str__(self):
        return f'{self.role_id} | {self.role_name} | {self.pyrus_stage}'

class PyrusForms(models.Model):  
    form_id = models.IntegerField(null=False)
    form_name = models.CharField(max_length=30, null=False, default='-empty-')

    def __str__(self) -> str:
        return f'{self.form_id} | {self.form_name} '

class SystemServicePyrusForms(models.Model):
    form = models.ForeignKey(PyrusForms, on_delete = models.CASCADE, blank=True, null=True)
    system_service = models.ManyToManyField('SystemService',  blank=True)

    def __str__(self) -> str:
        return f'{self.form} | {self.system_service}'

class TimeTable(models.Model):
    name = models.CharField(max_length=255, null=False, default='-empty-')
    description = models.CharField(max_length=255, null=False, default='-empty-')

    def __str__(self) -> str:
        return f'{self.name} | {self.description}'

class TimeTableDate(models.Model):
    date = models.DateField(null=False)
    is_work = models.BooleanField(null=False)
    week = models.IntegerField(null=False)
    year = models.IntegerField(null=False)
    qr = models.IntegerField(null=False)
    month = models.IntegerField(null=True, blank=True)
    timetable = models.ForeignKey('TimeTable', on_delete = models.CASCADE, null=True)

    def __str__(self) -> str:
        return f'{self.date}'