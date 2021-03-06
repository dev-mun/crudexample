# Generated by Django 3.0.5 on 2020-04-28 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('given_name', models.CharField(max_length=32)),
                ('family_name', models.CharField(max_length=32)),
                ('job_title', models.CharField(max_length=64, null=True)),
                ('address', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=254, null=True)),
                ('telephone', models.CharField(max_length=16)),
            ],
        ),
    ]
