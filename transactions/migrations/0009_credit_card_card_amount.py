# Generated by Django 4.2.4 on 2023-10-16 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0008_rename_date_credit_card_card_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='credit_card',
            name='card_amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
    ]