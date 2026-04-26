import csv

with open('c:/Users/Marcos/Documents/LithiumBateriasPro/reporte mercadopago.csv', 'r') as f:
    reader = csv.DictReader(f, delimiter=';')
    ingresos = 0
    egresos = 0
    for row in reader:
        try:
            val = float(row['REAL_AMOUNT'])
            date = row['TRANSACTION_DATE']
            if "2026-04" in date:
                if val > 0:
                    ingresos += val
                else:
                    egresos += abs(val)
        except:
            pass
    print(f"Abril Ingresos: {ingresos}")
    print(f"Abril Egresos: {egresos}")
    print(f"Balance Abril: {ingresos - egresos}")
