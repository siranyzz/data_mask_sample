import unittest
import pandas as pd
from generate_data import generate_csv
from anonymize import hash_value, mask, anonymize_columns
from parse import parse_df
from schema import person_template, salt
import os

class TestDataProcessing(unittest.TestCase):
    def setUp(self):
        self.original_data_dir = 'test_original_data.csv'
        self.anonymized_data_dir = 'test_anonymized_data.csv'
        generate_csv(self.original_data_dir, 10)
        self.df = pd.read_csv(self.original_data_dir)
    
    def tearDown(self):
        if os.path.exists(self.original_data_dir):
            os.remove(self.original_data_dir)
        if os.path.exists(self.anonymized_data_dir):
            os.remove(self.anonymized_data_dir)
    
    def test_generate_csv(self):
        df = pd.read_csv(self.original_data_dir)
        self.assertEqual(len(df), 10)
        self.assertTrue('first_name' in df.columns)
        self.assertTrue('last_name' in df.columns)
        self.assertTrue('address' in df.columns)
        self.assertTrue('date_of_birth' in df.columns)

    def test_parse_df(self):
        parsed_df = parse_df(self.df, person_template)
        self.assertEqual(parsed_df['first_name'].dtype, 'object')
        self.assertEqual(parsed_df['last_name'].dtype, 'object')
        self.assertEqual(parsed_df['address'].dtype, 'object')
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(parsed_df['date_of_birth']))
    
    def test_anonymize_columns(self):
        columns_to_anonymize = {
            'first_name': mask,
            'last_name': mask,
            'address': lambda x: hash_value(x + salt)
        }
        anonymized_df = anonymize_columns(self.df, columns_to_anonymize)
        self.assertNotEqual(list(self.df['first_name']), list(anonymized_df['first_name']))
        self.assertNotEqual(list(self.df['last_name']), list(anonymized_df['last_name']))
        self.assertNotEqual(list(self.df['address']), list(anonymized_df['address']))
    
    def test_end_to_end(self):
        df = parse_df(self.df, person_template)
        columns_to_anonymize = {
            'first_name': mask,
            'last_name': mask,
            'address': lambda x: hash_value(x + salt)
        }
        anonymized_df = anonymize_columns(df, columns_to_anonymize)
        anonymized_df.to_csv(self.anonymized_data_dir, index=False)
        
        result_df = pd.read_csv(self.anonymized_data_dir)
        self.assertEqual(len(result_df), 10)
        self.assertTrue('first_name' in result_df.columns)
        self.assertTrue('last_name' in result_df.columns)
        self.assertTrue('address' in result_df.columns)
        self.assertTrue('date_of_birth' in result_df.columns)

if __name__ == '__main__':
    unittest.main()
