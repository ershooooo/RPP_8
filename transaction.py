import asyncio
import random
from datetime import datetime, timedelta

async def generate_transaction():
    """Генерирует одну финансовую транзакцию."""
    timestamp = datetime.now() - timedelta(days=random.randint(0, 365))
    categories = ["Food", "Rent", "Utilities", "Transportation", "Entertainment", "Shopping", "Travel", "Salary", "Investment"]
    category = random.choice(categories)
    amount = round(random.uniform(1, 1000), 2)
    return {"timestamp": timestamp.isoformat(), "category": category, "amount": amount}


async def generate_transactions(num_transactions):
    """Генерирует заданное количество транзакций."""
    tasks = [generate_transaction() for _ in range(num_transactions)]
    transactions = []
    for task in asyncio.as_completed(tasks):
        transactions.append(await task)  # await здесь необходим
    return transactions

