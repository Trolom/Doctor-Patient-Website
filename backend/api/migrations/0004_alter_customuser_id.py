# Generated by Django 5.1.4 on 2025-01-08 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_alter_customuser_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
