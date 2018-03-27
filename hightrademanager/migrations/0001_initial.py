# Generated by Django 2.0 on 2018-03-27 04:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_value', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('buying_power', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('limit', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('user', models.ForeignKey(on_delete=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('code', models.CharField(db_index=True, max_length=6, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('volatility', models.CharField(choices=[('low', 'low'), ('medium', 'medium'), ('high', 'high')], default=None, max_length=50, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='StockActivityAudit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(choices=[('buy', 'buy'), ('sell', 'sell')], default=None, max_length=50, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('stock', models.ForeignKey(on_delete=True, to='hightrademanager.Stock')),
            ],
        ),
        migrations.CreateModel(
            name='StockPriceHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('stock', models.ForeignKey(on_delete=True, to='hightrademanager.Stock')),
            ],
        ),
    ]
