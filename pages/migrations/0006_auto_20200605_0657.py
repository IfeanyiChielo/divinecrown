# Generated by Django 2.1.5 on 2020-06-05 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20200529_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creamsales',
            name='cream_marketer_status',
            field=models.CharField(choices=[('A', 'Groupa'), ('B', 'Groupb'), ('C', 'Groupc')], max_length=1),
        ),
    ]
