# Generated by Django 5.0.4 on 2024-05-02 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MafetengDoctorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'doctors',
            },
        ),
    ]
