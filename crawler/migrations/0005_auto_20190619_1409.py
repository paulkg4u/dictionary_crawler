# Generated by Django 2.2.2 on 2019-06-19 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0004_auto_20190619_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translation',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='crawler.Word'),
        ),
        migrations.AlterField(
            model_name='worddefinition',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='definitions', to='crawler.Word'),
        ),
    ]
