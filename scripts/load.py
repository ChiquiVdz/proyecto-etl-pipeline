from pathlib import Path
import sqlite3

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "../outputs"
DB_PATH = BASE_DIR / "../proyecto.db"


def load_to_database():
	with sqlite3.connect(DB_PATH) as conn:
		categorias = pd.read_excel(OUTPUT_DIR / "categorias_clean.xlsx")
		productos = pd.read_excel(OUTPUT_DIR / "productos_clean.xlsx")
		proyectos = pd.read_excel(OUTPUT_DIR / "proyectos_clean.xlsx")
		relaciones = pd.read_excel(OUTPUT_DIR / "relaciones_clean.xlsx")
		transportes = pd.read_excel(OUTPUT_DIR / "transportes_clean.xlsx")
		envios = pd.read_excel(OUTPUT_DIR / "envios_clean.xlsx")
		costos = pd.read_excel(OUTPUT_DIR / "costos_clean.xlsx")

		categorias.to_sql("categorias", conn, if_exists="replace", index=False)
		productos.to_sql("productos", conn, if_exists="replace", index=False)
		proyectos.to_sql("proyectos", conn, if_exists="replace", index=False)
		relaciones.to_sql("producto_proyecto", conn, if_exists="replace", index=False)
		transportes.to_sql("transportes", conn, if_exists="replace", index=False)
		envios.to_sql("envios", conn, if_exists="replace", index=False)
		costos.to_sql("costos", conn, if_exists="replace", index=False)


if __name__ == "__main__":
	load_to_database()