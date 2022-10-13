# Generated by Django 4.1.1 on 2022-10-13 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0007_question_read_cnt_questioncount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="answer",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="작성날짜"),
        ),
        migrations.AlterField(
            model_name="answer",
            name="modified_at",
            field=models.DateTimeField(auto_now=True, verbose_name="수정날짜"),
        ),
        migrations.AlterField(
            model_name="question",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, verbose_name="작성날짜"),
        ),
        migrations.AlterField(
            model_name="question",
            name="modified_at",
            field=models.DateTimeField(auto_now=True, verbose_name="수정날짜"),
        ),
    ]