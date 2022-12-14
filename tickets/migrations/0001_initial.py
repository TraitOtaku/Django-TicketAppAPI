# Generated by Django 4.0.2 on 2022-09-28 20:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name_plural': 'Ticket Categories',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_date', models.DateTimeField(blank=True, null=True)),
                ('is_open', models.BooleanField(default=False)),
                ('is_email', models.BooleanField(default=False)),
                ('complete_by', models.DateField(blank=True, null=True)),
                ('open_details', models.CharField(blank=True, max_length=100, null=True)),
                ('inquiry', models.CharField(max_length=1000)),
                ('respond', models.CharField(max_length=1000)),
                ('is_contact', models.BooleanField(default=False)),
                ('contact_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='category_name', to='tickets.ticketcategory')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='customers.company')),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='customers.customercontact')),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ticket_created_by', to=settings.AUTH_USER_MODEL)),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='customers.store')),
                ('updated_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ticket_updated_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Tickets',
            },
        ),
    ]
