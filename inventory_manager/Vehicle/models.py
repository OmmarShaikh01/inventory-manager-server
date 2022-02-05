import uuid
from django.db import models
from django.db.models import (
    Model, UUIDField, CharField, TextField, BooleanField, DateField, EmailField, FileField, ImageField,
    IntegerField, ForeignKey, ManyToManyField,
)

VEHICLE_TYPE = [
    ('BK', 'Bike'),
    ('SK', 'Scooter'),
]
VEHICLE_STATUS = [
    ('REPR', 'Repairs'),
    ('INCM', 'Incomming'),
    ('OTCM', 'Outgoing'),
]
VEHICLE_SERVICE_STATUS = [
    ('REPR', 'Repairs'),
    ('WATP', 'Waiting For Parts'),
    ('COMP', 'Completed'),
]
VEHICLE_PAYMENT_STATUS = [
    ('COMP', 'Complete'),
    ('INCP', 'Incomplete'),
    ('NAPV', 'Approval Needed'),
    ('APVD', 'Approval Completed'),
    ('DWNP', 'Downpayment Paid'),
]
VEHICLE_REG_STATE = [
    ('AN', 'Andaman and Nicobar Islands'),
    ('AP', 'Andhra Pradesh'),
    ('AR', 'Arunachal Pradesh'),
    ('AS', 'Assam'),
    ('BH', 'Bharat'),
    ('BR', 'Bihar'),
    ('CH', 'Chandigarh'),
    ('CG', 'Chhattisgarh'),
    ('DD', 'Dadra and Nagar Haveli and Daman and Diu'),
    ('DL', 'Delhi'),
    ('GA', 'Goa'),
    ('GJ', 'Gujarat'),
    ('HR', 'Haryana'),
    ('HP', 'Himachal Pradesh'),
    ('JK', 'Jammu and Kashmir'),
    ('JH', 'Jharkhand'),
    ('KA', 'Karnataka'),
    ('KL', 'Kerala'),
    ('LA', 'Ladakh'),
    ('LD', 'Lakshadweep'),
    ('MP', 'Madhya Pradesh'),
    ('MH', 'Maharashtra'),
    ('MN', 'Manipur'),
    ('ML', 'Meghalaya'),
    ('MZ', 'Mizoram'),
    ('NL', 'Nagaland'),
    ('OD', 'Odisha'),
    ('PY', 'Puducherry'),
    ('PB', 'Punjab'),
    ('RJ', 'Rajasthan'),
    ('SK', 'Sikkim'),
    ('TN', 'Tamil Nadu'),
    ('TS', 'Telangana'),
    ('TR', 'Tripura'),
    ('UP', 'Uttar Pradesh'),
    ('UK', 'Uttarakhand'),
    ('WB', 'West Bengal'),
]


class Vehicle(Model):
    vehicle_id = UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    customer_id = ForeignKey("Customer", to_field = "customer_id", on_delete = models.CASCADE)
    vehicle_type = CharField(max_length = 2, choices = VEHICLE_TYPE)
    maker = CharField(max_length = 64)
    model = CharField(max_length = 64)
    year = DateField()
    color = CharField(max_length = 64)
    status = CharField(max_length = 4, choices = VEHICLE_STATUS)
    date_of_purchase = DateField()
    license_plate = CharField(max_length = 10)
    state_of_registration = CharField(max_length = 2, choices = VEHICLE_REG_STATE)
    VIN_number = CharField(max_length = 17)
    mileage = IntegerField()
    location_of_vehicle = CharField(max_length = 2, choices = VEHICLE_REG_STATE)
    payment_status = CharField(max_length = 4, choices = VEHICLE_PAYMENT_STATUS)
    cost = IntegerField()
    service_status = CharField(max_length = 4, choices = VEHICLE_SERVICE_STATUS)
    hasImage = BooleanField(default = False)
    hasDocument = BooleanField(default = False)
    isInsured = BooleanField(default = False)
    isFinanced = BooleanField(default = False)


class Customer(Model):

    # noinspection PyMethodParameters
    def customer_image_upload(inst, filename):
        return 'customer/user_{0}'.format(isnt.customer_id.id)

    customer_id = UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    first_name = CharField(max_length = 64)
    last_name = CharField(max_length = 64)
    address = TextField()
    email = EmailField()
    primary_number = IntegerField()
    secondary_number = IntegerField()
    bank_name = CharField(max_length = 256)
    account_number = CharField(max_length = 64)
    customer_image = ImageField(width_field = 413, height_field = 531, upload_to = customer_image_upload)
    comment = TextField()


class Financier(Model):
    financier_id = UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    vehicle_id = ForeignKey("Vehicle", to_field = "vehicle_id", on_delete = models.CASCADE)
    name = CharField(max_length = 64)
    account_number = CharField(max_length = 64)
    monthly_payment = IntegerField()
    expected_date_of_last_payment = DateField()
    status = CharField(max_length = 4, choices = VEHICLE_PAYMENT_STATUS)
    downpayment = IntegerField()


class Document(Model):

    # noinspection PyMethodParameters
    def doc_url_upload(inst, filename):
        return f'document/vehicle_{inst.vehicle_id.id}/{inst.doc_id.id}'

    DOC_TYPE = [
        ("INS", "Insurance"),
        ("ADH", "Adhaar Card"),
        ("EBL", "Electricity Bill"),
        ("HAR", "House Agreement"),
        ("LIC", "Licence"),
        ("PAN", "PAN Card"),
        ("PPT", "Passport"),
        ("LON", "Loan"),
    ]
    doc_id = UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    vehicle_id = ForeignKey("Vehicle", to_field = "vehicle_id", on_delete = models.CASCADE)
    doc_url = FileField(upload_to = doc_url_upload)
    doc_type = CharField(max_length = 3, choices = DOC_TYPE)


class Vehicle_Image(Model):

    # noinspection PyMethodParameters
    def image_url_upload(inst, filename):
        return 'vehi_img/vehicle_{0}/{1}'.format(inst.vehicle_id.id, inst.image_type.id)

    IMAGE_TYPE = [
        ('L', 'Left'),
        ('R', 'Right'),
        ('F', 'Front'),
        ('B', 'Back'),
    ]

    image_id = UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    vehicle_id = ForeignKey("Vehicle", to_field = "vehicle_id", on_delete = models.CASCADE)
    image_url = ImageField(width_field = 600, height_field = 600, upload_to = image_url_upload)
    image_type = CharField(max_length = 3, choices = IMAGE_TYPE)
