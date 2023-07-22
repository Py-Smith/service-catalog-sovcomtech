# Generated by Django 4.2.3 on 2023-07-22 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0009_alter_systemservice_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PyrusForms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_id', models.IntegerField()),
                ('form_name', models.CharField(default='-empty-', max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='systemservicepyrusforms',
            name='form_id',
        ),
        migrations.RemoveField(
            model_name='systemservicepyrusforms',
            name='form_name',
        ),
        migrations.AddField(
            model_name='systemservicepyrusforms',
            name='form',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_panel.pyrusforms'),
        ),
    ]
