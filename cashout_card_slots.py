import random

print("Игровые автоматы с выводом на карту - Демо!")
spins = 5
while spins > 0:
    spins -= 1
    result = random.choice(["Джекпот!", "Фриспин!", "Ещё спин!"])
    print(f"Спин {5 - spins}: {result}")
    if spins > 0:
        input("Нажми Enter для нового шанса...")
print("Крути и выводи на карту в топ-казино!")
