from collections import Counter

LINE_WIDTH = 45
FILE = "access.log"

unique_ip = Counter()
status_counter = Counter()
size = 0

def translating_from_bytes(size):
    if size >= 1_048_576:
        return (size / 1_048_576, "МБ")
    elif size >= 1_024:
        return (size / 1_024, "КБ")
    else:
        return (size, "Байт")

with open(FILE, encoding="utf-8") as logs:
    for count, log in enumerate(logs, 1):
        parts = log.split()
        ip = parts[0]
        status = parts[-2]
        size_log = int(parts[-1])

        unique_ip[ip] += 1
        status_counter[status] += 1
        size += size_log

size_tuple = translating_from_bytes(size)
size_final = size_tuple[0]
type_of_memory = size_tuple[1]
average_size = size / count
average_size_true = translating_from_bytes(average_size)

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
print()
print(f"Общий объём переданных данных: {size_final:.1f} {type_of_memory}")
print(f'Средний размер ответа: {average_size_true[0]:.1f} {type_of_memory}')