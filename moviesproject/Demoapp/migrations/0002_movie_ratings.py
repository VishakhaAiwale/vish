# Generated by Django 4.0.5 on 2022-06-30 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Demoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='ratings',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
