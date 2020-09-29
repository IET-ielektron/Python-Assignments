from django.db import models

#model that represent the table in postgress db
class employee_master(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    emp_name = models.CharField(max_length=200)

    class Meta:
        # model that represent the schema under which table is present
        db_table = u'"demo\".\"employee_master"'

class manager_master(models.Model):
    manager_id = models.IntegerField(primary_key=True)
    manager_name = models.CharField(max_length=200)

    class Meta:
        # model that represent the schema under which table is present
        db_table = u'"demo\".\"manager_master"'

class emp_mgr_rel_master(models.Model):
    emp_id = models.IntegerField()
    manager_id = models.IntegerField()

    class Meta:
        # model that represent the schema under which table is present
        db_table = u'"demo\".\"emp_mgr_rel_master"'
