# Generated by Django 3.1 on 2020-09-04 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20200903_2217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='profile_photo',
        ),
        migrations.AddField(
            model_name='customuser',
            name='main_image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]