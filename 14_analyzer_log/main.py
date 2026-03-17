from collections import Counter

LINE_WIDTH = 45
FILE = "access.log"

unique_ip = Counter()
status_counter = Counter()

with open(FILE, encoding="utf-8") as logs:
    for count, log in enumerate(logs, 1):
        parts = log.split()
        ip = parts[0]
        status = parts[-2]

        unique_ip[ip] += 1
        status_counter[status] += 1

print("=" * LINE_WIDTH)
print("ЛОГ-АНАЛИЗАТОР")
print("=" * LINE_WIDTH)
print()
print(f"Всего запросов: {count}")
print(f"Уникальных IP-адресов: {len(unique_ip)}")
print()
print("СТАТИСТИКА ПО СТАТУСАМ:")
print(f"✅ Успешных (200): {status_counter['200']}")
print(f"⚠️ Перенаправлений (301, 302): {status_counter['301'] + status_counter['302']}")
print(f"❌ Ошибок клиента (404, 403): {status_counter['404'] + status_counter['403']}")
print(f"💥 Ошибок сервера (500): {status_counter['500']}")