# Generated by Django 5.2 on 2025-04-19 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='file',
            field=models.FileField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='media',
            name='media_type',
            field=models.CharField(max_length=50),
        ),
    ]
