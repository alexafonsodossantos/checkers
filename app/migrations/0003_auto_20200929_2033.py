# Generated by Django 3.1.1 on 2020-09-29 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200929_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='id',
        ),
        migrations.AddField(
            model_name='pizza',
            name='cod_pizza',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pizza',
            name='sabor',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
