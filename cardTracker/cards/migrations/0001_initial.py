# Generated by Django 3.2.4 on 2021-06-21 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quanitity', models.IntegerField()),
                ('cardSet', models.CharField(max_length=50)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
