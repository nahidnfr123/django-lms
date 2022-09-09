# Generated by Django 4.1 on 2022-09-09 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('status', models.BooleanField(default=True)),
                ('type', models.CharField(choices=[('note', 'Note'), ('live_class', 'Live Class'), ('recorded_class', 'Recorded Class'), ('exam', 'Exam'), ('assignment', 'Assignment')], max_length=30, null=True)),
                ('available_at', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('instruction', models.TextField(null=True)),
                ('duration', models.IntegerField()),
                ('total_marks', models.IntegerField(null=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('subtitle', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(null=True, upload_to='uploads/course')),
                ('status', models.BooleanField(default=True)),
                ('featured', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discounted_price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('available_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Student')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('status', models.BooleanField(default=True)),
                ('type', models.CharField(choices=[('note', 'Note'), ('live_class', 'Live Class'), ('recorded_class', 'Recorded Class'), ('exam', 'Exam'), ('assignment', 'Assignment')], max_length=30, null=True)),
                ('available_at', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('total_marks', models.IntegerField()),
                ('total_questions', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('result_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('status', models.BooleanField(default=True)),
                ('description', models.TextField(null=True)),
                ('available_at', models.DateTimeField(auto_now_add=True)),
                ('order', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
            ],
            options={
                'ordering': ['-order', '-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.IntegerField(null=True)),
                ('start_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('end_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('total_marks', models.IntegerField(null=True)),
                ('obtained_marks', models.DecimalField(decimal_places=2, max_digits=10)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.exam')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RecordedClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('status', models.BooleanField(default=True)),
                ('type', models.CharField(choices=[('note', 'Note'), ('live_class', 'Live Class'), ('recorded_class', 'Recorded Class'), ('exam', 'Exam'), ('assignment', 'Assignment')], max_length=30, null=True)),
                ('available_at', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('link', models.CharField(max_length=200)),
                ('source', models.CharField(max_length=200)),
                ('duration', models.IntegerField()),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.section')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('status', models.BooleanField(default=True)),
                ('type', models.CharField(choices=[('note', 'Note'), ('live_class', 'Live Class'), ('recorded_class', 'Recorded Class'), ('exam', 'Exam'), ('assignment', 'Assignment')], max_length=30, null=True)),
                ('available_at', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('note', models.TextField(null=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.section')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mcq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('question_image', models.ImageField(null=True, upload_to='uploads/mcq')),
                ('a', models.CharField(max_length=200)),
                ('b', models.CharField(max_length=200)),
                ('c', models.CharField(max_length=200)),
                ('d', models.CharField(max_length=200)),
                ('e', models.CharField(max_length=200)),
                ('mark', models.IntegerField(default=1)),
                ('answer', models.CharField(max_length=200)),
                ('answer_image', models.ImageField(null=True, upload_to='uploads/mcq')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.exam')),
                ('student', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LiveClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('status', models.BooleanField(default=True)),
                ('type', models.CharField(choices=[('note', 'Note'), ('live_class', 'Live Class'), ('recorded_class', 'Recorded Class'), ('exam', 'Exam'), ('assignment', 'Assignment')], max_length=30, null=True)),
                ('available_at', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(auto_now=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('link', models.CharField(max_length=200)),
                ('source', models.CharField(choices=[('google_meet', 'Google Meet'), ('zoom', 'Zoom'), ('facebook_live', 'Facebook Live')], max_length=200)),
                ('duration', models.IntegerField()),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.section')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='exam',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.section'),
        ),
        migrations.CreateModel(
            name='AssignmentSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submission_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('total_marks', models.IntegerField(null=True)),
                ('obtained_marks', models.DecimalField(decimal_places=2, max_digits=10)),
                ('file', models.FileField(blank=True, upload_to='uploads/assignment/', verbose_name='Assignment File')),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.assignment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.section'),
        ),
    ]
