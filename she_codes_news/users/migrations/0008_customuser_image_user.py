# Generated by Django 3.1 on 2020-09-03 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_customuser_image_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image_user',
            field=models.ImageField(blank=True, null=True, upload_to='news/profile_image/'),
        ),
    ]
