# Generated by Django 4.2.6 on 2023-10-20 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='urlShotener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.CharField(max_length=200)),
                ('shortened_url', models.CharField(max_length=10)),
            ],
        ),
    ]
