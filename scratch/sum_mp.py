import csv

with open('c:/Users/Marcos/Documents/LithiumBateriasPro/reporte mercadopago.csv', 'r') as f:
    reader = csv.DictReader(f, delimiter=';')
    total = 0
    for row in reader:
        try:
            total += float(row['REAL_AMOUNT'])
        except:
            pass
    print(f"Total Neto en CSV: {total}")
