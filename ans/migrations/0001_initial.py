# Generated by Django 3.0.8 on 2020-08-22 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('from_email', models.EmailField(max_length=50)),
                ('subject', models.CharField(max_length=300)),
                ('message', models.TextField(max_length=1000)),
            ],
            options={
                'db_table': 'contact',
            },
        ),
    ]
