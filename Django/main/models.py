from django.db import models

class Products(models.Model):
    title = models.CharField('Название', max_length = 100)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Customers(models.Model):
    name = models.CharField('Имя', max_length = 60)
    surname = models.CharField('Фамилия', max_length = 60)
    phone = models.CharField('Телефон', max_length = 11)
    email = models.CharField('Почта', max_length = 100)

    def __str__(self):
        return f'{self.name} {self.surname}'
    
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Orders(models.Model):
    order_number = models.CharField('Номер', max_length = 100)
    order_date = models.DateField('Дата заказа')
    prod = models.ForeignKey('Products', on_delete = models.PROTECT, null=True)
    cust = models.ForeignKey('Customers', on_delete = models.PROTECT, null=True)
    quantity = models.IntegerField('Количество', default = 0)
    price = models.IntegerField('Цена', default = 0)

    def __str__(self):
        return self.order_number
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'