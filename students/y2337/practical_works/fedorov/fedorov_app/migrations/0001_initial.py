# Generated by Django 3.0.3 on 2020-03-13 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.CharField(max_length=9, primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=30)),
                ('provider', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('second_name', models.CharField(max_length=30)),
                ('birthday', models.DateField()),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='OwnerShip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField()),
                ('finish', models.DateField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fedorov_app.Car')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fedorov_app.Owner')),
            ],
        ),
        migrations.CreateModel(
            name='CarLicense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fedorov_app.Owner')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='car',
            field=models.ManyToManyField(through='fedorov_app.OwnerShip', to='fedorov_app.Owner'),
        ),
    ]
