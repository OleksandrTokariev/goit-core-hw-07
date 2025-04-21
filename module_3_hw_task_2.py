import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    # cheking the correctness of the parameters of the function
    if (min < 1):
        print('Incorrect min number. Must be not lower than 1')
    elif (max > 1000):
        print('Incorrect max number. Must be not greater than 1000')
    elif quantity > (max - min + 1) :
        print(f'Incorrect quantity. Must be between 1 and {max - min + 1}')
    else:
        numbers_set = set()
        while len(numbers_set) < quantity:
            new_number = random.randint(min, max)
            numbers_set.add(new_number)
        return sorted(list(numbers_set))

lottery_numbers = get_numbers_ticket(1, 49, 50)
print("Your lottery numbers:", lottery_numbers)