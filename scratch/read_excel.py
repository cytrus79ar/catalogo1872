import pandas as pd

try:
    df_dict = pd.read_excel('c:/Users/Marcos/Documents/LithiumBateriasPro/LISTA 4 - MOTO - AGM - SOLAR.xlsx', sheet_name=None)
    with open('c:/Users/Marcos/Documents/LithiumBateriasPro/scratch/probattery_excel.txt', 'w', encoding='utf-8') as f:
        for sheet_name, df in df_dict.items():
            f.write(f"--- SHEET: {sheet_name} ---\n")
            f.write(df.to_string())
            f.write("\n\n")
    print("Extracted successfully.")
except Exception as e:
    print(f"Error: {e}")
