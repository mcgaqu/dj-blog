# Generated by Django 4.1.1 on 2022-09-14 07:14

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(blank=True, max_length=100, null=True, verbose_name='código')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='nombre')),
                ('grade', models.CharField(blank=True, max_length=50, null=True, verbose_name='clase')),
                ('sort', models.CharField(blank=True, max_length=20, null=True, verbose_name='orden')),
                ('active', models.BooleanField(default=True, verbose_name='activo')),
                ('internal', models.BooleanField(default=False, verbose_name='interno')),
                ('locked', models.BooleanField(default=False, verbose_name='bloqueado')),
                ('replace', models.BooleanField(default=False, verbose_name='reemplaza')),
                ('datet', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='fecha-hora')),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='fecha')),
                ('num_int', models.IntegerField(default=0)),
                ('num_dec', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('mark', models.CharField(blank=True, max_length=250, null=True)),
                ('tags', models.TextField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True, verbose_name='nota')),
                ('json', models.JSONField(blank=True, null=True, verbose_name='valor')),
                ('file', models.FileField(blank=True, null=True, upload_to='', verbose_name='file')),
                ('html', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('level', models.IntegerField(blank=True, default=0, null=True)),
                ('pos', models.CharField(blank=True, max_length=150, null=True)),
                ('root_alias', models.CharField(blank=True, max_length=150, null=True)),
                ('last_alias', models.CharField(blank=True, max_length=150, null=True)),
                ('front', models.CharField(blank=True, max_length=250, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='layouts.component')),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
            options={
                'verbose_name': 'Component',
                'verbose_name_plural': '1. Components',
                'ordering': ['sort'],
                'abstract': False,
                'unique_together': {('site', 'alias')},
            },
        ),
        migrations.CreateModel(
            name='Layout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(blank=True, max_length=100, null=True, verbose_name='código')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='nombre')),
                ('grade', models.CharField(blank=True, max_length=50, null=True, verbose_name='clase')),
                ('sort', models.CharField(blank=True, max_length=20, null=True, verbose_name='orden')),
                ('active', models.BooleanField(default=True, verbose_name='activo')),
                ('internal', models.BooleanField(default=False, verbose_name='interno')),
                ('locked', models.BooleanField(default=False, verbose_name='bloqueado')),
                ('replace', models.BooleanField(default=False, verbose_name='reemplaza')),
                ('datet', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='fecha-hora')),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='fecha')),
                ('num_int', models.IntegerField(default=0)),
                ('num_dec', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('mark', models.CharField(blank=True, max_length=250, null=True)),
                ('tags', models.TextField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True, verbose_name='nota')),
                ('json', models.JSONField(blank=True, null=True, verbose_name='valor')),
                ('file', models.FileField(blank=True, null=True, upload_to='', verbose_name='file')),
                ('html', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('level', models.IntegerField(blank=True, default=0, null=True)),
                ('pos', models.CharField(blank=True, max_length=150, null=True)),
                ('root_alias', models.CharField(blank=True, max_length=150, null=True)),
                ('last_alias', models.CharField(blank=True, max_length=150, null=True)),
                ('front', models.CharField(blank=True, max_length=250, null=True)),
                ('mark_i18n', models.CharField(blank=True, max_length=250, null=True)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('comp', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='layouts.component')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='layouts.layout')),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sites.site')),
            ],
            options={
                'verbose_name': 'Template',
                'verbose_name_plural': '3. Templates',
                'ordering': ('pos',),
                'abstract': False,
                'unique_together': {('site', 'root_alias', 'alias')},
            },
        ),
        migrations.CreateModel(
            name='LayoutI18n',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alias', models.CharField(blank=True, max_length=100, null=True, verbose_name='código')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='nombre')),
                ('grade', models.CharField(blank=True, max_length=50, null=True, verbose_name='clase')),
                ('sort', models.CharField(blank=True, max_length=20, null=True, verbose_name='orden')),
                ('active', models.BooleanField(default=True, verbose_name='activo')),
                ('internal', models.BooleanField(default=False, verbose_name='interno')),
                ('locked', models.BooleanField(default=False, verbose_name='bloqueado')),
                ('replace', models.BooleanField(default=False, verbose_name='reemplaza')),
                ('datet', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='fecha-hora')),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='fecha')),
                ('num_int', models.IntegerField(default=0)),
                ('num_dec', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('mark', models.CharField(blank=True, max_length=250, null=True)),
                ('tags', models.TextField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True, verbose_name='nota')),
                ('json', models.JSONField(blank=True, null=True, verbose_name='valor')),
                ('file', models.FileField(blank=True, null=True, upload_to='', verbose_name='file')),
                ('html', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('layout_root_alias', models.CharField(blank=True, max_length=250, null=True)),
                ('last_alias', models.CharField(blank=True, max_length=50, null=True)),
                ('pos', models.CharField(blank=True, max_length=50, null=True)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('layout', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='layouts.layout')),
            ],
            options={
                'verbose_name': 'Traductor',
                'verbose_name_plural': '4. Traductores',
                'ordering': ('sort',),
                'abstract': False,
                'unique_together': {('layout', 'alias')},
            },
        ),
    ]