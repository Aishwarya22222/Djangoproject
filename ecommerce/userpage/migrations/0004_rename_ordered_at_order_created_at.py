# Generated by Django 4.2.1 on 2023-08-15 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userpage', '0003_rename_contact_number_order_phone_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='ordered_at',
            new_name='created_at',
        ),
    ]
