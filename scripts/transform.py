from pathlib import Path

import pandas as pd

from extract import load_data

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "../outputs"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def transform_categorias(categorias: pd.DataFrame) -> pd.DataFrame:
    categorias = categorias.copy()
    categorias["nombre_categoria"] = categorias["nombre_categoria"].str.strip().str.lower()
    return categorias.drop_duplicates()

def transform_productos(productos: pd.DataFrame) -> pd.DataFrame:
    productos = productos.copy()
    productos["nombre_producto"] = productos["nombre_producto"].str.strip().str.title()
    productos["material"] = productos["material"].fillna("desconocido")
    productos = productos[productos["precio"] > 0]
    return productos.drop_duplicates()

def transform_proyectos(proyectos: pd.DataFrame) -> pd.DataFrame:
    proyectos = proyectos.copy()
    proyectos["nombre_proyecto"] = proyectos["nombre_proyecto"].str.title()
    proyectos["ciudad"] = proyectos["ciudad"].str.title()
    return proyectos.drop_duplicates()

def transform_transportes(transportes: pd.DataFrame) -> pd.DataFrame:
    transportes = transportes.copy()
    transportes["tipo"] = transportes["tipo"].str.strip().str.lower()
    transportes["capacidad_kg"] = transportes["capacidad_kg"].fillna(
        transportes["capacidad_kg"].median()
    )
    return transportes[
        (transportes["costo_km"] > 0)
        & (transportes["consumo_km_litro"] > 0)
    ]

def transform_costos(costos: pd.DataFrame) -> pd.DataFrame:
    costos = costos.copy()
    costos["fecha"] = pd.to_datetime(costos["fecha"])
    costos["precio_gasolina"] = costos["precio_gasolina"].fillna(
        costos["precio_gasolina"].mean()
    )
    return costos[
        (costos["precio_gasolina"] > 15)
        & (costos["precio_gasolina"] < 35)
    ]

def transform_relaciones_envios(
    relaciones: pd.DataFrame,
    envios: pd.DataFrame,
    productos: pd.DataFrame,
    proyectos: pd.DataFrame,
    transportes: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    relaciones = relaciones.copy()
    envios = envios.copy()

    relaciones = relaciones[relaciones["cantidad"] > 0]
    relaciones = relaciones.drop_duplicates()
    envios = envios[envios["distancia_km"] > 0]

    relaciones = relaciones[relaciones["id_producto"].isin(productos["id_producto"])]
    relaciones = relaciones[relaciones["id_proyecto"].isin(proyectos["id_proyecto"])]

    envios = envios[
        envios["id_proyecto"].isin(proyectos["id_proyecto"])
        & envios["id_transporte"].isin(transportes["id_transporte"])
    ]
    return relaciones, envios

def save_outputs(dataframes: dict[str, pd.DataFrame]) -> None:
    dataframes["categorias"].to_excel(OUTPUT_DIR / "categorias_clean.xlsx", index=False)
    dataframes["productos"].to_excel(OUTPUT_DIR / "productos_clean.xlsx", index=False)
    dataframes["proyectos"].to_excel(OUTPUT_DIR / "proyectos_clean.xlsx", index=False)
    dataframes["transportes"].to_excel(OUTPUT_DIR / "transportes_clean.xlsx", index=False)
    dataframes["costos"].to_excel(OUTPUT_DIR / "costos_clean.xlsx", index=False)
    dataframes["relaciones"].to_excel(OUTPUT_DIR / "relaciones_clean.xlsx", index=False)
    dataframes["envios"].to_excel(OUTPUT_DIR / "envios_clean.xlsx", index=False)

def run_transform() -> dict[str, pd.DataFrame]:
    datos = load_data()

    categorias = transform_categorias(datos["categorias"])
    productos = transform_productos(datos["productos"])
    proyectos = transform_proyectos(datos["proyectos"])
    transportes = transform_transportes(datos["transportes"])
    costos = transform_costos(datos["costos"])
    relaciones, envios = transform_relaciones_envios(
        datos["relaciones"],
        datos["envios"],
        productos,
        proyectos,
        transportes,
    )

    resultado = {
        "categorias": categorias,
        "productos": productos,
        "proyectos": proyectos,
        "transportes": transportes,
        "costos": costos,
        "relaciones": relaciones,
        "envios": envios,
    }
    save_outputs(resultado)
    return resultado

if __name__ == "__main__":
    run_transform()