from django.db import models
from users.models import CustomUser
from django.utils import timezone
from cloudinary.models import CloudinaryField

# Create your models here.


class Location (models.Model):
    STATE_CHOICE = 	(('S', '-----------'),('AB', 'Abia'), ('FCT',' FCT') , ('AD', 'Adamawa'), ('AK', 'Akwa Ibom'), ('AN', 'Anambra'), ('BA', 'Bauchi'), ('BY', 'Bayelsa'), 
                    ('BE', 'Benue'), ('BO', 'Borno'), ('CR', 'Cross River'), ('DE', 'Delta'), ('EB', 'Ebonyi'), ('ED', 'Edo'), ('EK', 'Ekiti'), ('EN', 'Enugu'), 
                    ('GO', 'Gombe'), ('IM', 'Imo'), ('JI', 'Jigawa'), ('KD', 'Kaduna'), ('KN', 'Kano'), ('KT', 'Katsina'), ('KE', 'Kebbi'), ('KO', 'Kogi'), ('KW', 'Kwara'), 
                    ('LA', 'Lagos'), ('NA', 'Nasarawa'), ('NI', 'Niger'), ('OG', 'Ogun'), ('ON', 'Ondo'), ('OS', 'Osun'), ('OY', 'Oyo'), ('PL', 'Plateau'), ('RI', 'Rivers'), (
                    'SO', 'Sokoto'), ('TA', 'Taraba'), ('YO', 'Yobe'), ('ZA', 'Zamfara'))
    REGION_CHOICE = (('S', '-----------'),('ABJ1', 'ABUJA 1'), ('ABJ2', 'ABUJA 2'), ('AI', 'AGEGE IKORODU'), ('AP', 'APAPA'), ('AW', 'AWKA'), ('CRA', 'CROSS RIVER AKWA IBOM'), 
                    ('EE', 'ENUGU EBONYI'), ('FE', 'FESTAC'), ('IK', 'IKEJA'), ('IKL', 'IKOYI'), ('IA', 'IMO ABIA'), ('LI', 'LAGOS ISLAND'), ('MA1', 'MAINLAIN 1'), ('MA2', 'MAINLAIN 2'), 
                    ('MD1', 'MIDWEST 1'), ('MD2', 'MIDWEST 2'), ('NC', 'NORTH CENTRAL'), ('NE', 'NORTH EAST'), ('NW1', 'NORTH WEST 1'), ('NW2', 'NORTH WEST 2'), ('ON', 'ONITSHA'), 
                    ('RB1', 'RIVER BAYELSA 1'), ('RB2', 'RIVER BAYELSA 2'), ('SW1', 'SOUTH WEST 1'), ('SW2', 'SOUTH WEST 2'), ('VI', 'VICTORIA ISLAND'))
    clients = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    branch = models.CharField(blank=True, null=True, max_length=250)
    branch_id = models.CharField(blank=True, null=True,  max_length=15)
    cug_num1 = models.CharField(blank=True, null=True, max_length=14)
    cug_num2 = models.CharField(blank=True, null=True, max_length=14)
    state = models.CharField(null=False, blank=False, max_length=4, choices= STATE_CHOICE, default='S')
    address = models.CharField(blank=False, null=False, max_length=200)
    regional_office = models.BooleanField(default=False)
    region = models.CharField(max_length=5, choices=REGION_CHOICE, default='S')
    date_added = models.DateField(auto_now_add=True)

    def __str__ (self):
        return f'{self.branch_id} - {self.address}'
    
class Installation (models.Model):
    EQUIPMENT_CHOICE = (('S', 'Select Equipment'),('UPS', 'UPS'),('UB', 'UPS Battery'), ('PI', 'Power Inverter'), ('IB', 'Inverter Battery'), ('SP', 'Surge Protector'), ('PG', 'Power Generator'), ('VR', 'Voltage Regulator'),
                        ('BS', 'Bypass Switch'), ('SOP', 'Solar Panel'), ('OT', 'Others')
                        )
    STATUS_CHOICE = (('G', 'Good'), ('B', 'Bad'))
    LIFE_SPAN_CHOICE = (('NR', 'Not Rated'), ('1L', '1-2 Years'), ('2L', '2-3 Years'), ('3L', '3-4 Years'), ('4L', '4-5 Years'), ('5L', '5-6 Years'), ('6L', '6-7 Years'), ('7L', '7-8 Years'), 
                        ('8L', '8-9 Years'), ('9L', '9-10 Years'),  ('2kL', '2-4 Years'), ('4kL', '4-6 Years'), ('6kL', '6-8 Years'), ('8kL', '8-10 Years'), ('2YL', '20-25 Years'), ('5YL', '25-30 Years'), ('10YL', '30-35 Years'), ('OT', 'Others')) 
                        
    BRAND_CHOICE =(('S', 'Select Brand'),('', '---------------- Battery Brands----------------'), ('AMARON', 'AMARON'), ('ARCCHAR', 'ARCCHAR'), ('DAYSTAR', 'DAYSTAR'), ('E.P', 'E.P'), ('EVER EXCEED', 'EVER EXCEED'), ('FELICITY', 'FELICITY'), ('G.P', 'G.P'), ('GASTON', 'GASTON'),
                    ('GENUS', 'GENUS'), ('HOPPECKE', 'HOPPECKE'), ('MECURY', 'MECURY'), ('MF', 'MF'), ('MONBAT', 'MONBAT'), ('MVR', 'MVR'), ('POWER PREM', 'POWER PREM'), ('POWER STAR', 'POWER STAR'), 
                    ('POWER V', 'POWER V'), ('PRIME SOLAR', 'PRIME SOLAR'), ('PROSTAR-LEMAX', 'PROSTAR-LEMAX'), ('QUANTA', 'QUANTA'), ('RITAR', 'RITAR'), ('SHOTO', 'SHOTO'), ('SURFIT', 'SURFIT'), 
                    ('TRATA', 'TRATA'), ('TROJAN SAGEM', 'TROJAN SAGEM'), ('TROJAN(SLIM)', 'TROJAN(SLIM)'), (' ', '---------------- Generator Brands ----------------'), ('C-POWER', 'C-POWER'), ('CUMMINS', 'CUMMINS'), ('FG WILSON', 'FG WILSON'), ('GHADDOR', 'GHADDOR'), ('HAT GLOBAL SP', 'HAT GLOBAL SP'),
                    ('JMG', 'JMG'), ('JOHN HOLT', 'JOHN HOLT'), ('JUBALLI', 'JUBALLI'), ('KHNEISSER HIJAZI', 'KHNEISSER HIJAZI'), ('MANTRAC', 'MANTRAC'), ('MARAPCO', 'MARAPCO'),('MARCOPOLO', 'MARCOPOLO'), 
                    ('MIKANO', 'MIKANO'), ('PERKINS', 'PERKINS'), (' ', '---------------- Inverter Brands ----------------'), ('AARCHOR', 'AARCHOR'),('BPC', 'BPC'),('COMP HC', 'COMP HC'),('EMERSON', 'EMERSON'),('ENDLESS POWER', 'ENDLESS POWER'),('ENERGIER', 'ENERGIER'),
                    ('FELICITY', 'FELICITY'),('FRONIOUS', 'FRONIOUS'),('GENNEX', 'GENNEX'),('INFORM', 'INFORM'),('IPOWER PLUS', 'IPOWER PLUS'),('KINERGIER PRO', 'KINERGIER PRO'),('LIEBERT', 'LIEBERT'),
                    ('MEGATECH', 'MEGATECH'),('MONEY POWER', 'MONEY POWER'),('MST SERIES', 'MST SERIES'),('NUMERIC', 'NUMERIC'),('OPTI-SOLAR', 'OPTI-SOLAR'),('POWER PRO', 'POWER PRO'),(
                        'POWERGEM PRO', 'POWERGEM PRO'),('POWERSINE', 'POWERSINE'),('PROSTAR', 'PROSTAR'),('SCHNEIDER', 'SCHNEIDER'),('SOROTEC', 'SOROTEC'), ('OT', 'Others'))
 

    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    equipment_type = models.CharField(null=False, blank=False, max_length=4, choices=EQUIPMENT_CHOICE, default='S')
    equipment_others = models.CharField(null=True, blank=True, max_length=120)
    quantity = models.IntegerField(default=1)
    life_span = models.CharField(choices=LIFE_SPAN_CHOICE, max_length=5, default='NR')
    brand_name = models.CharField(null=False, blank=False, choices=BRAND_CHOICE, max_length=90)
    brand_others = models.CharField(null=True, blank=True, max_length=120)
    technical_specification = models.CharField(null=False, blank=False, max_length=120)
    date_manufactured = models.DateField(null=True, blank=True)
    installation_date = models.DateField(blank=True, null=True)
    replacement_date = models.DateField(blank=True, null=True)
    contact_person = models.CharField(null=True, blank=True, max_length=150)
    equipment_status = models.CharField(null=False, blank=False, max_length=1, choices=STATUS_CHOICE, default='Good')
    engineer = models.ForeignKey(CustomUser, on_delete= models.SET_NULL, null=True, blank=True)
    remark = models.CharField(max_length=150)
    photo = CloudinaryField('image', null=True, blank=True)

    def __str__(self):
        return f'{self.get_equipment_type_display()}, {self.get_brand_name_display()}, {self.location.address}'

class Report (models.Model):
    engineer = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    installation = models.ForeignKey(Installation, on_delete=models.CASCADE)
    report = models.CharField(null=False, blank=False, max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.installation.location.branch_id} - {self.installation.get_equipment_type_display()} - {self.report}'
