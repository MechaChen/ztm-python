birth_year = input('What year were you born?')

age = 2025 - int(birth_year)
print(f'You age is: {age}')

age = 2025 - float(birth_year)
print(f'You age is: {age}')

age = 2025 - bool(birth_year)
print(f'You age is: {age}')
