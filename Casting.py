from typing import Union

# String to Integer
num_str = "123"
num_int = int(num_str)  # => 123 (int)

# Float to Integer
pi = 3.14
whole = int(pi)         # => 3

# Integer to String
user_id = 101
user_id_str = str(user_id)  # => "101"

# String to Float
price = "19.99"
price_float = float(price)  # => 19.99

# Integer to Boolean
zero = 0
nonzero = 5
print(bool(zero))     # False
print(bool(nonzero))  # True


# Convert String or Float to Number
def to_int(value: Union[str, float, int]) -> int:
    return int(value)

print(to_int("42"))    # 42
print(to_int(3.7))     # 3