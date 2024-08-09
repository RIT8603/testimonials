# Generated by Django 5.0.6 on 2024-05-30 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('college', models.CharField(max_length=200)),
                ('age', models.IntegerField(max_length=10)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
