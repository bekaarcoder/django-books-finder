# Generated by Django 3.2 on 2021-04-27 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=255)),
                ('pages', models.CharField(max_length=255)),
                ('book_format', models.CharField(max_length=255)),
                ('size', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('ip', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Books',
            },
        ),
    ]