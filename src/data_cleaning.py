import pandas as pd
import numpy as np

def clean_transaction_data(input_path):
    
    print(f"Loading data from {input_path}...")
    df = pd.read_csv(input_path)
    df_clean = df.copy()

    df_clean['timestamp'] = pd.to_datetime(df_clean['timestamp'])
    df_clean['date'] = pd.to_datetime(df_clean['date'])

    text_columns = ['receiver_type', 'day_of_week', 'transaction_type', 
                    'payment_app', 'device_type', 'status', 'user_city_tier', 'user_kyc_status']
    for col in text_columns:
        df_clean[col] = df_clean[col].str.strip()

    df_clean.loc[df_clean['time_since_last_txn_min'] < 0, 'time_since_last_txn_min'] = np.nan

    cols_to_fill = ['time_since_last_txn_min', 'transaction_velocity', 'amount_deviation_score']
    for col in cols_to_fill:
        median_val = df_clean[col].median()
        df_clean[col] = df_clean[col].fillna(median_val)

    print("Data cleaning complete.")
    return df_clean

if __name__ == "__main__":
    cleaned_data = clean_transaction_data('data/transactions.csv')
    print(f"Cleaned dataset shape: {cleaned_data.shape}")