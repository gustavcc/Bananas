# Generated by Django 5.0.6 on 2024-08-06 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bananas', '0013_cutofbanana_id_lot_cutofbanana_porcentagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cutofbanana',
            name='date',
            field=models.DateField(),
        ),
    ]