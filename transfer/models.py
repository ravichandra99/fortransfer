from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
import uuid

# Create your models here.

class JustBase(models.Model):
	TRANSFER_REASON = [('MG','Medical Ground'),('PAR','Parent working in Govt / PSU/ Corporation got transferred'),('CLO','closure of course/ college')]
	TRANSFER_TYPE = [('WITHIN','With in the same university affiliated colleges'),('INTER','Inter University affiliated colleges'),('OTHER','Others')]
	COURSES = [('C1','COURSE1'),('C2','COURSE2')]
	PRUNIVERSITY_LIST = [('U1','UNIVERSITY1'),('U2','UNIVERSITY2')]
	PRDISTRICT_LIST = [('D1','DISTRICT1'),('D2','DISTRICT2')]
	PRCLASS = [('Cl1','CLASS1'),('Cl2','CLASS2')]
	PRCOLLEGE_LIST = [('Co1','COLLEGE1'),('Co2','COLLEGE2')]
	SUNIVERSITY_LIST = [('U1','UNIVERSITY1'),('U2','UNIVERSITY2')]
	SDISTRICT_LIST = [('D1','DISTRICT1'),('D2','DISTRICT2')]
	SCOLLEGE_LIST = [('Co1','COLLEGE1'),('Co2','COLLEGE2')]
	YN = [('YES','YES'),('NO','NO')]
	reason = models.CharField(max_length=3, choices=TRANSFER_REASON,verbose_name = 'Reason For Transfer')
	trtype = models.CharField(max_length=10, choices=TRANSFER_TYPE,verbose_name = 'Type of Transfer')
	regno = models.CharField(max_length = 20, verbose_name = 'Reg. No /Admission No')
	name = models.CharField(max_length = 100,verbose_name = 'Name of the Candidate')
	father = models.CharField(max_length = 100,verbose_name = "Father's Name")
	year = models.IntegerField(verbose_name = 'Year of Admission')
	course = models.CharField(max_length=3, choices=COURSES)
	branch = models.CharField(max_length=3, default = 'TF')
	prclass = models.CharField(max_length=3, choices=PRCLASS,verbose_name = 'Present Studying Class')
	auniv = models.CharField(max_length=3, choices=PRUNIVERSITY_LIST,verbose_name = 'Affiliated University')
	prdistrict = models.CharField(max_length=3, choices=PRDISTRICT_LIST,verbose_name = 'District of Present Studying College')
	prcollege = models.CharField(max_length=3, choices=PRCOLLEGE_LIST,verbose_name = 'Present Studying College')
	prnoc_number = models.CharField(max_length = 100,verbose_name = 'NOC Number for Present College', default = str(uuid.uuid4()))
	prnoc_date = models.DateField()
	issued = models.CharField(max_length=3, choices=YN, default = 'TF')
	district = models.CharField(max_length=3, choices=SDISTRICT_LIST,verbose_name = 'District of Seeking College')
	college = models.CharField(max_length=3, choices=SCOLLEGE_LIST,verbose_name = 'Present Seeking College')
	sauniv = models.CharField(max_length=3, choices=SUNIVERSITY_LIST,verbose_name = 'Seeking Affiliated University')
	snoc_number = models.CharField(max_length = 100,verbose_name = 'NOC Number for Seeking College',default = str(uuid.uuid4()))
	snoc_date = models.DateField()
	doc = models.FileField(upload_to = '',verbose_name = 'Supporting Document')
	email = models.EmailField()
	mobile = PhoneNumberField()
	under = models.BooleanField(verbose_name = "Accept")

	def __str__(self):
		return self.name








