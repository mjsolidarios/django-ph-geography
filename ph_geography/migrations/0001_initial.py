# Generated by Django 3.1.2 on 2020-10-03 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='Code')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('population', models.PositiveIntegerField(null=True)),
                ('island_group', models.CharField(choices=[('L', 'LUZON'), ('V', 'VISAYAS'), ('M', 'MINDANAO')], max_length=1)),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regions',
            },
        ),
        migrations.CreateModel(
            name='Province',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='Code')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('population', models.PositiveIntegerField(null=True)),
                ('income_class', models.CharField(blank=True, choices=[('1', '1ST'), ('2', '2ND'), ('3', '3RD'), ('4', '4TH'), ('5', '5TH'), ('6', '6TH'), ('S', 'SPECIAL')], max_length=1)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='provinces', related_query_name='province', to='ph_geography.region')),
            ],
            options={
                'verbose_name': 'Province',
                'verbose_name_plural': 'Provinces',
            },
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='Code')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('population', models.PositiveIntegerField(null=True)),
                ('is_city', models.BooleanField()),
                ('is_capital', models.BooleanField()),
                ('city_class', models.CharField(blank=True, choices=[('C', 'CC'), ('I', 'ICC'), ('H', 'HUC')], max_length=1)),
                ('income_class', models.CharField(blank=True, choices=[('1', '1ST'), ('2', '2ND'), ('3', '3RD'), ('4', '4TH'), ('5', '5TH'), ('6', '6TH'), ('S', 'SPECIAL')], max_length=1)),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='municipalities', related_query_name='municipality', to='ph_geography.province')),
            ],
            options={
                'verbose_name': 'Municipality',
                'verbose_name_plural': 'Municipalities',
            },
        ),
        migrations.CreateModel(
            name='Barangay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='Code')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('population', models.PositiveIntegerField(null=True)),
                ('is_urban', models.BooleanField(null=True)),
                ('municipality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='barangays', related_query_name='barangays', to='ph_geography.municipality')),
            ],
            options={
                'verbose_name': 'Barangay',
                'verbose_name_plural': 'Barangays',
            },
        ),
    ]