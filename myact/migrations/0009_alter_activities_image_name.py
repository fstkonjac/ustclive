# Generated by Django 4.0.4 on 2022-06-13 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myact', '0008_activities_image_name_alter_activities_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activities',
            name='image_name',
            field=models.CharField(max_length=100),
        ),
    ]