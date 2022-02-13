from faker import Faker
from .calculadora import Calculadora
from .operations.test.add import AddOperationSpy
from .operations.test.sub import SubOperationSpy

faker = Faker()

def test_add():
    addOperation = AddOperationSpy()
    calculadora = Calculadora(AddOperationSpy(), SubOperationSpy())

    number1 = faker.random_number()
    number2 = faker.random_number()

    result = calculadora.add(number1, number2, True)

    #Teste de entrada
    assert addOperation.soma_attributes['number1'] == number1
    assert addOperation.soma_attributes['number2'] == number2

    #Teste de saída
    assert result is not None