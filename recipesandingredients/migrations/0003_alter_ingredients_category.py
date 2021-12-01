# Generated by Django 3.2.6 on 2021-09-01 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipesandingredients', '0002_alter_ingredients_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredients',
            name='category',
            field=models.CharField(blank=True, choices=[('Food', 'Food'), ('Labor', 'Labor'), ('Packaging', 'Packaging'), ('UnCategorized', 'UnCategorized')], max_length=225, null=True),
        ),
    ]