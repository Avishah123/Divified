# Generated by Django 3.2.4 on 2022-09-25 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20220914_2337'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nse_bse_dividend_alerts',
            options={'ordering': ('-date_announcement',)},
        ),
        migrations.RemoveField(
            model_name='nse_bse_stocks',
            name='stock_ticker',
        ),
        migrations.AddField(
            model_name='nse_bse_stocks',
            name='date_of_listing',
            field=models.CharField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nse_bse_stocks',
            name='face_value',
            field=models.CharField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nse_bse_stocks',
            name='isin_number',
            field=models.CharField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nse_bse_stocks',
            name='market_lot',
            field=models.CharField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nse_bse_stocks',
            name='name_of_company',
            field=models.CharField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nse_bse_stocks',
            name='paid_up_value',
            field=models.CharField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nse_bse_stocks',
            name='series',
            field=models.CharField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nse_bse_stocks',
            name='symbol',
            field=models.CharField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
