import re

def generator_numbers(text):
    pattern = r'\b\d+\.\d+\b'  # Регулярний вираз для пошуку дійсних чисел у тексті
    for match in re.finditer(pattern, text):
        yield float(match.group())  # Повертаємо знайдене число як float

def sum_profit(text, generator_func):
    return sum(generator_func(text))

# Приклад використання:
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print("Загальний дохід: ", total_income)  
