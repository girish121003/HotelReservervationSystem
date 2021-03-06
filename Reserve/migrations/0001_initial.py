# Generated by Django 2.0.6 on 2018-07-27 02:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('adminid', models.AutoField(db_column='AdminID', primary_key=True, serialize=False)),
                ('adminname', models.CharField(db_column='AdminName', default='giru', max_length=50, verbose_name='Name')),
            ],
            options={
                'db_table': 'Admin',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('billid', models.AutoField(db_column='BillID', primary_key=True, serialize=False)),
                ('total', models.CharField(blank=True, db_column='Total', max_length=10, null=True)),
            ],
            options={
                'db_table': 'Bill',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Billpay',
            fields=[
                ('billpayid', models.AutoField(db_column='BillPayID', primary_key=True, serialize=False)),
                ('dateid', models.DateTimeField(blank=True, db_column='DateId', null=True)),
                ('billid', models.ForeignKey(blank=True, db_column='BillId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Reserve.Bill')),
            ],
            options={
                'db_table': 'BillPay',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('bookingid', models.AutoField(db_column='BookingID', primary_key=True, serialize=False)),
                ('cin_date', models.DateTimeField(blank=True, db_column='CIN_Date', null=True, verbose_name='Check-In Date')),
                ('cout_date', models.DateTimeField(blank=True, db_column='COUT_Date', null=True, verbose_name='Check-Out Date')),
                ('admin', models.ForeignKey(db_column='Admin_ID', default='1', on_delete=django.db.models.deletion.DO_NOTHING, to='Reserve.Admin')),
            ],
            options={
                'db_table': 'Booking',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(db_column='Customer_ID', primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, db_column='First_Name', max_length=30, null=True, verbose_name='First')),
                ('last_name', models.CharField(blank=True, db_column='Last_Name', max_length=30, null=True, verbose_name='Last')),
            ],
            options={
                'db_table': 'Customer',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Paytype',
            fields=[
                ('payid', models.AutoField(db_column='PayID', primary_key=True, serialize=False)),
                ('ptype', models.CharField(db_column='PType', max_length=50)),
            ],
            options={
                'db_table': 'PayType',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('ratingid', models.AutoField(db_column='RatingID', primary_key=True, serialize=False)),
                ('rat_description', models.CharField(blank=True, db_column='Rat_Description', max_length=100, null=True, verbose_name='Ratings')),
            ],
            options={
                'db_table': 'Ratings',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('rentid', models.AutoField(db_column='RentID', primary_key=True, serialize=False)),
                ('account', models.CharField(blank=True, db_column='Account', max_length=1, null=True)),
                ('from_date', models.DateTimeField(blank=True, db_column='From_Date', null=True, verbose_name='Check-In Date')),
                ('to_date', models.DateTimeField(blank=True, db_column='To_Date', null=True, verbose_name='Check-Out Date')),
                ('isactive', models.NullBooleanField(db_column='ISactive')),
            ],
            options={
                'db_table': 'Rent',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('roomid', models.AutoField(db_column='RoomID', primary_key=True, serialize=False)),
                ('is_reserved', models.NullBooleanField(db_column='IS_Reserved')),
            ],
            options={
                'db_table': 'ROOM',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Roomratings',
            fields=[
                ('roomratingid', models.AutoField(db_column='RoomRatingID', primary_key=True, serialize=False)),
                ('from_date', models.DateTimeField(blank=True, db_column='From_Date', null=True, verbose_name='Check-In Date')),
                ('to_date', models.DateTimeField(blank=True, db_column='To_Date', null=True, verbose_name='Check-Out Date')),
                ('isactive', models.NullBooleanField(db_column='ISactive')),
                ('r_code', models.ForeignKey(blank=True, db_column='R_Code', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Reserve.Ratings')),
                ('roomno', models.ForeignKey(blank=True, db_column='RoomNo', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Reserve.Room')),
            ],
            options={
                'db_table': 'RoomRatings',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Roomtype',
            fields=[
                ('roomtypeid', models.AutoField(db_column='RoomTypeID', primary_key=True, serialize=False)),
                ('roomtype', models.CharField(blank=True, db_column='RoomType', default='Single', max_length=20, null=True, verbose_name='Type')),
            ],
            options={
                'db_table': 'RoomType',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SignUpUser',
            fields=[
                ('user_id', models.AutoField(db_column='UserId', primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, db_column='FirstName', max_length=30, null=True)),
                ('last_name', models.CharField(blank=True, db_column='LastName', max_length=30, null=True)),
                ('email', models.EmailField(db_column='Email', max_length=254)),
                ('username', models.CharField(db_column='UserName', max_length=20)),
            ],
            options={
                'db_table': 'signup',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_site', models.URLField(blank=True)),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Login',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='room',
            name='roomtype',
            field=models.ForeignKey(db_column='RoomType', default='Single', on_delete=django.db.models.deletion.DO_NOTHING, to='Reserve.Roomtype', verbose_name='Room Type'),
        ),
        migrations.AddField(
            model_name='rent',
            name='roomtypeid',
            field=models.ForeignKey(blank=True, db_column='RoomTypeID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Reserve.Roomtype'),
        ),
        migrations.AddField(
            model_name='booking',
            name='customer',
            field=models.ForeignKey(db_column='Customer_ID', default='1', on_delete=django.db.models.deletion.DO_NOTHING, to='Reserve.Customer'),
        ),
        migrations.AddField(
            model_name='billpay',
            name='paytypeid',
            field=models.ForeignKey(blank=True, db_column='PaytypeId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Reserve.Paytype', verbose_name='Type'),
        ),
        migrations.AddField(
            model_name='bill',
            name='rentid',
            field=models.ForeignKey(blank=True, db_column='RentId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Reserve.Rent'),
        ),
        migrations.AddField(
            model_name='bill',
            name='resid',
            field=models.ForeignKey(blank=True, db_column='ResID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Reserve.Booking'),
        ),
    ]
