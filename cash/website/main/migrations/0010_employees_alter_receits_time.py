# Generated by Django 5.0.3 on 2024-04-03 12:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0009_shift_finishing_alter_receits_time"),
    ]

    operations = [
        migrations.CreateModel(
            name="Employees",
            fields=[
                (
                    "id",
                    models.AutoField(
                        primary_key=True, serialize=False, verbose_name="id"
                    ),
                ),
                ("nickname", models.FloatField(verbose_name="Nickname")),
                (
                    "Money",
                    models.CharField(max_length=50, verbose_name="Money IN / OUT"),
                ),
                ("receitsCount", models.IntegerField(verbose_name="No of Receits ")),
            ],
            options={
                "verbose_name_plural": "Employees",
            },
        ),
        migrations.AlterField(
            model_name="receits",
            name="time",
            field=models.TimeField(default="14:21:11", verbose_name="Time"),
        ),
    ]
