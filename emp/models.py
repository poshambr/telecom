from django.db import models

# Create your models here.
from django.db import models
#from django.db import models

# Create your models here.
from django.db import models
import datetime
from django.core.validators import RegexValidator,FileExtensionValidator
from django.core.exceptions import ValidationError
from django.core.files.storage import FileSystemStorage


fs = FileSystemStorage(location='media/images')


Validators = {
             'DeptNo': RegexValidator(r'^[0-9]{1,6}$', 'Only Numbers and Upper are allowed (max. 6)'),
             'Desig_No': RegexValidator(r'^[0-9]{1,6}$', 'Only Numbers and Upper are allowed (max. 6)'),
             'Emp_No': RegexValidator(r'^[0-9]{1,10}$', 'Only Numbers and Upper are allowed (max. 6)'),
             'Intercom_No': RegexValidator(r'^[0-9]{1,4}$', 'Only Numbers and Upper are allowed (max. 6)'),
             'Cug_No': RegexValidator(r'^[0-9]{1,10}$', 'Only Numbers and Upper are allowed (max. 6)'),
             'Phone_No': RegexValidator(r'^[0-9]{1,12}$', 'Only Numbers and Upper are allowed (max. 6)'),
             'Plan_No': RegexValidator(r'^[0-9]{1,5}$', 'Only Numbers and Upper are allowed (max. 6)'),
             'Quarter_No': RegexValidator(r'^[0-9]{1,10}$', 'Only Numbers and Upper are allowed (max. 6)'),
             'RollNumber': RegexValidator(r'^[0-9A-Z]{6,8}$', 'Only Numbers and Upper Case Alphabets are allowed (max. 10)'),
             'FullName': RegexValidator(r'^[a-zA-Z\' ]{1,50}$', 'Only Alphabets, Spaces and \' are allowed (max. 50)'),
             'MobileNumber': RegexValidator(r'^[0-9+]{10,15}$', 'Only digits and + are allowed'),
             'Nationality': RegexValidator(r'^[a-zA-Z]{1,30}$', 'Only Alphabets are allowed (max. 30)'),
             'Photograph': FileExtensionValidator(['jpg', 'png'], 'Only JPG and PNG files are allowed'),
             # 'DateOfBirth': _DOBValidator,
             'SBIAccountNumber': RegexValidator(r'^[0-9]{11}$', 'SBI Account Number should have 11 digits'),
             'AadharCardNumber': RegexValidator(r'^[0-9]{12}$', 'Aadhar number should have 12 digits'),
             'MACAddress': RegexValidator(r'^([0-9A-F]{2}:){5}[0-9A-F]{2}$', 'MAC Address should be six pairs of hex digits in uppercase separated by colons'),
}

# def _GetPhotographPath(Instance, FileName):
#       FileExtension = FileName.split('.')[-1]
#       StorageName = Instance.RegistrationNumber + '.' + FileExtension
#       return 'student_photographs/{0}'.format(StorageName)



class Department(models.Model):
        department_number = models.CharField(max_length=10, unique=True, primary_key=True, validators=[Validators['DeptNo']])
        departmnet_name = models.CharField(max_length=200, unique=True)
        departmnet_short_name = models.CharField(max_length=100, unique=True)
        pub_date = models.DateTimeField('date published', default=datetime.datetime.now)


        def __str__(self):
                return '%s %s' %(self.departmnet_name, self.departmnet_short_name)


class Designation(models.Model):
        designation_number = models.CharField(max_length=10, unique=True, primary_key=True, validators=[Validators['Desig_No']])
        designation_name = models.CharField(max_length=200, unique=True)
        pub_date = models.DateTimeField('date published', default=datetime.datetime.now)

        def __str__(self):
                return '%s %s' %(self.designation_name, self.designation_number)

class Employee(models.Model):
        employee_id = models.CharField(max_length=10, unique=True, primary_key=True, validators=[Validators['Emp_No']])
        name = models.CharField(max_length=200)
        personal_phone_no = models.CharField(max_length=12, unique=True, validators=[Validators['Phone_No']])
        email_id = models.EmailField(unique=True)
        department_no = models.ForeignKey(Department, on_delete=models.CASCADE)
        designation_no = models.ForeignKey(Designation, on_delete=models.CASCADE)
        pub_date = models.DateTimeField('date published', default=datetime.datetime.now)

        def __str__(self):
                return self.employee_id

class Intercom(models.Model):
        intercom_number = models.CharField(max_length=4, unique=True, primary_key=True,validators=[Validators['Intercom_No']])
        emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
        pub_date = models.DateTimeField('date published', default=datetime.datetime.now)

        def __str__(self):
                return self.emp_id

class Cug(models.Model):
        cug_number = models.CharField(max_length=10, unique=True, primary_key=True, validators=[Validators['Cug_No']])
        emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
        paln = models.IntegerField(default=0, validators=[Validators['Plan_No']])
        pub_date = models.DateTimeField('date published', default=datetime.datetime.now)

        def __str__(self):
                return self.cug_number

class Quarter(models.Model):
        quarter_number = models.CharField(max_length=10, unique=True, primary_key=True, validators=[Validators['Quarter_No']])
        emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
        pub_date = models.DateTimeField('date published', default=datetime.datetime.now)

        def __str__(self):
                return self.quarter_number


    # phone_no = models.IntegerField(max_length=10)
    #def __str__(self):
        #return self.quarter_number


