text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений \
додатковими надходженнями 27.45 і 324.00 доларів."

def generator_numbers(text: str):
    for elem in text.split(' '):
        try:
            float(elem)
            yield float(elem)
        except ValueError:
            continue

def sum_profit(text, generator_numbers):
    return sum(list(generator_numbers(text)))

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")

