# Generated by Django 3.2.9 on 2022-08-02 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20220102_0900'),
        ('shop', '0002_auto_20220103_0817'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='quantity',
            new_name='numberInStock',
        ),
        migrations.RemoveField(
            model_name='item',
            name='itemTrailerVideo',
        ),
        migrations.RemoveField(
            model_name='item',
            name='type',
        ),
        migrations.AddField(
            model_name='item',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='bannerImagePath',
            field=models.ImageField(blank=True, default='default_banner_pics.jpg', upload_to='gameon/admin/shop/games/bannerImagePath/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='cat',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='displayImagePath',
            field=models.ImageField(blank=True, default='default_display_pics.jpg', upload_to='gameon/admin/shop/games/displayImagePath/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='platform',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='thumbnailImagePath',
            field=models.ImageField(blank=True, default='default_thumbnail_pics.jpg', upload_to='gameon/admin/shop/games/thumbnailImagePath/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item_vendor', to='users.profile'),
        ),
    ]
