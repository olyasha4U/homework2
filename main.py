1
# class Task
#     def __init__(self, title="Вивчити Python", description="Прочитати главу про об’єктно-орієнтоване програмування",  deadline="2025-11-05", status="виконане"):
#         self.title=title
#         self.description=description
#         self.deadline=deadline
#         self.status=status
#     def __str__(self):
#         return f"Назва: {self.title}, Дедлайн: {self.deadline}, Стан: {self.status}"
# class TaskManager:
#     def __init__(self, mannager_name,):
#         self.manager=mannager_name
#         self.task=[]
#     def add_task(self, task):
#         self.task.append(task)
#     def delete_task(self, title):
#         for task in self.task:
#             if task.title == title:
#                 self.task.remove(task)
#     def add_status(self, title ):
#         for task in self.task:
#             if task.title == title:
#                 new_status = input("Відмітьте статус (виконане/не виконане): ")
#                 task.status = new_status
#                 print(f"Статус '{title}' оновлено на: {task.status}")
#                 return
#     def show_tasks(self):
#         if self.task:
#             print(f" Завдання менеджера {self.manager}:")
#             for t in self.task:
#                 print("-", t)
#         else:
#             print(f"наразі немає завдань у {self.manager}.")
#
# task_1 = Task("Вивчити Python", "Прочитати главу про об’єктно-орієнтоване програмування", "2025-11-05")
# task_2 = Task("Підготувати презентацію", "Створити слайди для зустрічі з клієнтом", "2025-10-28")
# task_3 = Task("Підготувати звіт", "Зробити щомісячний фінансовий звіт у Excel", "2025-10-31")
#
# manager=TaskManager("TaskManager")
#
# manager.add_task(task_1)
# manager.add_task(task_2)
# manager.add_task(task_3)
# manager.delete_task(task_1)
# manager.show_tasks()
2
# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def __str__(self):
#         return f"{self.name} — {self.price} грн (кількість: {self.quantity})"
#
#
# class Cart:
#     def __init__(self):
#         self.products = []
#
#     def add_product(self, product):
#         self.products.append(product)
#
#     def delete_item(self, name):
#         for product in self.products:
#             if product.name == name:
#                 self.products.remove(product)
#                 return
#
#
#     def total_price(self):
#         total = 0
#         for p in self.products:
#             total += p.price
#         return total
#
#     def show_products(self):
#         if self.products:
#             print(" Вміст кошика:")
#             for product in self.products:
#                 print(f"- {product.name}: {product.price} грн (x{product.quantity})")
#             print(f" Загальна сума: {self.total_price()} грн")
#         else:
#             print(" Кошик порожній.")
#
#
# p1 = Product("Ноутбук Lenovo IdeaPad", 28999, 5)
# p2 = Product("Смартфон Samsung Galaxy A55", 19999, 8)
# p3 = Product("Навушники JBL Tune 510BT", 2999, 12)
# p4 = Product("Мишка Logitech M185", 899, 20)
#
# cart = Cart()
#
# cart.add_product(p1)
# cart.add_product(p2)
# cart.add_product(p3)
# cart.add_product(p4)
#
# cart.delete_item("Навушники JBL Tune 510BT")
#
# cart.show_products()
# 4
# class Employee:
#     def __init__(self, name, position, salary):
#         self.name=name
#         self.position=position
#         self.salary=salary
#
# class Department:
#     def __init__(self):
#         self.employees=[]
#     def add_employees(self, employee):
#         self.employees.append(employee)
#     def remove_employees(self, employee):
#         if employee in self.employees:
#             self.employees.remove(employee)
#             return
#     def total_salary(self):
#         total = 0
#         for s in self.employees:
#             total += s.salary
#         return  total
#
#     def show_employees(self):
#         if self.employees:
#             print(f"Загальна заробітня плата відділу:{self.total_salary()}")
#         else:
#             print("У відділі немає працівників.")
#
# em1 = Employee("Олег", "Директор", 67500)
# em2 = Employee("Олександра", "Керівник", 67500)
# em3 = Employee("Марія", "Менеджер", 35000)
#
# department=Department()
# department.add_employees(em1)
# department.add_employees(em2)
# department.add_employees(em3)
# department.remove_employees(em1)
# department.show_employees()