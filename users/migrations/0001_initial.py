# Generated by Django 3.2.9 on 2021-12-31 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableCountry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_code', models.CharField(max_length=200)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserLoginActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_IP', models.CharField(blank=True, max_length=200, null=True)),
                ('login_datetime', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(blank=True, choices=[('success', 'Success'), ('failed', 'Failed')], default='success', max_length=100, null=True)),
                ('user_agent_info', models.CharField(blank=True, max_length=255, null=True)),
                ('login_city', models.CharField(blank=True, max_length=255, null=True)),
                ('login_country', models.CharField(blank=True, max_length=255, null=True)),
                ('login_loc', models.CharField(blank=True, max_length=255, null=True)),
                ('login_other_info', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserKYC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_type', models.CharField(max_length=200)),
                ('id_unique_number', models.CharField(max_length=200, null=True)),
                ('photo', models.FileField(blank=True, default='default_photo.jpg', upload_to='gameon/vendor/kyc/front_path/')),
                ('photo_2', models.FileField(blank=True, default='default_photo.jpg', upload_to='gameon/vendor/kyc/front_back/')),
                ('verified', models.BooleanField(default=False)),
                ('verified_at', models.DateField(null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_kyc', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_code', models.CharField(max_length=200)),
                ('key', models.CharField(blank=True, max_length=100, unique=True)),
                ('enable_2fa', models.BooleanField(default=False)),
                ('phone', models.CharField(blank=True, max_length=40, null=True)),
                ('phone_verified', models.BooleanField(default=False)),
                ('first_name', models.CharField(blank=True, max_length=200, null=True)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('dob', models.DateField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, max_length=200, null=True)),
                ('profile_set_up', models.BooleanField(default=False)),
                ('dev_phase', models.CharField(choices=[('live_prod', 'Live Prod'), ('staging', 'Staging'), ('beta', 'Beta')], default='beta', max_length=200)),
                ('photo', models.ImageField(blank=True, default='default_profile_pics.jpg', upload_to='gameon/vendor/user_profile/')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=100)),
                ('apartment_address', models.CharField(max_length=100)),
                ('city', models.CharField(blank=True, max_length=300, null=True)),
                ('state', models.CharField(blank=True, max_length=300, null=True)),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('zip', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
