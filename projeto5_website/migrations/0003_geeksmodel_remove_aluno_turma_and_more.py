# Generated by Django 4.0.4 on 2022-05-17 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto5_website', '0002_alternativa_pergunta'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeeksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.RemoveField(
            model_name='aluno',
            name='turma',
        ),
        migrations.AlterField(
            model_name='alternativa',
            name='conteudo',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='alternativa',
            name='perfil',
            field=models.IntegerField(choices=[(1, 'dominancia'), (2, 'influencia'), (3, 'cautela'), (4, 'estabilidade')]),
        ),
    ]
