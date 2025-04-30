from typing import List, Literal

def square_numbers(numbers: List[int]) -> List[int]:
    return [number ** 2 for number in numbers]

input_numbers = [1, 2, 3, 4, 5]
squared_numbers = square_numbers(input_numbers)
print(squared_numbers)

account_type: Literal['savings', 'checking', 'credit']
account_type = 'savings'