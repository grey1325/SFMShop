from src.main import load_orders_from_file, process_orders, analyze_orders

def process_order_file(input_file, output_file):
    orders = load_orders_from_file(input_file)
    process = process_orders(orders)
    analyze = analyze_orders(process)

    with open(output_file, "w", encoding="utf-8") as file:
        part_order = analyze["total_orders"]
        part_total = analyze["total_sum"]
        result = [f"{status} : {count}" for status, count in analyze["by_status"].items()]
        status = ", ".join(result)
        part_users = analyze["unique_users"]
        file.write(
        f"Обработано заказов: {part_order}\n"
        f"Общая сумма: {part_total} руб.\n"
        f"По статусам: {status}\n"
        f"Уникальных пользователей: {len(part_users)}\n"
        )
    return output_file

process_order_file = process_order_file("SFMShop/data/orders.txt", "SFMShop/data/orders_processed.txt")

