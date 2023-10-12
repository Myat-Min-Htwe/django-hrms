# Generated by Django 4.2.3 on 2023-09-30 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('pay_date', models.DateField()),
                ('base_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('overtime', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bonus', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paystub', models.ImageField(blank=True, default=None, upload_to='')),
            ],
        ),
    ]