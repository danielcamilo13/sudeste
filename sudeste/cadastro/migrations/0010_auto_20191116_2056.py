# Generated by Django 2.2.7 on 2019-11-16 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0009_auto_20191116_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cacamba',
            name='htcacamba',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cadastro.historicocacamba', verbose_name='Historico da cacamba'),
        ),
    ]
