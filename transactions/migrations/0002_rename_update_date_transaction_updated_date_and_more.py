# Generated by Django 4.2.4 on 2023-09-20 05:47

from django.db import migrations
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='update_date',
            new_name='updated_date',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_id',
            field=shortuuid.django_fields.ShortUUIDField(alphabet='0123456789', length=15, max_length=25, prefix='', unique=True),
        ),
    ]