# Generated by Django 2.1.7 on 2019-06-09 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_customuser_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images'),
        ),
    ]