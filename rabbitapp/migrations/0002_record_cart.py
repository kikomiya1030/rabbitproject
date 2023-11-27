# Generated by Django 4.0 on 2023-11-20 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('rabbitapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='購入したアイテム')),
                ('price', models.IntegerField(verbose_name='購入する時の単価')),
                ('qty', models.IntegerField(verbose_name='購入した数量')),
                ('buying_date', models.DateField(auto_now_add=True, verbose_name='購入日')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser', verbose_name='ユーザー')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='購入アイテム')),
                ('price', models.IntegerField(verbose_name='単価')),
                ('qty', models.IntegerField(verbose_name='購入数量')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser', verbose_name='ユーザー')),
            ],
        ),
    ]