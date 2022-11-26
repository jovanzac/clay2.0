# Generated by Django 4.1.3 on 2022-11-25 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0004_remove_user_details_healthcare_centres'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
                ('doctor', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user_details')),
            ],
        ),
    ]
