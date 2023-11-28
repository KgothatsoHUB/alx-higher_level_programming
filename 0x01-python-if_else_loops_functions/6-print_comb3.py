#!/usr/bin/python3

result = [f"{i}{j}" for i in range(9) for j in range(i + 1, 10) if i * 10 + j < 89]
print(", ".join(result))

