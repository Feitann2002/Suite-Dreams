# Generated by Django 5.1.1 on 2024-10-22 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=30, null=True)),
                ('lastname', models.CharField(blank=True, max_length=30, null=True)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('confirm_password', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='user',
            old_name='firstname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
