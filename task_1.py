def caching_fibonacci():
    cache = {} # Створити порожній словник

    def fibonacci(n):
        if n <= 0: 
            return 0
        if n == 1: 
            return 1
        if n in cache: # Пошук в кеші готового результату
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2) # Обраховуємо числа Фібоначчі
        return cache[n]

    return fibonacci


# Визиваємо функцію fibonacci
fib = caching_fibonacci()

# Перевірка результатів
print(fib(10))  
print(fib(15))
