# Generated by Django 4.1.7 on 2023-04-07 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0004_alter_qr_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qr',
            name='published_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
