from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_alter_media_description_alter_media_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='description',
            field=models.TextField(blank=True, default='No description'),
            preserve_default=False,

        ),
        migrations.AlterField(
            model_name='media',
            name='file',
            field=models.FileField(upload_to='media_uploads/'),
        ),
        migrations.AlterField(
            model_name='media',
            name='media_type',
            field=models.CharField(choices=[('photo', 'Photo'), ('video', 'Video')], max_length=10),
        ),
    ]
