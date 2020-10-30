# Generated by Django 3.1.2 on 2020-10-29 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=100, verbose_name='Employee Name')),
                ('manager_id', models.CharField(max_length=100, verbose_name='Manager Name')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employee',
            },
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
        migrations.DeleteModel(
            name='Manager',
        ),
    ]
