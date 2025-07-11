# Generated by Django 5.2.1 on 2025-05-23 16:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_company_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company_profile',
            name='company_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='resume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.resume'),
        ),
        migrations.AlterField(
            model_name='resume',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.address'),
        ),
    ]
