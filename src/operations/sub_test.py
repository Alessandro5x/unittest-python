from .sub import SubOperation
from faker import Faker

fake = Faker()

def test_sub():
    subOperation = SubOperation()
    number1 = fake.random_number()
    number2 = fake.random_number()
    expect = number1 - number2

    result = subOperation.diferenca(number1, number2)

    assert result == expect