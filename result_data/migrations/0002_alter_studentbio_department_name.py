# Generated by Django 4.0.4 on 2022-06-04 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentbio',
            name='department_name',
            field=models.CharField(default='Chandigarh university', max_length=50),
        ),
    ]
