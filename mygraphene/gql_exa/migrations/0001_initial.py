# Generated by Django 3.0.9 on 2020-08-03 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('population', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('number', models.SmallIntegerField()),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gql_exa.City')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('age', models.IntegerField()),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gql_exa.School')),
            ],
        ),
    ]
