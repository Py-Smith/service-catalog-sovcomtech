# Generated by Django 4.2.3 on 2023-07-25 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0003_remove_timetabledate_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetabledate',
            name='month',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
