# Generated by Django 3.1.4 on 2020-12-18 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201210_1843'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Resumo',
            new_name='Historia',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Conteudo',
            new_name='Jogadores',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Autor',
            new_name='Tecnico',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='Titulo',
            new_name='Time',
        ),
        migrations.RemoveField(
            model_name='post',
            name='Data',
        ),
    ]
