# Generated by Django 3.1.2 on 2020-10-03 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('manager_id', models.AutoField(primary_key=True, serialize=False)),
                ('manager_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.AutoField(primary_key=True, serialize=False)),
                ('emp_name', models.CharField(max_length=50)),
                ('manager_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp_mgr_rel.manager')),
            ],
        ),
    ]