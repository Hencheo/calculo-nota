# Generated by Django 5.0.1 on 2025-03-03 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='disciplina',
            name='nota_prova',
        ),
        migrations.AddField(
            model_name='disciplina',
            name='nota_prova1',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Nota da Prova 1'),
        ),
        migrations.AddField(
            model_name='disciplina',
            name='nota_prova2',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True, verbose_name='Nota da Prova 2'),
        ),
    ]
