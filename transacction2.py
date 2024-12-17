import json
import locale

# Установка локали для вывода чисел с точкой в качестве десятичного разделителя
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8') #Или другая подходящая локаль


async def process_transactions(filename="transactions.json", spending_limit=1000):
    """Обрабатывает файл с транзакциями."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            transactions = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Ошибка чтения файла: {e}")
        return {}

    category_sums = {}
    for transaction in transactions:
        category = transaction["category"]
        amount = transaction["amount"]
        category_sums[category] = category_sums.get(category, 0) + amount

    for category, amount in category_sums.items():
        if amount > spending_limit:
            print(f"Превышение лимита расходов в категории '{category}': {amount:.2f} руб.")

    return category_sums


async def main():
    filename = input("Введите имя файла с транзакциями (transactions.json по умолчанию): ") or "transactions.json"
    try:
        spending_limit = float(input("Введите лимит расходов для предупреждения (1000 по умолчанию): ") or 1000)
        if spending_limit <=0:
            raise ValueError("Лимит расходов должен быть положительным числом.")
    except ValueError as e:
        print(f"Ошибка: {e}")
        return

    category_sums = await process_transactions(filename, spending_limit)
    print("Суммы по категориям:")
    for category, amount in category_sums.items():
        print(f"{category}: {amount:.2f} руб.")

if __name__ == "__main__":
    asyncio.run(main())
