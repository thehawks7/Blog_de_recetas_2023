# Generated by Django 5.0 on 2023-12-28 20:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='texto',
            new_name='contenido',
        ),
        migrations.RemoveField(
            model_name='post',
            name='imagen',
        ),
        migrations.AddField(
            model_name='post',
            name='imagenes',
            field=models.ImageField(blank=True, default='static/post_default.png', null=True, upload_to='recetas'),
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('subtitulo', models.CharField(blank=True, max_length=100, null=True)),
                ('resumen', models.CharField(max_length=200, null=True)),
                ('texto', models.TextField()),
                ('imagenes', models.ImageField(upload_to='recetas')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('categorias', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recetas.categoria')),
            ],
        ),
    ]
