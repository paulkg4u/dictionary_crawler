# Generated by Django 2.2.2 on 2019-06-19 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0002_auto_20190619_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worddefinition',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='definitions', to='crawler.Word'),
        ),
    ]
