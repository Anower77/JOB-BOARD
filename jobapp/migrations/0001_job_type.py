# Generated by Django 5.1.4 on 2024-12-27 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', 'xxxx_add_initial_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='type',
            field=models.CharField(choices=[('full_time', 'Full Time'), ('part_time', 'Part Time'), ('internship', 'Internship')], default='full_time', max_length=20),
        ),
    ]
