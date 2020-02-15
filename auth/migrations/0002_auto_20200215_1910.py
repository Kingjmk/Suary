# Generated by Django 3.0.3 on 2020-02-15 17:10

import _common.utils
import _common.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avatar_url',
        ),
        migrations.AddField(
            model_name='user',
            name='avatar_uuid',
            field=models.CharField(max_length=36, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(db_index=True, editable=False, max_length=128, unique=True, validators=[_common.validators.UsernameValidator]),
        ),
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.CharField(db_index=True, default=_common.utils.generate_uuid, editable=False, max_length=36, primary_key=True, serialize=False),
        ),
    ]
