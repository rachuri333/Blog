# Generated by Django 3.0.2 on 2020-02-10 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200209_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='1437653332689.jpg', upload_to='profile_pics/'),
        ),
    ]