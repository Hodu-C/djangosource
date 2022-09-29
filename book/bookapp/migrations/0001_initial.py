# Generated by Django 4.1.1 on 2022-09-28 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False, verbose_name='코드')),
                ('title', models.CharField(max_length=200, verbose_name='제목')),
                ('author', models.CharField(max_length=50, verbose_name='저자')),
                ('price', models.IntegerField(verbose_name='가격')),
                ('register_dttm', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
            ],
            options={
                'db_table': 'bookTBL',
            },
        ),
    ]
