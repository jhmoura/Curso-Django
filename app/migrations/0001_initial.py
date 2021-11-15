# Generated by Django 3.2.9 on 2021-11-15 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Preço')),
                ('estoque', models.IntegerField(verbose_name='Quantidade em estoque')),
            ],
        ),
    ]