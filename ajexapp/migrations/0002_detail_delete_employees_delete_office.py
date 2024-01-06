# Generated by Django 4.1.4 on 2023-09-08 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ajexapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField()),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.DeleteModel(
            name='Employees',
        ),
        migrations.DeleteModel(
            name='Office',
        ),
    ]