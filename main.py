import asyncio
import json
from transaction import generate_transactions

async def save_transaction(transaction, transaction_number):
    filename = f"transaction_{transaction_number}.json"
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(transaction, f, indent=4)
        print(f"Сохранена транзакция {transaction_number} в файл {filename}")
    except Exception as e:
        print(f"Ошибка сохранения транзакции: {e}")

async def main():
    try:
        num_transactions = int(input("Введите количество транзакций для генерации: "))
        if num_transactions <= 0:
            raise ValueError("Количество транзакций должно быть положительным.")

        transactions = await generate_transactions(num_transactions)

        for i, transaction in enumerate(transactions):
            await save_transaction(transaction, i + 1)

        print("Генерация транзакций завершена.")
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    asyncio.run(main())

