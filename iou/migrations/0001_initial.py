# Generated by Django 4.0 on 2021-12-14 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debt', models.IntegerField()),
                ('creditor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creditor', to='auth.user')),
                ('debtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debtor', to='auth.user')),
            ],
        ),
    ]
