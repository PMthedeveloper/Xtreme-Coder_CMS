# Generated by Django 3.0.4 on 2020-05-09 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='rating',
            field=models.CharField(choices=[('b', 'Bad'), ('a', 'Average'), ('e', 'Excellent')], default='a', max_length=1),
            preserve_default=False,
        ),
    ]