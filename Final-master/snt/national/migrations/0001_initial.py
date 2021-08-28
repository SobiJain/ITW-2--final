# Generated by Django 3.1.3 on 2020-11-12 18:23

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NConveyance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conveyance', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='NPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='NPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.IntegerField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='national.npackage')),
            ],
        ),
        migrations.CreateModel(
            name='NBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Name must be greater than 1 character')])),
                ('date', models.DateField()),
                ('no_of_People', models.IntegerField(validators=[django.core.validators.MinValueValidator(1, 'Atleast one person should be on the trip!Or are you a Ghost?'), django.core.validators.MaxValueValidator(30, 'Bro a bus can only fit 30 people')])),
                ('any_special_requests', models.TextField(blank=True, null=True)),
                ('status', models.CharField(default='Not Confirmed', max_length=200)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='national.npackage')),
                ('preferred_mode_of_travel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='national.nconveyance')),
            ],
        ),
    ]
