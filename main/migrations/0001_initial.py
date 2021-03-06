# Generated by Django 4.0.4 on 2022-06-02 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_about', models.TextField(verbose_name='Про нас')),
            ],
            options={
                'verbose_name': 'Добавить текст на страницу "Про нас"',
                'verbose_name_plural': 'Добавить текст на страницу "Про нас"',
            },
        ),
        migrations.CreateModel(
            name='HomeNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='img')),
                ('title', models.CharField(max_length=90, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('date', models.DateTimeField(verbose_name='Дата и время публикации')),
            ],
            options={
                'verbose_name': 'Новости на главном странице',
                'verbose_name_plural': 'Новости на главном странице',
            },
        ),
    ]
