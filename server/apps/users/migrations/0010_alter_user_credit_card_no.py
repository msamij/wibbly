# Generated by Django 4.1 on 2022-09-16 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_user_credit_card_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='credit_card_no',
            field=models.IntegerField(unique=True),
        ),
    ]