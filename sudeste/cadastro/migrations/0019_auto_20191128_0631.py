# Generated by Django 2.2.7 on 2019-11-28 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0018_auto_20191128_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cacamba',
            name='argCacamba',
            field=models.IntegerField(blank=True, null=True, verbose_name='Argola'),
        ),
    ]
