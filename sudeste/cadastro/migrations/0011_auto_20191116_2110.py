# Generated by Django 2.2.7 on 2019-11-17 00:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0010_auto_20191116_2056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cacamba',
            name='htcacamba',
        ),
        migrations.AddField(
            model_name='historicocacamba',
            name='cacamba',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cadastro.cacamba', verbose_name='Historico de cacamba'),
        ),
    ]
