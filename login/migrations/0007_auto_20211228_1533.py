# Generated by Django 3.1.7 on 2021-12-28 10:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_auto_20211228_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookdetails',
            name='bookid',
            field=models.TextField(default=uuid.UUID('57680b2f-67c5-11ec-bb54-cb5e2e676fe0'), max_length=16, primary_key=True, serialize=False, unique=True),
        ),
    ]
