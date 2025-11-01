
from faker import Faker
import random
import csv
from pathlib import Path

fake = Faker('pt_BR')

personas = []

for _ in range(15):
    persona = {
        "Nome": fake.name(),
        "Idade": random.randint(18, 80),
        "Cidade": fake.city()
    }
    personas.append(persona)


arquivo_csv = Path("Lista de nomes.csv")
with arquivo_csv.open(mode='w', newline='', encoding='utf-8') as file:
    fieldnames = ["Nome", "Idade", "Cidade"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(personas)

print("Arquivo CSV criado com sucesso!")