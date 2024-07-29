import pandas as pd
import hashlib

def hash_value(value):
    """Return a SHA-256 hash of the given value."""
    hashed = hashlib.sha256(value.encode()).hexdigest()
    return 'h-'+hashed

def mask(name):
    """Return a masked version of the name."""
    mask='X'
    return f"{name[0]}{mask * (len(name) - 1)}"

def anonymize_columns(df, columns):
    """
    Anonymizes specific columns in a DataFrame using provided masking methods.
    
    Parameters:
    df (pd.DataFrame): The input DataFrame.
    columns (dict): Dictionary mapping columns to their respective mask methods.
    
    Returns:
    pd.DataFrame: The anonymized DataFrame.
    """
    try:
        df_copy = df.copy()
        for column, mask_method in columns.items():
            if column in df_copy.columns:
                df_copy[column] = df_copy[column].apply(mask_method)
    except Exception as e:
        print(f"Error anonymizing columns: {e}")
    return df_copy