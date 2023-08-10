# Generated by Django 4.2.3 on 2023-08-10 12:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0006_systemservice_timetable_timetabledate_month'),
    ]

    operations = [
        migrations.CreateModel(
            name='PyrusUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pyrus_id', models.IntegerField()),
                ('email', models.EmailField(max_length=255)),
                ('username', models.CharField(default='-empty-', max_length=255)),
                ('department', models.CharField(default='-empty-', max_length=255)),
                ('management', models.CharField(default='-empty-', max_length=255)),
                ('divizion', models.CharField(default='-empty-', max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='systemservice',
            name='supervizor_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='admin_panel.pyrususers'),
        ),
    ]
