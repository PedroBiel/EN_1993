"""
EN 1993-1-8:2005

EUROCÓDIGO 3: PROYECTO DE ESTRUCTURAS DE ACERO

PARTE 1-8: UNIONES

SECCIÓN 3. CONEXIONES CON TORNILLOS O BULONES

PARTE 3.1. TORNILLOS, TUERCAS Y ARANDELAS

LÍMITE ELÁSTICO f.yb Y RESISTENCIA ÚLTIMA A TRACCIÓN f.ub PARA TORNILLOS

DATOS DE LA BASE DE DATOS tornillos.db, TABLA EN_1993_1_8_fyb_fub

27/09/2024

__author__ = Pedro Biel

__version__ = 0.0.0

__email__ = pedro.biel@abalsirengineering.com
"""

import pandas as pd
from src.utils.paths import Paths
from src.utils.sqlitepandasdf import SQLitePandasDF


class DatosEN1993_1_8:
    def __init__(self) -> None:
        """
        EN 1993-1-8:2005

        EUROCÓDIGO 3: PROYECTO DE ESTRUCTURAS DE ACERO

        PARTE 1-8: UNIONES

        SECCIÓN 3. CONEXIONES CON TORNILLOS O BULONES

        PARTE 3.1. TORNILLOS, TUERCAS Y ARANDELAS

        LÍMITE ELÁSTICO f.yb Y RESISTENCIA ÚLTIMA A TRACCIÓN f.ub PARA TORNILLOS

        DATOS DE LA BASE DE DATOS tornillos.db, TABLA EN_1993_1_8_fyb_fub

        Clase para gestionar los datos de la tabla 'EN_1993_1_8_fyb_fub' de la base de datos 'tornillos.db'.
        Contiene valores del límite elástico mínimo (f.yb) y resistencia última a tracción (f.ub) de los tornillos.
        """
        # Ruta a la base de datos de tornillos
        self.ruta_datos = f'{Paths.data}\\'
        self.tornillos_db = 'tornillos.db'
        self.tabla = 'EN_1993_1_8_fyb_fub'

        # Clase para gestionar la conexión a SQLite
        self.sql_pd = SQLitePandasDF

        # Cache para almacenar el DataFrame cargado
        self._df_cache = None

    def _load_dataframe(self) -> pd.DataFrame:
        """
        Carga el DataFrame desde la base de datos SQLite y lo cachea para futuras llamadas.

        :return: DataFrame con los datos de la tabla.
        """
        if self._df_cache is None:  # Solo cargar si el DataFrame no está en cache
            sql_pd = self.sql_pd(f'{self.ruta_datos}{self.tornillos_db}', self.tabla)
            self._df_cache = sql_pd.sql_to_df()
        return self._df_cache

    def grados(self) -> list[str]:
        """
        Obtiene la lista de grados del acero (columna 'Bolt_class').

        :return: Lista de grados de acero.
        """
        df = self._load_dataframe()
        return df['Bolt_class'].to_list()

    def limites_elasticos(self) -> list[int]:
        """
        Obtiene la lista de valores de límite elástico f.yb (columna 'fyb_N/mm2').

        :return: Lista de valores f.yb en N/mm².
        """
        df = self._load_dataframe()
        return df['fyb_N/mm2'].to_list()

    def limite_elastico(self, grado: str) -> int:
        """
        Obtiene el valor del límite elástico f.yb para un grado de acero específico.

        :param grado: Grado de acero.
        :return: Valor f.yb en N/mm².
        """
        df = self._load_dataframe()
        return df.loc[df['Bolt_class'] == grado, 'fyb_N/mm2'].item()

    def resistencias_ultimas_traccion(self) -> list[int]:
        """
        Obtiene la lista de valores de resistencia última a tracción f.ub (columna 'fub_N/mm2').

        :return: Lista de valores f.ub en N/mm².
        """
        df = self._load_dataframe()
        return df['fub_N/mm2'].to_list()

    def resistencia_ultima_traccion(self, grado: str) -> int:
        """
        Obtiene el valor de resistencia última a tracción f.ub para un grado de acero específico.

        :param grado: Grado de acero.
        :return: Valor f.ub en N/mm².
        """
        df = self._load_dataframe()
        return df.loc[df['Bolt_class'] == grado, 'fub_N/mm2'].item()


if __name__ == '__main__':
    import random
    from prettytable import PrettyTable

    # Inicializar PrettyTable para mostrar resultados
    tabla = PrettyTable()

    # Instanciar la clase DatosEN1993_1_8
    datos = DatosEN1993_1_8()

    # Obtener los datos de la tabla (grados, límite elástico y resistencia a tracción)
    grados = datos.grados()
    limites_elasticos = datos.limites_elasticos()
    resistencias_ultimas = datos.resistencias_ultimas_traccion()

    # Añadir columnas a la tabla
    tabla.add_column('Grado', grados)
    tabla.add_column('f.yb (N/mm²)', limites_elasticos)
    tabla.add_column('f.ub (N/mm²)', resistencias_ultimas)

    # Imprimir la tabla
    print(tabla)

    # Simulación de la consulta de datos aleatorios
    for _ in range(5):
        grado = random.choice(['4.6', '4.8', '5.6', '5.8', '6.8', '8.8', '10.9'])
        f_yb = datos.limite_elastico(grado)
        f_ub = datos.resistencia_ultima_traccion(grado)
        print(f'\nGrado: {grado}')
        print(f'Límite elástico f.yb: {f_yb} N/mm²')
        print(f'Resistencia última a tracción f.ub: {f_ub} N/mm²')
