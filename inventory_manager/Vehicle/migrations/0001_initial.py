# Generated by Django 4.0.1 on 2022-02-04 12:45

from django.db import migrations, models
import django.db.models.deletion
import inventory_manager.Vehicle.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('address', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('primary_number', models.IntegerField()),
                ('secondary_number', models.IntegerField()),
                ('bank_name', models.CharField(max_length=256)),
                ('account_number', models.CharField(max_length=64)),
                ('customer_image', models.ImageField(height_field=531, upload_to=inventory_manager.Vehicle.models.Customer.customer_image_upload, width_field=413)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vehicle_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('vehicle_type', models.CharField(choices=[('BK', 'Bike'), ('SK', 'Scooter')], max_length=2)),
                ('maker', models.CharField(max_length=64)),
                ('model', models.CharField(max_length=64)),
                ('year', models.DateField()),
                ('color', models.CharField(max_length=64)),
                ('status', models.CharField(choices=[('REPR', 'Repairs'), ('INCM', 'Incomming'), ('OTCM', 'Outgoing')], max_length=4)),
                ('date_of_purchase', models.DateField()),
                ('license_plate', models.CharField(max_length=10)),
                ('state_of_registration', models.CharField(choices=[('AN', 'Andaman and Nicobar Islands'), ('AP', 'Andhra Pradesh'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BH', 'Bharat'), ('BR', 'Bihar'), ('CH', 'Chandigarh'), ('CG', 'Chhattisgarh'), ('DD', 'Dadra and Nagar Haveli and Daman and Diu'), ('DL', 'Delhi'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('HR', 'Haryana'), ('HP', 'Himachal Pradesh'), ('JK', 'Jammu and Kashmir'), ('JH', 'Jharkhand'), ('KA', 'Karnataka'), ('KL', 'Kerala'), ('LA', 'Ladakh'), ('LD', 'Lakshadweep'), ('MP', 'Madhya Pradesh'), ('MH', 'Maharashtra'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OD', 'Odisha'), ('PY', 'Puducherry'), ('PB', 'Punjab'), ('RJ', 'Rajasthan'), ('SK', 'Sikkim'), ('TN', 'Tamil Nadu'), ('TS', 'Telangana'), ('TR', 'Tripura'), ('UP', 'Uttar Pradesh'), ('UK', 'Uttarakhand'), ('WB', 'West Bengal')], max_length=2)),
                ('VIN_number', models.CharField(max_length=17)),
                ('mileage', models.IntegerField()),
                ('location_of_vehicle', models.CharField(choices=[('AN', 'Andaman and Nicobar Islands'), ('AP', 'Andhra Pradesh'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BH', 'Bharat'), ('BR', 'Bihar'), ('CH', 'Chandigarh'), ('CG', 'Chhattisgarh'), ('DD', 'Dadra and Nagar Haveli and Daman and Diu'), ('DL', 'Delhi'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('HR', 'Haryana'), ('HP', 'Himachal Pradesh'), ('JK', 'Jammu and Kashmir'), ('JH', 'Jharkhand'), ('KA', 'Karnataka'), ('KL', 'Kerala'), ('LA', 'Ladakh'), ('LD', 'Lakshadweep'), ('MP', 'Madhya Pradesh'), ('MH', 'Maharashtra'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OD', 'Odisha'), ('PY', 'Puducherry'), ('PB', 'Punjab'), ('RJ', 'Rajasthan'), ('SK', 'Sikkim'), ('TN', 'Tamil Nadu'), ('TS', 'Telangana'), ('TR', 'Tripura'), ('UP', 'Uttar Pradesh'), ('UK', 'Uttarakhand'), ('WB', 'West Bengal')], max_length=2)),
                ('payment_status', models.CharField(choices=[('COMP', 'Complete'), ('INCP', 'Incomplete'), ('NAPV', 'Approval Needed'), ('APVD', 'Approval Completed'), ('DWNP', 'Downpayment Paid')], max_length=4)),
                ('cost', models.IntegerField()),
                ('service_status', models.CharField(choices=[('REPR', 'Repairs'), ('WATP', 'Waiting For Parts'), ('COMP', 'Completed')], max_length=4)),
                ('hasImage', models.BooleanField(default=False)),
                ('hasDocument', models.BooleanField(default=False)),
                ('isInsured', models.BooleanField(default=False)),
                ('isFinanced', models.BooleanField(default=False)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vehicle.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle_Image',
            fields=[
                ('image_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image_url', models.ImageField(height_field=600, upload_to=inventory_manager.Vehicle.models.Vehicle_Image.image_url_upload, width_field=600)),
                ('image_type', models.CharField(choices=[('L', 'Left'), ('R', 'Right'), ('F', 'Front'), ('B', 'Back')], max_length=3)),
                ('vehicle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vehicle.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Financier',
            fields=[
                ('financier_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('account_number', models.CharField(max_length=64)),
                ('monthly_payment', models.IntegerField()),
                ('expected_date_of_last_payment', models.DateField()),
                ('status', models.CharField(choices=[('COMP', 'Complete'), ('INCP', 'Incomplete'), ('NAPV', 'Approval Needed'), ('APVD', 'Approval Completed'), ('DWNP', 'Downpayment Paid')], max_length=4)),
                ('downpayment', models.IntegerField()),
                ('vehicle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vehicle.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('doc_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('doc_url', models.FileField(upload_to=inventory_manager.Vehicle.models.Document.doc_url_upload)),
                ('doc_type', models.CharField(choices=[('INS', 'Insurance'), ('ADH', 'Adhaar Card'), ('EBL', 'Electricity Bill'), ('HAR', 'House Agreement'), ('LIC', 'Licence'), ('PAN', 'PAN Card'), ('PPT', 'Passport'), ('LON', 'Loan')], max_length=3)),
                ('vehicle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vehicle.vehicle')),
            ],
        ),
    ]
