# Generated by Django 4.0.3 on 2022-03-22 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_newsletter_alter_booking_reservation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='service',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], max_length=200),
        ),
    ]
