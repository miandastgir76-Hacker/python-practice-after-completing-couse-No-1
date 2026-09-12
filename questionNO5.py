import random
import statistics

data = []

for i in range(10):
    data.append(random.randint(1, 50))

print("Random numbers:", data)

mean_value = statistics.mean(data)

print("The mean value is:", mean_value)