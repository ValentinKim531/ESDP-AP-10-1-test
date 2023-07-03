# Generated by Django 4.2.2 on 2023-07-01 12:47

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(blank=True, max_length=30, null=True)),
                ('first_name', models.CharField(max_length=30, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, null=True, verbose_name='Фамилия')),
                ('middle_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Отчество')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('about_me', models.TextField(max_length=3000, null=True, verbose_name='Описание')),
                ('occupation', models.TextField(max_length=3000, null=True, verbose_name='Род деятельности')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')),
                ('first_visit_app', models.BooleanField(default=True, verbose_name='Первое посещение приложения')),
                ('likes_qty', models.IntegerField(blank=True, null=True, verbose_name='Количество лайков')),
                ('email', models.EmailField(max_length=254, null=True, unique=True, verbose_name='Электронная почта')),
                ('phone', models.CharField(blank=True, max_length=30, null=True, verbose_name='Номер телефона')),
                ('industries', models.CharField(blank=True, max_length=250, null=True, verbose_name='Отрасли')),
                ('companies', models.CharField(blank=True, max_length=250, null=True, verbose_name='Компании')),
                ('expertise', models.CharField(blank=True, max_length=250, null=True, verbose_name='Экспертиза')),
                ('resources_available', models.CharField(blank=True, max_length=250, null=True, verbose_name='Ресурсы имеющиеся')),
                ('resources_searching', models.CharField(blank=True, max_length=250, null=True, verbose_name='Ресурсы запрашиваемые')),
                ('achievements', models.CharField(blank=True, max_length=250, null=True, verbose_name='Достижения')),
                ('goal_for_the_year', models.CharField(blank=True, max_length=250, null=True, verbose_name='Цель на год')),
                ('request', models.CharField(blank=True, max_length=250, null=True, verbose_name='Запрос')),
                ('hobby', models.CharField(blank=True, max_length=250, null=True, verbose_name='Хобби')),
                ('education', models.CharField(blank=True, max_length=250, null=True, verbose_name='Образование')),
                ('children', models.CharField(blank=True, max_length=50, null=True, verbose_name='Дети')),
                ('facts_about_me', models.CharField(blank=True, max_length=250, null=True, verbose_name='Факты обо мне')),
                ('site', models.CharField(blank=True, max_length=50, null=True, verbose_name='Сайт')),
                ('social_links', models.CharField(blank=True, max_length=250, null=True, verbose_name='Ссылки на социальные сети')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
                'ordering': ['first_name'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='FamilyStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Семейный статус')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Роль')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Cтатус')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, max_length=3000, null=True, verbose_name='Текст отзыва')),
                ('like', models.BooleanField(default=False, null=True, verbose_name='Лайк')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')),
                ('user_receive_review', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews_for_user_receive_review', to=settings.AUTH_USER_MODEL, verbose_name='Отзыв к профилю')),
                ('user_write_review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL, verbose_name='Создатель отзыва')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='RegisterAdminUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin', to=settings.AUTH_USER_MODEL, verbose_name='Администратор')),
                ('resident', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Профиль пользователя')),
            ],
        ),
    ]
