# Generated by Django 3.2.5 on 2021-08-20 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210821_0259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payslip',
            name='Taxes',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='settaxes',
            name='taxPercent',
            field=models.IntegerField(),
        ),
    ]
