# Generated by Django 2.2.6 on 2019-12-09 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floreria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100)),
                ('producto', models.CharField(max_length=100)),
                ('valor', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('total', models.IntegerField()),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='flores',
            name='imagen',
            field=models.ImageField(upload_to='media'),
        ),
    ]
