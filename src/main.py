#
# def load_orders_from_file(filename):
#     orders_data = []
#     try:
#         with open(filename, "r", encoding="utf-8") as file:
#             for line in file:
#                 line = line.strip()
#                 elements = line.split(":")
#                 if len(elements) == 4:
#                     orders_data.append(line)
#     except FileNotFoundError:
#         print("Ошибка! Файл не существует")
#         return []
#     return orders_data
#
# def calculate_order_total(price, discount_rate):
#     if 0 <= discount_rate <= 1:
#         total = price * (1 - discount_rate)
#         return round(total, 2)
#
#
# def get_discount_by_total(total):
#     if total <= 0:
#         return 0
#     if  total > 10000:
#         discount_rate = 0.15
#     elif total > 5000:
#         discount_rate = 0.10
#     else:
#         discount_rate = 0.05
#     return discount_rate
#
# def process_orders(orders_data):
#     order_list =[]
#     for order in orders_data:
#         try:
#             order_dict = {}
#             parts = order.split(":")
#             parts[1] = int(parts[1])
#             discount = get_discount_by_total(parts[1])
#             total_sum = calculate_order_total(parts[1], discount)
#             order_dict['order_id'] = parts[0]
#             order_dict['total'] = total_sum
#             order_dict['status'] = parts[2]
#             order_dict['user'] = parts[3]
#             order_list.append(order_dict)
#         except ValueError:
#             print("Некорректные данные, должно быть число!")
#     return order_list
#
#
# def analyze_orders(processed_orders):
#     stats = {
#     "total_orders": 0,
#     "total_sum": 0,
#     "by_status": {},
#     "unique_users": set()
#               }
#     for order in processed_orders:
#         total_sum = order['total']
#         by_status = order['status']
#         unique_user = order['user']
#         stats['total_orders'] += 1
#         stats['total_sum'] += total_sum
#         if by_status not in stats['by_status']:
#             stats['by_status'][by_status] = 0
#         stats['by_status'][by_status] += 1
#         stats['unique_users'].add(unique_user)
#     stats['unique_users'] = sorted(list(stats['unique_users']))
#     return stats
#
# from src.models.exceptions import ValidationError, InsufficientStockError, InvalidOrderError, BusinessLogicError
# from src.models.order import Order
# from src.models.payment import CardPayment, PayPalPayment
# from src.models.product import Product
# from src.models.user import User
#
#
# def process_order_system():
#     user = User("Иван", "ivan@test.com")
#     product1 = Product("Ноутбук", 50000, 2)
#     product2 = Product("Мышь", 1500, 3)
#     order = Order(user, [product1, product2])
#     total = order.calculate_total()
#     print(f"Общая стоимость заказа: {total}")
#     payments = [
#         CardPayment(1000, "1234 5678 9012 3456"),
#         PayPalPayment(2000, "test@paypal.com")
#     ]
#     for payment in payments:
#         print(payment.process_payment())
#     sorted_products = sorted([product1, product2])
#     for product in sorted_products:
#         print(product)
#     try:
#         product2.set_price(-1000)
#     except ValidationError as e:
#         print("Ошибка валидации:", e)
#     try:
#         product1.sell(100)
#     except InsufficientStockError as e:
#         print("Ошибка бизнес-логики:", e)
#     try:
#         user.set_email("ivantest.com")
#     except ValidationError as e:
#         print("Ошибка валидации:", e)
#     try:
#         order.add_product("product1")
#     except InvalidOrderError as e:
#         print("Ошибка валидации:", e)
#     try:
#        order2 = Order(user, [])
#     except BusinessLogicError as e:
#         print("Ошибка бизнес-логики:", e)
#
#
# process_order_system()

data = ["1", "2", "3", "новый"]
total = 0

for i in data:
    if i.isdigit():
        total += int(i)

print(total)

visitors_day_1 = {"user_123", "user_456", "user_789"}
visitors_day_2 = {"user_456", "user_789", "user_999"}

new_visitors = visitors_day_1.difference(visitors_day_2)
print(new_visitors)
