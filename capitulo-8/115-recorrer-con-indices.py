analogos = ["A0", "A1", "A2", "A3", "A4", "A5"]

i = 1
for analogo in analogos:
    print(f"{i} - {analogo}")
    i += 1

print("-" * 30)

for i in range(len(analogos)):
    print(f"{i} - {analogos[i]}")

print("-" * 30)

for i, analogo in enumerate(analogos, start=1):
    print(f"{i} - {analogo}")