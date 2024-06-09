# Generated by Django 5.0.6 on 2024-06-08 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processedresults',
            name='mode_value',
        ),
        migrations.AddField(
            model_name='processedresults',
            name='std_value',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='processedresults',
            name='column_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='processedresults',
            name='mean_value',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='processedresults',
            name='median_value',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
