
# Case 1
import random
random_numbers = [random.randint(1, 100) for _ in range(100)]
selected_numbers = random.sample(random_numbers, 10)
sorted_numbers = sorted(selected_numbers)
print(sorted_numbers)
biggest_numbers = sorted_numbers[-3:]
print(biggest_numbers)


# Case 2
import random
numbers = set()
while len(numbers) < 100:
    numbers.add(random.randint(1, 100))
sorted_numbers = list(numbers)
sorted_numbers.sort()
print(sorted_numbers)

biggest_numbers = sorted_numbers[-3:]
print(biggest_numbers)
