# Generated by Django 3.1 on 2020-09-02 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_image_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image_user',
            field=models.ImageField(blank=True, null=True, upload_to='profile_image'),
        ),
    ]
