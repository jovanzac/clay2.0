# Generated by Django 4.1.3 on 2022-11-25 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0004_remove_user_details_healthcare_centres'),
    ]

    operations = [
        migrations.CreateModel(
            name='PendingPayments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hospital_name', models.CharField(max_length=20)),
                ('desc', models.TextField()),
                ('amt', models.IntegerField()),
                ('due_by', models.DateField()),
                ('user_details', models.ManyToManyField(to='user.user_details')),
            ],
        ),
    ]
