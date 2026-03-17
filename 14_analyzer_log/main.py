from collections import Counter

LINE_WIDTH = 45
FILE = "access.log"

unique_ip = Counter()
status_counter = Counter()
size = 0
mb1 = False
local_ip = True

def translating_from_bytes(size):
    if size >= 1_048_576:
        return (size / 1_048_576, "МБ")
    elif size >= 1_024:
        return (size / 1_024, "КБ")
    else:
        return (size, "Байт")

try:
    with open(FILE, encoding="utf-8") as logs:
        for count, log in enumerate(logs, 1):
            try:
                parts = log.split()
                ip = parts[0]
                status = parts[-2]
                size_log = int(parts[-1])

                unique_ip[ip] += 1
                status_counter[status] += 1
                size += size_log

                if size_log >= 1_048_576:
                    mb1 = True
                if not ip.startswith('192.168.'):
                    local_ip = False
            except (IndexError, ValueError):
                continue

except FileNotFoundError:
    print(f"❌ Файл {FILE} не найден")
except PermissionError:
    print(f"❌ Нет прав на чтение {FILE}")
except Exception as e:
    print(f"Неизвестная ошибка {e}")

size_tuple = translating_from_bytes(size)
size_final = size_tuple[0]
type_of_memory = size_tuple[1]

if count > 0:
    average_size = size / count
    average_size_true = translating_from_bytes(average_size)
else:
    average_size_true = (0, "Байт")
    type_of_memory = "Байт"

top5_ip = unique_ip.most_common(5)

if status_counter:
    errors = filter(lambda s: s.startswith('4') or s.startswith('5'), status_counter)
    most_common_error = max(errors, key=lambda s: status_counter[s])
    error_count = status_counter[most_common_error]
else:
    most_common_error = 'нет ошибок'
    error_count = 0

print("=" * LINE_WIDTH)
print("ЛОГ-АНАЛИЗАТОР")
print("=" * LINE_WIDTH)
print()
print(f"Всего запросов: {count}")
print(f"Уникальных IP-адресов: {len(unique_ip)}")
print()
print("ТОП-5 IP ПО КОЛИЧЕСТВУ ЗАПРОСОВ:")
for rank, (ip, cnt) in enumerate(top5_ip, 1):
    print(f"{rank}. {ip} → {cnt}")
print()
print("СТАТИСТИКА ПО СТАТУСАМ:")
print(f"✅ Успешных (200): {status_counter['200']}")
print(f"⚠️ Перенаправлений (301, 302): {status_counter['301'] + status_counter['302']}")
print(f"❌ Ошибок клиента (404, 403): {status_counter['404'] + status_counter['403']}")
print(f"💥 Ошибок сервера (500): {status_counter['500']}")
print()
print(f"Общий объём переданных данных: {size_final:.1f} {type_of_memory}")
print(f'Средний размер ответа: {average_size_true[0]:.1f} {average_size_true[1]}')
print()
print(f"Самая частая ошибка: {most_common_error} ({error_count} раз)")
print()
print('Дополнительные проверки:')
print(f"📈 Есть запросы с объёмом > 1 MB? {'да' if mb1 else 'нет'}")
print(f"🌍 Все запросы от локальных IP? {'да' if local_ip else 'нет'}")