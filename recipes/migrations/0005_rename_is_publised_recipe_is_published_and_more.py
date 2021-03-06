# Generated by Django 4.0.2 on 2022-02-15 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_recipe_preparation_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='is_publised',
            new_name='is_published',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cover',
            field=models.ImageField(blank=True, default='', upload_to='recipes/covers/%Y/%m/%d/'),
        ),
    ]
