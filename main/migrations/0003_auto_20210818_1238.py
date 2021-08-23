# Generated by Django 3.2.5 on 2021-08-18 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_networks'),
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=455)),
                ('description', models.CharField(max_length=455)),
                ('release_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Shows',
        ),
        migrations.RenameModel(
            old_name='Networks',
            new_name='Network',
        ),
        migrations.AddField(
            model_name='show',
            name='network',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shows', to='main.network'),
        ),
    ]
