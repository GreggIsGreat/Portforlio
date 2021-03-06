# Generated by Django 3.2.7 on 2021-09-29 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('Physical_Address', models.CharField(max_length=200)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=200)),
                ('Postal_Address', models.CharField(max_length=200)),
                ('Name_of_Parent', models.CharField(max_length=200)),
                ('Description', models.TextField(max_length=200)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
