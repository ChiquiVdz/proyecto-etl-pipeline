from pathlib import Path

import pandas as pd

from extract import load_data

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "../outputs"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

datos = load_data()

categorias = datos["categorias"]
productos = datos["productos"]
proyectos = datos["proyectos"]
relaciones = datos["relaciones"]
transportes = datos["transportes"]
costos = datos["costos"]
envios = datos["envios"]

categorias["nombre_categoria"] = (
    categorias["nombre_categoria"].str.strip().str.lower()
)

categorias = categorias.drop_duplicates()

categorias.to_excel(OUTPUT_DIR / "categorias_clean.xlsx", index=False)

productos["nombre_producto"] = productos["nombre_producto"].str.strip().str.title()
productos["material"] = productos["material"].fillna("desconocido")
productos = productos[productos["precio"] > 0]
productos = productos.drop_duplicates()

productos.to_excel(OUTPUT_DIR / "productos_clean.xlsx", index=False)

proyectos["nombre_proyecto"] = proyectos["nombre_proyecto"].str.title()
proyectos["ciudad"] = proyectos["ciudad"].str.title()
proyectos = proyectos.drop_duplicates()

proyectos.to_excel(OUTPUT_DIR / "proyectos_clean.xlsx", index=False)

transportes["tipo"] = transportes["tipo"].str.strip().str.lower()

transportes["capacidad_kg"] = transportes["capacidad_kg"].fillna(
    transportes["capacidad_kg"].median()
)

transportes = transportes[
    (transportes["costo_km"] > 0) &
    (transportes["consumo_km_litro"] > 0)
]

transportes.to_excel(OUTPUT_DIR / "transportes_clean.xlsx", index=False)

costos["fecha"] = pd.to_datetime(costos["fecha"])

costos["precio_gasolina"] = costos["precio_gasolina"].fillna(
    costos["precio_gasolina"].mean()
)

costos = costos[
    (costos["precio_gasolina"] > 15) &
    (costos["precio_gasolina"] < 35)
]

costos.to_excel(OUTPUT_DIR / "costos_clean.xlsx", index=False)

relaciones = relaciones[relaciones["cantidad"] > 0]
relaciones = relaciones.drop_duplicates()

envios = envios[envios["distancia_km"] > 0]

relaciones = relaciones[
    relaciones["id_producto"].isin(productos["id_producto"])
]

relaciones = relaciones[
    relaciones["id_proyecto"].isin(proyectos["id_proyecto"])
]

envios = envios[
    envios["id_proyecto"].isin(proyectos["id_proyecto"]) &
    envios["id_transporte"].isin(transportes["id_transporte"])
]

relaciones.to_excel(OUTPUT_DIR / "relaciones_clean.xlsx", index=False)
envios.to_excel(OUTPUT_DIR / "envios_clean.xlsx", index=False)