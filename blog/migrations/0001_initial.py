# Generated by Django 2.2.3 on 2019-07-23 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pub_date', models.DateField(auto_now=True)),
                ('body', models.TextField(max_length=500)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
