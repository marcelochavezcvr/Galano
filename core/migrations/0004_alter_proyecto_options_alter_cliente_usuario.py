# Generated by Django 5.1.3 on 2024-11-18 08:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_user_rol'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proyecto',
            options={'ordering': ['-created_at'], 'verbose_name': 'Proyecto', 'verbose_name_plural': 'Proyectos'},
        ),
        migrations.AlterField(
            model_name='cliente',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clientes', to=settings.AUTH_USER_MODEL),
        ),
    ]
