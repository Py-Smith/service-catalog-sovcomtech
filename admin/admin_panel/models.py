from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
# TODO: Проверить ограничения и уникальность строк. Не должно быть дублирование записей для Система-сервис


class Service(models.Model):
    name = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=255, null=False)

    class Meta:
        verbose_name = "Справочник услуг"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.name


class SystemCategory(models.Model):
    name = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=255, null=False)

    class Meta:
        verbose_name = "Справочник категорий систем"
        verbose_name_plural = "Категории систем"

    def __str__(self):
        return self.name


class System(models.Model):
    name = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=255, null=False)
    category = models.ForeignKey(SystemCategory, on_delete=models.CASCADE, default=-1)

    class Meta:
        verbose_name = "Справочник систем"
        verbose_name_plural = "Системы"

    def __str__(self):
        return self.name


class SystemAlias(models.Model):
    alias = models.CharField(max_length=30, null=False)
    system = models.ManyToManyField('System')

    class Meta:
        verbose_name = "Справочник синонимов системы"
        verbose_name_plural = "Синонимы систем"

    def __str__(self):
        return self.alias


class SystemService(models.Model):
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    plan_time = models.DecimalField(decimal_places=2, max_digits=5, null=False,
                                    default=0, validators=[MinValueValidator(0),
                                                           MaxValueValidator(200)])
    start_support_time = models.DecimalField(decimal_places=2, max_digits=5, null=False,
                                             default=0, validators=[MinValueValidator(0),
                                                                    MaxValueValidator(24)])
    end_support_time = models.DecimalField(decimal_places=2, max_digits=5, null=False,
                                           default=24, validators=[MinValueValidator(0),
                                                                   MaxValueValidator(24)])
    timetable = models.ForeignKey('TimeTable', on_delete=models.CASCADE, default=1)
    supervizor = models.ForeignKey('PyrusUsers', on_delete=models.CASCADE, default=1)
    system_service_main_teams = models.ManyToManyField('SystemServiceMainTeams', blank=True)
    system_service_competence_teams = models.ManyToManyField('SystemServiceСompetenceTeams', blank=True)
    method_providing_service = models.ForeignKey('MethodProvidingService', on_delete=models.CASCADE, default=1)
    forms = models.ManyToManyField('PyrusForms', blank=True)

    class Meta:
        verbose_name = "Услуги для системы"
        verbose_name_plural = "Услуги для системы"

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

    class Meta:
        verbose_name = "Основные команды сопровождения для услуг"
        verbose_name_plural = "Основные команды сопровождения для услуг"

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

    class Meta:
        verbose_name = "Команды компетенций для услуг"
        verbose_name_plural = "Команды компетенций для услуг"

    def __str__(self):
        return f'{self.role_id} | {self.role_name} | {self.pyrus_stage}'


class PyrusForms(models.Model):
    form_id = models.IntegerField(null=False)
    form_name = models.CharField(max_length=30, null=False, default='-empty-')

    class Meta:
        verbose_name = "Справочник форм пайруса"
        verbose_name_plural = "Справочник форм пайруса"

    def __str__(self) -> str:
        return f'{self.form_id} | {self.form_name} '


class TimeTable(models.Model):
    name = models.CharField(max_length=255, null=False, default='-empty-')
    description = models.CharField(max_length=255, null=False, default='-empty-')

    class Meta:
        verbose_name = "Справочник календарей"
        verbose_name_plural = "Справочник календарей"

    def __str__(self) -> str:
        return f'{self.name} | {self.description}'


class TimeTableDate(models.Model):
    date = models.DateField(null=False)
    is_work = models.BooleanField(null=False)
    week = models.IntegerField(null=False)
    year = models.IntegerField(null=False)
    qr = models.IntegerField(null=False)
    month = models.IntegerField(null=True, blank=True)
    timetable = models.ForeignKey('TimeTable', on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Дни в календаре"
        verbose_name_plural = "Дни в календаре"

    def __str__(self) -> str:
        return f'{self.date}'


class PyrusUsers(models.Model):
    pyrus_id = models.IntegerField(blank=False, null=False)
    email = models.EmailField(max_length=255, null=False)
    username = models.CharField(max_length=255, null=False, default='-empty-')
    department = models.CharField(max_length=255, null=False, default='-empty-')
    management = models.CharField(max_length=255, null=False, default='-empty-')
    divizion = models.CharField(max_length=255, null=False, default='-empty-')

    class Meta:
        verbose_name = "Справочник менеджеров"
        verbose_name_plural = "Справочник менеджеров"

    def __str__(self) -> str:
        return f'{self.email} | {self.username}'


class MethodProvidingService(models.Model):
    name = models.CharField(max_length=255, null=False, blank=True)
    description = models.CharField(max_length=512, null=False, blank=True)

    class Meta:
        verbose_name = "Справочник способов предоставления услуги"
        verbose_name_plural = "Справочник способов предоставления услуги"

    def __str__(self) -> str:
        return f'{self.name} | {self.description}'
