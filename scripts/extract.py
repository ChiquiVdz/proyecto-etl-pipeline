from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "../data"


def load_data():
	categorias = pd.read_excel(DATA_DIR / "categorias.xlsx")
	productos = pd.read_excel(DATA_DIR / "productos.xlsx")
	proyectos = pd.read_excel(DATA_DIR / "proyectos.xlsx")
	relaciones = pd.read_excel(DATA_DIR / "producto_proyecto.xlsx")
	transportes = pd.read_excel(DATA_DIR / "transportes.xlsx")
	costos = pd.read_excel(DATA_DIR / "costos_operacion.xlsx")
	envios = pd.read_excel(DATA_DIR / "envios.xlsx")

	return {
		"categorias": categorias,
		"productos": productos,
		"proyectos": proyectos,
		"relaciones": relaciones,
		"transportes": transportes,
		"costos": costos,
		"envios": envios,
	}


if __name__ == "__main__":
	load_data()