# Generated by Django 4.1 on 2022-08-15 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activitybookingdays', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weekday',
            name='week_day',
            field=models.CharField(choices=[('Monday', 0), ('Tuesday', 1), ('Wednesday', 2), ('Thursday', 3), ('Friday', 4), ('Saturday', 5), ('Sunday', 6)], max_length=15),
        ),
    ]
