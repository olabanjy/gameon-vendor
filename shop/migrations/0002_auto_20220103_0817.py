# Generated by Django 3.2.9 on 2022-01-03 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='itemTrailerVideo',
            field=models.FileField(blank=True, default='default_trailer_video.mp4', upload_to='vendor/gameon/shop/items/trailer/mp4/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='bannerImagePath',
            field=models.ImageField(blank=True, default='default_banner_pics.jpg', upload_to='vendor/gameon/shop/items/bannerImagePath/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='displayImagePath',
            field=models.ImageField(blank=True, default='default_display_pics.jpg', upload_to='vendor/gameon/shop/items/displayImagePath/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='thumbnailImagePath',
            field=models.ImageField(blank=True, default='default_thumbnail_pics.jpg', upload_to='vendor/gameon/shop/items/thumbnailImagePath/'),
        ),
    ]
