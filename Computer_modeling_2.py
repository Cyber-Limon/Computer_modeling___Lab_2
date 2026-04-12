import random



print("Введите:")
a, b = map(float, input("- пределы интегрирования:       ").split())
f    =        str(input("- подынтегральную функцию:      "))
I    =      float(input("- известное значение интеграла: "))

n    =        int(input("- количество итераций:          "))



u = []
x = []
E = []

for i in range(n):
    u.append(random.random())
    x.append(a + (b - a) * u[-1])
    E.append(eval(f.replace("x", f"({str(x[-1])})")))



w = (b - a) * sum(E) / n

S = 0
for i in range(n):
    S += (E[i] - w) ** 2
S = S / (n - 1)

d = 1.96 * (S ** 0.5) / (n ** 0.5)
l = w - d
r = w + d
l, r = min(l, r), max(l, r)



length = max(max(u), abs(min(u)), max(x), abs(min(x)), max(E), abs(min(E)))
length = len(str(round(length, 5))) + 1

print(f"\nНомер испытания | {" | ".join(f"{i:<{length}}" for i in range(1, n + 1))}")
print('-' * (16 + n * (length + 3)))
print(f"u_i             | {" | ".join(f"{i:<{length}.5f}" for i in u)}")
print(f"x_i             | {" | ".join(f"{i:<{length}.5f}" for i in x)}")
print(f"f(x_i)          | {" | ".join(f"{i:<{length}.5f}" for i in E)}")

print(f"\n- w {' ' * 19} = {w}")
print(f"- |I - w| {' ' * 13} = {abs(I - w)}")
print(f"- S^2 {' ' * 17} = {S}")
print(f"- доверительный интервал: ({l}, {r})")

if l < I < r:
    print(f"\n\n\nВычисление верное: {I} принадлежит ({l}, {r})")
else:
    print(f"\n\n\nВычисление неверное: {I} не принадлежит ({l}, {r})")



print("\n\n\n\n\n")
