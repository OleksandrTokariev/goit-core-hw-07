import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    # cheking the correctness of the parameters of the function
    if (min < 1) | (max > 1000) | quantity > (max - min + 1) :
        print('Incorrect input data. Check parameters of the function')
    else:
        numbers_set = set()
        while len(numbers_set) < quantity:
            new_number = random.randint(min, max)
            numbers_set.add(new_number)
        return sorted(list(numbers_set))

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Your lottery numbers:", lottery_numbers)