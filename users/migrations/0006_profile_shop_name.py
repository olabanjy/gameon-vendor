# Generated by Django 3.2.9 on 2022-08-06 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_onboarded'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='shop_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]