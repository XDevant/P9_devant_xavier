# Generated by Django 4.0.4 on 2022-05-19 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_alter_review_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrpheanImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=128)),
            ],
        ),
    ]
