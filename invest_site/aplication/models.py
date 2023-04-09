from django.db import models


class Categories(models.Model):
    title = models.CharField(max_length=50,
                             verbose_name='Направление')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f"{self.title}"



class Aplication(models.Model):
    MATRIAL_CHOICES = (
        ('ye', 'Женат/Замужем'),
        ('no', 'Холост/Не замужем'),
    )
    last_name = models.CharField(max_length=100,
                                 verbose_name='Фамилия')
    first_name = models.CharField(max_length=100,
                                  verbose_name='Имя')
    parent_name = models.CharField(max_length=100,
                                   verbose_name='Отчество')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    marital_status = models.CharField(max_length=2,
                                      choices=MATRIAL_CHOICES,
                                      default='ye',
                                      verbose_name='Семейное положение')
    children = models.CharField(max_length=255,
                                default="Нет",
                                verbose_name='Дети')
    registration_address = models.CharField(max_length=300,
                                            verbose_name='Адрес регистрации')
    residential_address = models.CharField(max_length=300,
                                           verbose_name='Адрес проживания')
    mobile_phone = models.CharField(max_length=11,
                                    verbose_name='Мобильный телефон')
    home_phone = models.CharField(default="Нет",
                                  max_length=15,
                                  verbose_name='Домашний телефон')
    email_address = models.EmailField(verbose_name='Электронная почта')
    # direction_of_the_appeal = models.ForeignKey('DirectionOfTheAppeal', on_delete=models.CASCADE)
    # higher_education = models.ForeignKey('HigherEducation', on_delete=models.CASCADE)
    average_perfomance = models.FloatField(verbose_name='Средний балл успеваемости',
                                           blank=True, null=True)
    academic_degrees = models.CharField(max_length=300,
                                        verbose_name='Ученые степени, звания',
                                        blank=True, null=True)
    training_courses = models.CharField(max_length=300,
                                        verbose_name='Курсы повышения квалификации',
                                        blank=True, null=True)
    professional_skills = models.TextField(verbose_name='Профессиональные навыки',
                                           blank=True, null=True)
    software = models.CharField(max_length=500,
                                verbose_name='ПО, которым владеете',
                                blank=True, null=True)
    # foreign_languages = models.ForeignKey('ForeignLanguages', on_delete=models.CASCADE)
    # enterprises = models.ForeignKey('Enterprises', on_delete=models.CASCADE)
    FIO = models.CharField(max_length=150,
                           verbose_name="ФИО рекомендатора",
                           blank=True, null=True)
    work_place = models.CharField(max_length=100,
                                  verbose_name='Место работы рекомендатора',
                                  blank=True, null=True)
    position_of_recom = models.CharField(max_length=200,
                                         verbose_name='Должность рекомендатора',
                                         blank=True, null=True)
    phone_of_recom = models.CharField(max_length=12,
                                      verbose_name='Телефон рекомендатора',
                                      blank=True, null=True)
    # family_remember = models.ForeignKey('FamilyRemember', on_delete=models.CASCADE)
    comment = models.CharField(max_length=200,
                               verbose_name='Комментарий',
                               blank=True, null=True)
    passed_the_questionnaire = models.BooleanField(verbose_name='Прошел анкету', default='True')
    test_result = models.CharField(max_length=10,
                                   verbose_name="Результат теста",
                                   blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Клиенты'
        verbose_name_plural = "Клиенты"



class FamilyRemember(models.Model):
    family_remember = models.ForeignKey('Aplication', on_delete=models.CASCADE)
    pos_in_family = models.CharField(max_length=40,
                                     verbose_name='Член семьи')
    FIO = models.CharField(max_length=150,
                           verbose_name='ФИО')
    date_of_birth_fanily = models.DateField(verbose_name='Дата рождения')
    place_of_work = models.CharField(max_length=100,
                                     verbose_name='Место работы')

    def __str__(self):
        return f"{self.FIO}"

    class Meta:
        verbose_name = 'Члены семьи'
        verbose_name_plural = "Члены семьи"


class Enterprises(models.Model):
    enterprises = models.ForeignKey('Aplication', on_delete=models.CASCADE)
    title_ent = models.CharField(max_length=100,
                                 verbose_name='Название предприятния')
    date_of_dismissal = models.DateField(verbose_name='Дата увольнения')
    post_ent = models.CharField(max_length=100,
                                verbose_name='Должность')
    responsibilities = models.TextField(verbose_name='Обязанности')
    reason_of_leaving = models.CharField(max_length=150,
                                         verbose_name='Причина ухода')

    def __str__(self):
        return f"{self.title_ent}"

    class Meta:
        verbose_name = 'Предприятия'
        verbose_name_plural = "Предприятия"


class ForeignLanguages(models.Model):
    foreign_languages = models.ForeignKey('Aplication', on_delete=models.CASCADE)
    PROFICIENCY_LEVEL_CHOICES = (
        ('св', "Свободно"),
        ('рз', "Разговорный"),
        ('чп', 'Читаю/Пишу'),
        ("чс", 'Читаю/Пишу со словарем')
    )
    title = models.CharField(max_length=100,
                             verbose_name='Название')
    proficiency_level = models.CharField(max_length=2,
                                         choices=PROFICIENCY_LEVEL_CHOICES,
                                         default='св',
                                         verbose_name='Уровень владения')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Иностранные языки'
        verbose_name_plural = "Иностранные языки"


class HigherEducation(models.Model):
    FORM_OF_TRAINIG = (
        ('dn', 'Очная(Дневная)'),
        ('vc', 'Очная(Вечерняя)'),
        ('za', 'Заочная')
    )
    higher_education = models.ForeignKey('Aplication', on_delete=models.CASCADE)
    name_of_the_university = models.CharField(max_length=150,
                                              verbose_name='Название ВУЗа')
    year_of_entry = models.CharField(max_length=4,
                                     verbose_name='Год поступления')
    year_of_graduation = models.CharField(max_length=4,
                                          verbose_name='Год окончания')
    faculty = models.CharField(max_length=100,
                               blank=True, null=True,
                               verbose_name='Факультет')
    specialization = models.CharField(max_length=100,
                                      verbose_name='Специальность')
    form_of_training = models.CharField(max_length=2,
                                        choices=FORM_OF_TRAINIG,
                                        default='dn',
                                        verbose_name='Форма обученя')

    def __str__(self):
        return f"{self.name_of_the_university}"

    class Meta:
        verbose_name = 'Высшее образование'
        verbose_name_plural = "Высшее образование"


class DirectionOfTheAppeal(models.Model):
    direction_of_the_appeal = models.ForeignKey('Aplication', on_delete=models.CASCADE)
    PURPOSE_CHOICE = (
        ('pr', 'Практика'),
        ('ed', 'Обучение/Стажировка'),
        ('wk', 'Работа')
    )
    DESIRED_CHOICE = (
        ('РО', "Ростовская область"),
        ("КК", "Краснодарский край"),
        ('СТ', "Ставропольский край"),
        ('ВО', 'Волгоградская область'),
        ("МО", 'Москва'),
        ("НН", 'Нижний новгород')
    )
    purpose = models.CharField(max_length=100,
                               choices=PURPOSE_CHOICE,
                               verbose_name='Цель обращения',
                               default='pr')
    desired_region = models.CharField(max_length=2,
                                      choices=DESIRED_CHOICE,
                                      verbose_name='Желаемый регион',
                                      default='РО')
    date_with = models.DateField(blank=True, null=True,
                                 verbose_name='С')
    date_before = models.DateField(blank=True, null=True,
                                   verbose_name='До')
    working_in_bank = models.BooleanField(verbose_name='Хочет работать в банке')
    desired_direction = models.ManyToManyField('DesiredDirection',
                                               verbose_name='Желаемое направление работы',
                                               # default=lambda: [DesiredDirection.objects.get(direction='пока не определился(-лась)')]
                                               )
    expectations = models.CharField(verbose_name='Ваши ожидания от работы в Банке',
                                    blank=True, null=True, max_length=150)
    removal = models.BooleanField(default=False,
                                  verbose_name='Готовность перехать')
    documents_before = models.BooleanField(verbose_name='Подавал ранее')
    results_of_documents = models.CharField(max_length=255,
                                            verbose_name='Результат подачи',
                                            blank=True, null=True)

    def __str__(self):
        return f"{self.purpose}"


    class Meta:
        verbose_name = 'Направление обращения'
        verbose_name_plural = "Направление обращения"


class DesiredDirection(models.Model):
    direction = models.CharField(max_length=50,
                                 verbose_name='Желаемое направление',)

    def __str__(self):
        return f"{self.direction}"

    class Meta:
        verbose_name = 'Направления в банке'
        verbose_name_plural = "Направления в банке"

class Test(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE,
                                 verbose_name='Категории')

    def __str__(self):
        return f"{self.category}"

class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE,
                             verbose_name='Тест')
    question_text = models.CharField(max_length=200,
                                     verbose_name='Текст вопроса')
    true_answer = models.CharField(max_length=100,
                                   verbose_name='Правильный ответ')

    def __str__(self):
        return f'{self.test}_{self.question_text}'

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                             verbose_name='Вопрос')
    answer_option = models.CharField(max_length=100,
                                     verbose_name='Вариант ответа',
                                     blank=True, null=True)
    def __str__(self):
        return f'{self.question}'

class TestResult(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE,
                             verbose_name='Тест')
    aplicat = models.ForeignKey(Aplication, on_delete=models.CASCADE,
                             verbose_name='Клиент')
    score = models.IntegerField(verbose_name='Оценка', default=0)

    def __str__(self):
        return f'{self.aplicat}_{self.test}'
