import requests
import json
def obtener_datos_historicos(fecha):
    url = f"https://api.coingecko.com/api/v3/coins/bitcoin/history?date={fecha}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            # Extraer precios en USD y EUR, y capitalización de mercado
            price_usd = data.get('market_data', {}).get('current_price', {}).get('usd', None)
            price_eur = data.get('market_data', {}).get('current_price', {}).get('eur', None)
            market_cap = data.get('market_data', {}).get('market_cap', {}).get('usd', None)
            return {
                "date": fecha,
                "price_usd": price_usd,
                "price_eur": price_eur,
                "market_cap": market_cap
            }
        else:
            print(f"Error al obtener datos para la fecha {fecha}: {response.status_code}")
            return {
                "date": fecha,
                "price_usd": None,
                "price_eur": None,
                "market_cap": None
            }
    except Exception as e:
        print(f"Excepción al obtener datos para la fecha {fecha}: {str(e)}")
        return {
            "date": fecha,
            "price_usd": None,
            "price_eur": None,
            "market_cap": None
        }

#Lista para almacenar los datos
datos_bitcoin = []

#Obtener los datos para cada fecha
for fecha in fechas:
    datos = obtener_datos_historicos(fecha)
    datos_bitcoin.append(datos)

#Guardar los datos en un archivo JSON
with open('bitcoin_historical_data.json', 'w') as f:
    json.dump({"data": datos_bitcoin}, f, indent=4)

print("Datos guardados en bitcoin_historical_data.json")