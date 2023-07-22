# Generated by Django 4.2.3 on 2023-07-22 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0008_alter_systemservice_system_service_competence_teams_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='systemservice',
            options={'verbose_name': 'Система-сервис', 'verbose_name_plural': 'Система-сервис'},
        ),
        migrations.AlterField(
            model_name='systemservice',
            name='system_service_competence_teams',
            field=models.ManyToManyField(blank=True, to='admin_panel.systemserviceсompetenceteams'),
        ),
        migrations.AlterField(
            model_name='systemservice',
            name='system_service_main_teams',
            field=models.ManyToManyField(blank=True, to='admin_panel.systemservicemainteams'),
        ),
        migrations.CreateModel(
            name='SystemServicePyrusForms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_id', models.IntegerField()),
                ('form_name', models.CharField(default='-empty-', max_length=30)),
                ('system_service', models.ManyToManyField(blank=True, to='admin_panel.systemservice')),
            ],
        ),
    ]
