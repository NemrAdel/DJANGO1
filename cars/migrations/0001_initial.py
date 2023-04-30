# Generated by Django 4.1.7 on 2023-04-02 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=15)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(null=True)),
                ('boolean', models.BooleanField(default=True)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]