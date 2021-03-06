# Generated by Django 4.0.4 on 2022-06-13 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activities',
            name='details',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='activities',
            name='img_url',
            field=models.ImageField(upload_to='img_url/', verbose_name='图片地址'),
        ),
        migrations.AlterField(
            model_name='activities',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='activities',
            name='phone',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='activities',
            name='topic',
            field=models.CharField(max_length=100),
        ),
    ]
