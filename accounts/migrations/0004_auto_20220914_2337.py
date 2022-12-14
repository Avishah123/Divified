# Generated by Django 3.2.4 on 2022-09-14 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_ticker_dividend_type_ticker_ex_dividend_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='nse_bse_dividend_alerts',
            name='date_announcement',
            field=models.CharField(default='Not Declared', max_length=254),
        ),
        migrations.AlterField(
            model_name='nse_bse_dividend_alerts',
            name='date_record',
            field=models.CharField(default='Not Declared', max_length=254),
        ),
        migrations.AlterField(
            model_name='nse_bse_dividend_alerts',
            name='dividend_precentage',
            field=models.CharField(default='Not Declared', max_length=254),
        ),
        migrations.AlterField(
            model_name='nse_bse_dividend_alerts',
            name='dividend_type',
            field=models.CharField(default='Not Declared', max_length=254),
        ),
        migrations.AlterField(
            model_name='nse_bse_dividend_alerts',
            name='ex_dividend_date',
            field=models.CharField(default='Not Declared', max_length=254),
        ),
        migrations.AlterField(
            model_name='ticker',
            name='dividend_percetage',
            field=models.CharField(default='Not Declared', max_length=254),
        ),
        migrations.AlterField(
            model_name='ticker',
            name='dividend_type',
            field=models.CharField(default='Not Declared', max_length=254),
        ),
        migrations.AlterField(
            model_name='ticker',
            name='ex_dividend_date',
            field=models.CharField(default='Not Declared', max_length=254),
        ),
        migrations.AlterField(
            model_name='ticker',
            name='stock_announcement_date',
            field=models.CharField(default='Not Declared', max_length=254),
        ),
        migrations.AlterField(
            model_name='ticker',
            name='stock_record_date',
            field=models.CharField(default='Not Declared', max_length=254),
        ),
    ]
