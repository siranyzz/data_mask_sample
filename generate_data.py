import pandas as pd
from faker import Faker


def generate_csv(file_path,number):
    try:
        fake = Faker()
        data = {
            'first_name': [fake.first_name() for _ in range(number)],
            'last_name': [fake.last_name() for _ in range(number)],
            'address': [fake.address() for _ in range(number)],
            'date_of_birth': [fake.date_of_birth() for _ in range(number)]
        }
        df = pd.DataFrame(data)
        df.to_csv(file_path, index=False)
    except Exception as e:
        print(f"Error generating CSV: {e}")

