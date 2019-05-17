# Generated by Django 2.2.1 on 2019-05-11 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200, verbose_name='Вид связи')),
                ('direct', models.CharField(max_length=200, verbose_name='Прямое')),
                ('inverse', models.CharField(max_length=200, verbose_name='Обратное')),
                ('relative', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Вид отношении',
                'verbose_name_plural': 'Виды отношений',
                'ordering': ['type'],
            },
        ),
        migrations.CreateModel(
            name='ContactType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_contact', models.CharField(max_length=200, verbose_name='Тип контакта')),
                ('remarks', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Тип контакт',
                'verbose_name_plural': 'Виды контакта',
                'ordering': ['type_contact'],
            },
        ),
        migrations.CreateModel(
            name='Criminals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(verbose_name='Уровень доступа')),
                ('first_name', models.CharField(max_length=200, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=200, verbose_name='Отчетство')),
                ('birthday', models.DateField(blank=True, verbose_name='Дата рождение')),
                ('gender', models.CharField(choices=[('N', 'Не указан'), ('M', 'Мужской'), ('F', 'Женский')], max_length=1, verbose_name='Пол')),
                ('citizenship', models.CharField(default='Не указан', max_length=200, verbose_name='Гражданство')),
                ('INN', models.CharField(max_length=14, verbose_name='ПИН')),
                ('passport_serial', models.CharField(max_length=2, verbose_name='Серия паспорта')),
                ('passport_number', models.CharField(max_length=7, verbose_name='Номер паспорта')),
                ('issue_organ', models.CharField(max_length=200, verbose_name='Место выдачи')),
                ('issue_data', models.DateField(verbose_name='Дата выдачи')),
                ('education', models.CharField(choices=[('NS', 'Не указан'), ('NOT', 'Нет образование'), ('PGE', 'Начальное общее образование'), ('BGE', 'Основное общее образование'), ('SGE', 'Среднее общее образование'), ('SVE', 'Среднее профессиональное образование'), ('HEB', 'Высшее образование - бакалавриат'), ('HES', 'Высшее образование - специалитет, магистратура'), ('HET', 'Высшее образование - подготовка кадров высшей квалификации')], default='NS', max_length=3, verbose_name='Образование')),
                ('education_place', models.CharField(max_length=200, verbose_name='Место образование')),
                ('profession', models.CharField(default='Нет профессии', max_length=200, null=True, verbose_name='Профессия')),
                ('job', models.CharField(default='Не указан', max_length=200, verbose_name='Работа')),
                ('workplace', models.CharField(default='Не указан', max_length=200, null=True, verbose_name='Место работы')),
                ('marital_status', models.CharField(choices=[('N', 'Не указан'), ('SB', 'Холост'), ('SG', 'Незамужем'), ('MB', 'Женат'), ('MG', 'Замужен'), ('D', 'Разведен(а)')], default='N', max_length=2, verbose_name='Семейное положение')),
                ('health_information', models.TextField(blank=True, verbose_name='Информация о здоровье')),
                ('hobby', models.CharField(blank=True, max_length=200, verbose_name='Хобби и увлечения')),
                ('status', models.CharField(choices=[('N', 'Неизвестно'), ('D', 'Мертв'), ('L', 'Жив')], default='N', max_length=1, verbose_name='Статус')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/criminals/', verbose_name='Фото')),
                ('user', models.CharField(max_length=200, verbose_name='Создал')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Дата создание')),
                ('remarks', models.TextField(blank=True, verbose_name='Примечание')),
                ('birth_City', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='address.City', verbose_name='Город')),
                ('birth_District', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='address.District', verbose_name='Район')),
                ('birth_Village', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='address.Village', verbose_name='Село')),
                ('birth_country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='address.Country', verbose_name='Страна рождения')),
                ('birth_region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='address.Region', verbose_name='Область')),
            ],
            options={
                'verbose_name': 'Террориста или экстремиста',
                'verbose_name_plural': 'Террористы и экстремисти',
                'ordering': ['last_name', 'first_name', 'patronymic'],
            },
        ),
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_occ', models.CharField(max_length=40, verbose_name='Тип деятельности')),
                ('occ_abbr', models.CharField(max_length=40, verbose_name='Аббревиатура')),
                ('remarks', models.TextField(verbose_name='Примечание')),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Тип деятельности',
            },
        ),
        migrations.CreateModel(
            name='Organizations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название организации')),
                ('occupation', models.CharField(choices=[('NS', 'Неизвестно'), ('MTO', 'МТО'), ('MEO', 'МЭО')], max_length=3, verbose_name='Тип организации')),
                ('leader', models.CharField(blank=True, max_length=200, verbose_name='Лидер организации')),
                ('ideology', models.CharField(blank=True, max_length=200, verbose_name='Идеология организации')),
                ('foundation_year', models.CharField(blank=True, default='Неизвестно', max_length=20, verbose_name='Год осование')),
                ('remarks', models.TextField(blank=True, null=True, verbose_name='Примечание')),
            ],
            options={
                'verbose_name': 'Организация',
                'verbose_name_plural': 'Запрещенные организации',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='RelativeRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200, verbose_name='Вид связи')),
                ('direct', models.CharField(max_length=200, verbose_name='Прямое')),
                ('inverse', models.CharField(max_length=200, verbose_name='Обратное')),
                ('relative', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Вид родственног отношении',
                'verbose_name_plural': 'Виды родственных отношений',
                'ordering': ['type'],
            },
        ),
        migrations.CreateModel(
            name='Persons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField(verbose_name='Уровень доступа')),
                ('first_name', models.CharField(max_length=200, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=200, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=200, verbose_name='Отчетство')),
                ('birthday', models.DateField(blank=True, verbose_name='Дата рождение')),
                ('gender', models.CharField(choices=[('N', 'Не указан'), ('M', 'Мужской'), ('F', 'Женский')], max_length=1, verbose_name='Пол')),
                ('citizenship', models.CharField(default='Не указан', max_length=200, verbose_name='Гражданство')),
                ('INN', models.CharField(max_length=14, verbose_name='ПИН')),
                ('passport_serial', models.CharField(max_length=2, verbose_name='Серия паспорта')),
                ('passport_number', models.CharField(max_length=7, verbose_name='Номер паспорта')),
                ('issue_organ', models.CharField(max_length=200, verbose_name='Место выдачи')),
                ('issue_data', models.DateField(verbose_name='Дата выдачи')),
                ('education', models.CharField(choices=[('NS', 'Не указан'), ('NOT', 'Нет образование'), ('PGE', 'Начальное общее образование'), ('BGE', 'Основное общее образование'), ('SGE', 'Среднее общее образование'), ('SVE', 'Среднее профессиональное образование'), ('HEB', 'Высшее образование - бакалавриат'), ('HES', 'Высшее образование - специалитет, магистратура'), ('HET', 'Высшее образование - подготовка кадров высшей квалификации')], default='NS', max_length=3, verbose_name='Образование')),
                ('education_place', models.CharField(max_length=200, verbose_name='Место образование')),
                ('profession', models.CharField(default='Нет профессии', max_length=200, null=True, verbose_name='Профессия')),
                ('job', models.CharField(default='Не указан', max_length=200, verbose_name='Работа')),
                ('workplace', models.CharField(default='Не указан', max_length=200, null=True, verbose_name='Место работы')),
                ('marital_status', models.CharField(choices=[('N', 'Не указан'), ('SB', 'Холост'), ('SG', 'Незамужем'), ('MB', 'Женат'), ('MG', 'Замужен'), ('D', 'Разведен(а)')], default='N', max_length=2, verbose_name='Семейное положение')),
                ('phone', models.CharField(blank=True, max_length=40, null=True, verbose_name='Номер телефона')),
                ('email', models.CharField(blank=True, max_length=200, null=True, verbose_name='Электронная почта')),
                ('health_information', models.TextField(blank=True, verbose_name='Информация о здоровье')),
                ('hobby', models.CharField(blank=True, max_length=200, verbose_name='Хобби и увлечения')),
                ('status', models.CharField(choices=[('N', 'Неизвестно'), ('D', 'Мертв'), ('L', 'Жив')], default='N', max_length=1, verbose_name='Статус')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/persons/', verbose_name='Фото')),
                ('user', models.CharField(max_length=200, verbose_name='Создал')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Дата создание')),
                ('remarks', models.TextField(blank=True, verbose_name='Примечание')),
                ('birth_City', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='address.City', verbose_name='Город')),
                ('birth_District', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='address.District', verbose_name='Район')),
                ('birth_Village', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='address.Village', verbose_name='Село')),
                ('birth_country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='address.Country', verbose_name='Страна рождения')),
                ('birth_region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='address.Region', verbose_name='Область')),
            ],
            options={
                'verbose_name': 'Персона',
                'verbose_name_plural': 'Люди',
                'ordering': ['last_name', 'first_name', 'patronymic'],
            },
        ),
        migrations.CreateModel(
            name='PersonAddresses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(choices=[('residence', 'Место проживание'), ('registration', 'Место прориски')], default='registration', max_length=20, verbose_name='Тип адреса')),
                ('micro_district', models.CharField(blank=True, max_length=200, null=True, verbose_name='Микрорайон/Жил.массив')),
                ('street', models.CharField(blank=True, max_length=200, null=True, verbose_name='Улица')),
                ('home', models.CharField(blank=True, max_length=200, null=True, verbose_name='Дом')),
                ('date_entry', models.DateField(null=True, verbose_name='Дата входа')),
                ('date_release', models.DateField(null=True, verbose_name='Дата выхода')),
                ('remarks', models.TextField(blank=True, verbose_name='Примечание')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='address.City', verbose_name='Город')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='address.District', verbose_name='Район')),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.Persons', verbose_name='ФИО')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='address.Region', verbose_name='Регион')),
                ('village', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='address.Village', verbose_name='Село')),
            ],
            options={
                'verbose_name': 'Адресс Родственника и контактируемого лица',
                'verbose_name_plural': 'Адреса Родственников и контактируемых лиц',
                'ordering': ['person_id'],
            },
        ),
        migrations.CreateModel(
            name='CriminalsActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_begin', models.DateField(verbose_name='Дата начало')),
                ('date_end', models.DateField(verbose_name='Дата конец')),
                ('criminal_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.Criminals', verbose_name='ФИО')),
            ],
            options={
                'verbose_name': 'Активность человека',
                'verbose_name_plural': 'Активность человека',
                'ordering': ['criminal_id'],
            },
        ),
        migrations.AddField(
            model_name='criminals',
            name='occupation',
            field=models.ManyToManyField(related_name='persons', to='persons.Occupation', verbose_name='Деятелльность'),
        ),
        migrations.AddField(
            model_name='criminals',
            name='organizations',
            field=models.ManyToManyField(blank=True, related_name='members', to='persons.Organizations', verbose_name='Организации'),
        ),
        migrations.CreateModel(
            name='CriminalAddresses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(choices=[('residence', 'Место проживание'), ('registration', 'Место прориски')], default='registration', max_length=20, verbose_name='Тип адреса')),
                ('micro_district', models.CharField(blank=True, max_length=200, null=True, verbose_name='Микрорайон/Жил.массив')),
                ('street', models.CharField(blank=True, max_length=200, null=True, verbose_name='Улица')),
                ('home', models.CharField(blank=True, max_length=200, null=True, verbose_name='Дом')),
                ('date_entry', models.DateField(null=True, verbose_name='Дата входа')),
                ('date_release', models.DateField(null=True, verbose_name='Дата выхода')),
                ('remarks', models.TextField(blank=True, verbose_name='Примечание')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='address.City', verbose_name='Город')),
                ('criminal_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.Criminals', verbose_name='ФИО')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='address.District', verbose_name='Район')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='address.Region', verbose_name='Регион')),
                ('village', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='address.Village', verbose_name='Село')),
            ],
            options={
                'verbose_name': 'Адресс террориста и экстремиста',
                'verbose_name_plural': 'Адреса террористов и экстремистов',
                'ordering': ['criminal_id'],
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=200, verbose_name='Контакт')),
                ('remarks', models.TextField(verbose_name='Примечание')),
                ('criminal_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.Criminals', verbose_name='ФИО')),
                ('type_contact', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='persons.ContactType', verbose_name='Тип контакта')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
                'ordering': ['criminal_id'],
            },
        ),
    ]
