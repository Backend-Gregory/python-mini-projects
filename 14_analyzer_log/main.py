from collections import Counter

LINE_WIDTH = 45
FILE = "access.log"

unique_ip = Counter()

with open(FILE, encoding="utf-8") as logs:
    for count, log in enumerate(logs, 1):
        parts = log.split()
        ip = parts[0]
        unique_ip[ip] += 1

print("=" * LINE_WIDTH)
print("ЛОГ-АНАЛИЗАТОР")
print("=" * LINE_WIDTH)
print()
print(f"Всего запросов: {count}")
print(f"Уникальных IP-адресов: {len(unique_ip)}")