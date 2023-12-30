# Generated by Django 5.0 on 2023-12-29 21:42

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('subtitulo', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('contenido', models.TextField()),
                ('activo', models.BooleanField(default=True)),
                ('imagenes', models.ImageField(blank=True, default='static/post_default.png', null=True, upload_to='recetas')),
                ('publicado', models.DateTimeField(default=django.utils.timezone.now)),
                ('categoria', models.ForeignKey(default='Sin categoría', null=True, on_delete=django.db.models.deletion.SET_NULL, to='recetas.categoria')),
            ],
            options={
                'ordering': ('-publicado',),
            },
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
                ('categorias', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='recetas.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('usuario', models.CharField(max_length=50)),
                ('noticia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='recetas.receta')),
            ],
        ),
    ]
