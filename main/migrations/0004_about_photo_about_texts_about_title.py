# Generated by Django 4.0.4 on 2022-06-02 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_about_photo_remove_about_text_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
        migrations.AddField(
            model_name='about',
            name='texts',
            field=models.TextField(null=True, verbose_name='Текст про нас'),
        ),
        migrations.AddField(
            model_name='about',
            name='title',
            field=models.CharField(default=2, max_length=90, verbose_name='Название'),
            preserve_default=False,
        ),
    ]