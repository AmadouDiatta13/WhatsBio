# Generated by Django 4.1 on 2022-08-20 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allcourses', '0002_cour_domaine_delete_topic_cour_domaine_cour_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cour',
            name='following',
            field=models.BooleanField(default=False),
        ),
    ]
