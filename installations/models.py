from django.db import models
from users.models import CustomUser
from django.utils import timezone
from cloudinary.models import CloudinaryField

# Create your models here.


class Location (models.Model):
    STATE_CHOICE = 	(('S', '-----------'),('AB', 'Abia'), ('FCT',' Abuja') , ('AD', 'Adamawa'), ('AK', 'Akwa Ibom'), ('AN', 'Anambra'), ('BA', 'Bauchi'), ('BY', 'Bayelsa'), 
                    ('BE', 'Benue'), ('BO', 'Borno'), ('CR', 'Cross River'), ('DE', 'Delta'), ('EB', 'Ebonyi'), ('ED', 'Edo'), ('EK', 'Ekiti'), ('EN', 'Enugu'), 
                    ('GO', 'Gombe'), ('IM', 'Imo'), ('JI', 'Jigawa'), ('KD', 'Kaduna'), ('KN', 'Kano'), ('KT', 'Katsina'), ('KE', 'Kebbi'), ('KO', 'Kogi'), ('KW', 'Kwara'), 
                    ('LA', 'Lagos'), ('NA', 'Nasarawa'), ('NI', 'Niger'), ('OG', 'Ogun'), ('ON', 'Ondo'), ('OS', 'Osun'), ('OY', 'Oyo'), ('PL', 'Plateau'), ('RI', 'Rivers'), (
                    'SO', 'Sokoto'), ('TA', 'Taraba'), ('YO', 'Yobe'), ('ZA', 'Zamfara'))
    clients = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    branch_id = models.CharField(blank=True, null=True, max_length=150)
    state = models.CharField(null=False, blank=False, max_length=4, choices= STATE_CHOICE, default='S')
    address = models.CharField(blank=False, null=False, max_length=200)
    date_added = models.DateField(auto_now_add=True)

    def __str__ (self):
        return f'{self.branch_id} - {self.address}'
    
class Installation (models.Model):
    EQUIPMENT_CHOICE = (('S', 'Select Equipment'),('UPS', 'UPS'),('UB', 'UPS Battery'), ('PI', 'Power Inverter'), ('PIB', 'Power Inverter Battery'), ('SP', 'Surge Protector'), ('PG', 'Power Generator'), ('GE', 'General Electrical Wiring and Earthing Condition'),
                        ('GTO', 'General Technical Observation'), ('BTR', 'Battery Rack Type'), ('AS', 'AVS Switcher'), ('OT', 'Others')
                        )
    STATUS_CHOICE = (('G', 'Good'), ('B', 'Bad'))
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    equipment_type = models.CharField(null=False, blank=False, max_length=4, choices=EQUIPMENT_CHOICE, default='S')
    equipment_others = models.CharField(null=True, blank=True, max_length=120)
    brand_name = models.CharField(null=False, blank=False, max_length=150)
    technical_specification = models.CharField(null=False, blank=False, max_length=120)
    date_manufactured = models.DateField(null=True, blank=True)
    installation_date = models.DateField(blank=False, null=False, default=timezone.now)
    replacement_date = models.DateField(blank=False, null=False)
    contact_person = models.CharField(null=False, blank=False, max_length=150)
    equipment_status = models.CharField(null=False, blank=False, max_length=1, choices=STATUS_CHOICE, default='Good')
    engineer = models.ForeignKey(CustomUser, on_delete= models.SET_NULL, null=True, blank=True)
    remark = models.CharField(null=False, blank=False, max_length=150)
    photo = CloudinaryField('image', null=True, blank=True)

    def __str__(self):
        return f'{self.get_equipment_type_display()}, {self.brand_name}, {self.location.address}, - by: {self.engineer.first_name}'

class Report (models.Model):
    engineer = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    installation = models.ForeignKey(Installation, on_delete=models.CASCADE)
    report = models.CharField(null=False, blank=False, max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.installation.location.branch_id} - {self.engineer.first_name} - {self.installation.equipment_type} - {self.report}'
