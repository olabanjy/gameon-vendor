# Generated by Django 3.2.9 on 2022-01-02 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20220102_0716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='address_1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='address_2',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='state',
        ),
        migrations.AlterField(
            model_name='userkyc',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_kyc', to='users.profile'),
        ),
    ]
