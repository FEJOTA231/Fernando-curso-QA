from faker import Faker
import random

fake = Faker('pt_BR')

persona = {
    "Nome": "Fernando",
    "Idade": random.randint(18, 80),
    "Cidade": "São Paulo"
}

print(persona)