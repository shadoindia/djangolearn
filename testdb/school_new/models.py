from django.db import models

# Create your models here.
class Personnew(models.Model):
    personid = models.AutoField(db_column='PersonID', primary_key=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50)  # Field name made lowercase.
    hiredate = models.DateTimeField(db_column='HireDate', blank=True, null=True)  # Field name made lowercase.
    enrollmentdate = models.DateTimeField(db_column='EnrollmentDate', blank=True, null=True)  # Field name made lowercase.
    discriminator = models.CharField(db_column='Discriminator', max_length=50)  # Field name made lowercase.

    class Meta:
        db_table = 'Personnew'