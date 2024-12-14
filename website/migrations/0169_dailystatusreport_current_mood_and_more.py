# Generated by Django 5.1.3 on 2024-12-13 20:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0168_add_streak_badges"),
    ]

    operations = [
        migrations.AddField(
            model_name="dailystatusreport",
            name="current_mood",
            field=models.CharField(default="Happy 😊", max_length=50),
        ),
        migrations.AddField(
            model_name="dailystatusreport",
            name="goal_accomplished",
            field=models.BooleanField(default=False),
        ),
    ]
