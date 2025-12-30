import pandas as pd

def clean_data(df):
    """Clean the DataFrame by handling missing values and duplicates.

    Args:
        df (pd.DataFrame): The DataFrame to clean.
    Returns:
        pd.DataFrame: The cleaned DataFrame.
    """
    if 'unnamed: 0' in df.columns:
        df = df.drop(columns=['unnamed: 0'])
        print("[INFO] Dropped 'unnamed: 0' column")

    # Strip whitespace and standardize the text
    df['headline'] = df['headline'].astype(str).str.strip().str.lower()
    df['publisher'] = df['publisher'].astype(str).str.strip().str.lower()
    df['stock'] = df['stock'].astype(str).str.strip().str.upper()

    # Convert 'date' column to datetime
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    #Drop rows with missing values
    df = df.dropna(subset=['headline', 'publisher', 'stock', 'date'])

    # Add helper columns
    df['text_length'] = df['headline'].apply(len)
    df['day'] = df['date'].dt.day
    df['month'] = df['date'].dt.month
    df['hour'] = df['date'].dt.hour

    print(f"[INFO] Cleaned dataset: {df.shape[0]} rows, {df.shape[1]} columns")
    return df