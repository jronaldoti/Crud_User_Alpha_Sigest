# Generated by Django 2.1.2 on 2018-10-28 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0003_auto_20181028_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='situacao',
            field=models.CharField(max_length=40),
        ),
    ]
