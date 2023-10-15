from django.db import models
from django.contrib import admin
from django.utils.html import format_html


class Advertisement(models.Model):
    id = models.AutoField("порядковый номер", primary_key=True)
    title = models.CharField("заголовок", max_length=128)
    description = models.TextField("описание")
    price = models.DecimalField("цена", max_length=10, decimal_places=2, max_digits=20)  # decimal_places - количество чисел после точки
    action = models.BooleanField("торг", help_text='отметьте, если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)  # auto_now_add=True, чтобы дата сама автоматически выставлялась при добавлении этого поля
    created_up = models.DateTimeField(auto_now=True)  # автоматически меняется(не добавляется)

    class Meta:
        db_table = 'advertisements'
        verbose_name = 'Объявления'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>'

    @admin.display(description='Дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%h:%M:%S')
            return format_html(
                '<span style="color:green;">Сегодня в {}</span>', created_time
            )
        return self.created_at.strftime('%h:%m:%Y в %h:%M:%S')

    @admin.display(description='Дата обновления')
    def updated_date(self):
        from django.utils import timezone
        if self.created_up.date() == timezone.now().date():
            updated_time = self.created_up.time().strftime('%h:%M:%S')
            return format_html(
                '<span style="color:green;">Сегодня в {}</span>', updated_time
            )
        return self.created_up.strftime('%h:%m:%Y в %h:%M:%S')