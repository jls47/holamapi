# Generated by Django 2.1.3 on 2018-11-17 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20181115_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programrequest',
            name='id',
            field=models.CharField(default=9117, max_length=4, primary_key=True, serialize=False),
        ),
    ]
