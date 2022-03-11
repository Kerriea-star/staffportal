# Generated by Django 4.0 on 2022-03-07 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('regNO', models.IntegerField(default=0)),
                ('post', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('period', models.IntegerField(blank=True, default=0, null=True)),
                ('salary', models.FloatField(default=0)),
            ],
        ),
    ]
