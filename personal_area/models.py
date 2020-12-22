from datetime import date, datetime

from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django.db import models


class UserPosition(models.Model):
    """ Модель для описания должностей пользователей """

    title: str = models.CharField('Должность', max_length=64, null=False)
    multiplier: float = models.FloatField('Множитель репутаций', null=False, default=1)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'user_position'
        verbose_name = 'Дожности пользователя'
        verbose_name_plural = 'Должности пользователей'


class Role(models.Model):
    """ Модель для описания ролей участников """

    title: str = models.CharField('Роль', max_length=64, null=False)
    multiplier: float = models.FloatField('Множитель репутаций', null=False, default=1)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'role'
        verbose_name = 'Должность на мероприятий'
        verbose_name_plural = 'Должности на мероприятиях'


class Direction(models.Model):
    """ Модель для описания направлений (специальностей и профессий) """

    SPECIALTY, PROFESSION = 1, 2
    TYPES = ((SPECIALTY, 'Специальность'), (PROFESSION, 'Профессия'))

    type: int = models.SmallIntegerField('Тип', choices=TYPES, default=SPECIALTY)

    code: str = models.CharField('Код', null=False, max_length=8)
    title: str = models.CharField('Название', max_length=64, null=False)
    abbreviation: str = models.CharField('Аббревиатура', null=False, max_length=4)

    def __str__(self):
        return f'{self.code} - {self.title}'

    class Meta:
        db_table = 'direction'
        verbose_name = 'Направление'
        verbose_name_plural = 'Направления'


class Group(models.Model):
    """ Модель для описания групп """

    number: int = models.PositiveSmallIntegerField('Номер группы', null=False, default=1)
    year: int = models.PositiveSmallIntegerField('Год набора', null=False)
    direction = models.ForeignKey(Direction, on_delete=models.PROTECT, null=False, verbose_name='Специальность')

    graduated: bool = models.BooleanField('Группа закончила обучение?', null=False, default=False)

    def __str__(self):
        return f'{self.number}{self.direction.abbreviation}-{self.year}{" ВЫПУЩЕНА!" if self.graduated else ""}'

    class Meta:
        db_table = 'group'
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Event(models.Model):
    """ Модель для описания мероприятий """

    title: str = models.CharField('Название', max_length=64, null=False)
    about: str = models.CharField('Описание', max_length=256, null=False)

    roles = models.ManyToManyField(Role, verbose_name='Роли', help_text='Возможные роли на мероприятий',
                                   related_name='event_set', related_query_name='event')

    start_time: datetime = models.DateTimeField('Дата и время начала', null=False)
    end_time: datetime = models.DateTimeField('Дата и время конца', null=False)

    weight: float = models.FloatField('Баллов за участие', null=False, default=1)

    def __str__(self):
        return f'{self.title} - {self.about}'

    @property
    def users(self):
        return Participation.objects.filter(event=self)

    @property
    def number_of_participants(self) -> int:
        return len(self.users)

    class Meta:
        db_table = 'events'
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class UserProfile(models.Model):
    """ Модель для описания профиля пользователя """

    GENRE_UNKNOWN, GENRE_FEMALE, GENRE_MALE = 0, 1, 2
    GENRE_CHOICES = ((GENRE_UNKNOWN, 'Не известно'), (GENRE_FEMALE, 'Женщина'), (GENRE_MALE, 'Мужчина'))

    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE, null=False)

    group = models.ForeignKey(Group, on_delete=models.PROTECT, verbose_name='Группа', null=True, blank=True)

    genre: int = models.SmallIntegerField('Пол', choices=GENRE_CHOICES, default=GENRE_UNKNOWN)
    birth_date: datetime = models.DateField('Дата рождения', null=True, blank=True, default=None)

    position = models.ForeignKey(UserPosition, verbose_name='Должность', on_delete=models.PROTECT, null=True)

    @property
    def age(self) -> int or None:
        if not self.birth_date:
            return None

        today = date.today()

        try:
            birthday = self.birth_date.replace(year=today.year)
        except ValueError:
            birthday = self.birth_date.replace(year=today.year, month=self.birth_date.month + 1, day=1)

        if birthday > today:
            return today.year - self.birth_date.year - 1
        else:
            return today.year - self.birth_date.year

    @property
    def email(self) -> str or None:
        return self.user.email

    @property
    def full_name(self) -> str:
        return self.user.get_full_name()

    @property
    def participations(self):
        """ Функция возвращает мероприятия в которых участвовал пользователь """

        return Participation.objects.filter(user=self.user)

    @property
    def participations_count(self) -> int:
        """ Функция возвращет кол-во мероприятий в которых участвовал пользователь """

        return self.participations.count()

    @property
    def reputation(self) -> float:
        """ Функци расчитывает репутацию пользователя """

        points = 0

        for participation in self.participations:
            # Получаем "вес" мероприятия и множитель роли
            weight = participation.event.weight
            multiplier = participation.positions_of_participant.multiplier

            # Добавляем к общей сумме
            points += weight * multiplier

        return points * self.position.multiplier

    def __str__(self):
        return f'{self.position.title} {self.user.get_full_name()}'

    class Meta:
        db_table = 'user_profile'
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Participation(models.Model):
    """ Модель для описания связей пользователей и мероприятий """

    WAITING, DENIED, CONFIRMED = 1, 2, 3
    STATUSES = ((WAITING, 'Ожидание'), (DENIED, 'Отказано'), (CONFIRMED, 'Подтверждено'))

    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.PROTECT, null=True)
    event = models.ForeignKey(Event, verbose_name='Мероприятие', on_delete=models.PROTECT, null=True)
    role = models.ForeignKey(Role, verbose_name='Роль', on_delete=models.PROTECT, null=False)

    status: int = models.SmallIntegerField('Статус', choices=STATUSES, default=WAITING)

    create_at: datetime = models.DateTimeField('Дата создания', auto_now_add=True)
    update_at: datetime = models.DateTimeField('Дата обновления', auto_now=True)

    def __str__(self):
        return f'{self.user.get_full_name()} - {self.event.title} ({self.status})'

    @property
    def adds_to_reputation(self) -> float:
        """ Функция считает сколько участие добавляет к репутаций """

        return self.event.weight * self.role.multiplier

    class Meta:
        db_table = 'participation'
        verbose_name = 'Участие'
        verbose_name_plural = 'Участия'


# Создаём сигнал - при созданий пользователя - создавать ему профиль
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user: UserProfile = UserProfile.objects.create(user=instance)
        user.position = UserPosition.objects.get(title='Студент')
        user.save()


# Регистрируем сигнал
post_save.connect(create_user_profile, sender=User)
