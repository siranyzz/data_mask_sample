from generate_data import generate_csv
from anonymize import hash_value,mask,anonymize_columns
from parse import parse_df
from schema import person_template,salt
import pandas as pd

if __name__ == "__main__":
    original_data_dir = 'original_data.csv'
    anonymized_data_dir = 'anonymized_data.csv'
    try:
        # Generate the original CSV file
        generate_csv(original_data_dir,100)

        df = pd.read_csv(original_data_dir)

        df = parse_df(df,person_template)

        # Define anonymization methods for specific columns
        columns_to_anonymize = {
            'first_name': mask,
            'last_name': mask,
            'address': lambda x: hash_value(x+salt)
        }
        
        anonymized_df = anonymize_columns(df, columns_to_anonymize)
        anonymized_df.to_csv(anonymized_data_dir, index=False)
    except Exception as e:
        print(f"Error in main execution: {e}")


