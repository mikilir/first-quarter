day_1 = int(input("Введите результаты пробежки первого дня в км: "))
result = int(input("Введите общий желаемый результат в км: "))
result_days = 1
result_km = day_1
while result_km < result:
        day_1 = day_1 + 0.1 * day_1
        result_days += 1
        result_km = result_km + day_1
print(f"Вы достигнете требуемых показателей на {result_days} день")