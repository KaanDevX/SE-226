import math

girdi1 = input("1. Noktanin koordinatlarini girin (x1 y1): ")
x1, y1 = map(float, girdi1.split())


girdi2 = input("2. Noktanin koordinatlarini girin (x2 y2): ")
x2, y2 = map(float, girdi2.split())


mesafe = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


print(f"\nNoktalar: ({x1}, {y1}) ve ({x2}, {y2})")
print(f"Aradaki Mesafe: {mesafe}")