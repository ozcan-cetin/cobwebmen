fibonacci=[1]
for i in range(1,56):
    if i == 1:
        fibonacci.append(i)

    elif i == fibonacci[-1] + fibonacci[-2]:
        fibonacci.append(i)

    elif fibonacci[-1] == 55:
        break
print(f"fibonacci numbers: {fibonacci}")
