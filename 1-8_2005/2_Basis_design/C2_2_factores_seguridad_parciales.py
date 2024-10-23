"""
COEFICIENTES PARCIALES DE SEGURIDAD PARA LAS UNIONES DEL FICHERO
EN_1993_1_8_coeficientes_parciales_seguridad_uniones.json

EN 1993-1-8:2005

EUROCÓDIGO 3: PROYECTO DE ESTRUCTURAS DE ACERO

PARTE 1-8: UNIONES

SECCIÓN 2. BASES DE CÁLCULO

PARTE 2.2. REQUISITOS GENERALES

TABLA 2.1: COEFICIENTES PARCIALES DE SEGURIDAD PARA LAS UNIONES

DATOS DE LA BASE DE DATOS tornillos.db, TABLA EN_1993_1_8_fyb_fub

09/10/2024

__author__ = Pedro Biel

__version__ = 0.0.0

__email__ = pedro.biel@abalsirengineering.com
"""

from src.utils.paths import Paths
from src.utils.dictjson import JsonDict


class DatosCoeficientesParcialesSeguridad:

    def __init__(self) -> None:
        """
        Clase para gestionar los datos de los coeficientes parciales de seguridad para las uniones, desde el fichero
        json 'EN_1993_1_8_coeficientes_parciales_seguridad.json'. Contiene valores los coeficientes parciales de
        seguridad para:

        +----------+-------------------------------------------------------------------------+
        | γ.M2     | Resistencia de los tornillos, bulones, soldaduras y chapas              |
        +----------+-------------------------------------------------------------------------+
        | γ.M3     | Resistencia al deslizamiento en estado límite último (Categoría C)      |
        +----------+-------------------------------------------------------------------------+
        | γ.M3,ser | Resistencia al deslizamiento en estado límite de servicio (Categoría B) |
        +----------+-------------------------------------------------------------------------+
        | γ.M4     | Resistencia de un tornillo de inyección                                 |
        +----------+-------------------------------------------------------------------------+
        | γ.M5     | Resistencia de uniones en vigas en celosía de perfiles tubulares        |
        +----------+-------------------------------------------------------------------------+
        | γ.M6,ser | Resistencia de bulones enn estado límite de servicio                    |
        +----------+-------------------------------------------------------------------------+
        | γ.M7     | Precarga de tornillos de alta resistencia                               |
        +----------+-------------------------------------------------------------------------+
        | γ.c,pt   | Situación de cálculo de hormigón permanente o transitoria               |
        +----------+-------------------------------------------------------------------------+
        | γ.c,a    | Situación de cálculo de hormigón accidental                             |
        +----------+-------------------------------------------------------------------------+

        γ.c,pt y γ.c,a según EN 1992-1-1:2004, tabla 2.1N

        """

        self.ruta_datos = f'{Paths.data}\\'
        self.coeficientes_gamma = 'EN_1993_1_8_coeficientes_parciales_seguridad_uniones.json'

        # Carga los datos del JSON en el constructor y los almacena en un atributo de instancia
        self._coeficientes = self._cargar_coeficientes()

    def _cargar_coeficientes(self) -> dict:
        """
        Carga los coeficientes parciales de seguridad desde el archivo JSON.

        :return: Diccionario con los coeficientes.
        """
        try:
            gammas_json_to_dict = JsonDict(self.ruta_datos, self.coeficientes_gamma)
            return gammas_json_to_dict.json_to_dict()
        except FileNotFoundError:
            raise Exception(f'No se encontró el archivo {self.coeficientes_gamma}')
        except KeyError as e:
            raise Exception(f'Error en el formato del JSON: clave {str(e)} no encontrada')

    def obtener_coeficiente(self, clave: str) -> float:
        """
        Devuelve el valor del coeficiente solicitado, si existe.

        :param clave: La clave del coeficiente en el diccionario.
        :return: Valor del coeficiente o lanza una excepción si la clave no existe.
        """
        try:
            return self._coeficientes[clave]
        except KeyError:
            raise KeyError(f'El coeficiente "{clave}" no se encuentra en el archivo JSON')

    def gamma_M2(self) -> float:
        """
        Coeficiente parcial de seguridad para la resistencia de los tornillos, bulones, soldaduras y chapas γ.M2.
        """
        return self.obtener_coeficiente('gamma_M2')

    def gamma_M3(self) -> float:
        """
        Coeficiente parcial de seguridad para la resistencia a deslizamiento en estado límite último Categoría C γ.M3.
        """
        return self.obtener_coeficiente('gamma_M3')

    def gamma_M3ser(self) -> float:
        """
        Coeficiente parcial de seguridad para la resistencia a deslizamiento en estado límite de servicio Categoría B
        γ.M3,ser.
        """
        return self.obtener_coeficiente('gamma_M3ser')

    def gamma_M4(self) -> float:
        """
        Coeficiente parcial de seguridad para la resistencia de un tornillo de inyección γ.M4.
        """
        return self.obtener_coeficiente('gamma_M4')

    def gamma_M5(self) -> float:
        """
        Coeficiente parcial de seguridad para la resistencia de uniones en vigas de celosía de perfiles tubulares γ.M5.
        """
        return self.obtener_coeficiente('gamma_M5')

    def gamma_M6ser(self) -> float:
        """
        Coeficiente parcial de seguridad para la resistencia de bulones en estado límite de servicio γ.M6,ser.
        """
        return self.obtener_coeficiente('gamma_M6ser')

    def gamma_M7(self) -> float:
        """
        Coeficiente parcial de seguridad para precarga de tornillos de alta resistencia γ.M7.
        """
        return self.obtener_coeficiente('gamma_M7')

    def gamma_Mc_permanente_transitoria(self) -> float:
        """
        Coeficiente parcial de seguridad para la resistencia del hormigón en situaciones permanentes o transitorias
        γ.Mc.
        """
        return self.obtener_coeficiente('gamma_c_permanente_transitoria')

    def gamma_Mc_accidental(self) -> float:
        """
        Coeficiente parcial de seguridad para la resistencia del hormigón en situaciones accidentales γ.Mc.
        """
        return self.obtener_coeficiente('gamma_c_accidental')


if __name__ == '__main__':

    datos = DatosCoeficientesParcialesSeguridad()
    g_M2 = datos.gamma_M2()
    g_M3 = datos.gamma_M3()
    g_M3ser = datos.gamma_M3ser()
    g_M4 = datos.gamma_M4()
    g_M5 = datos.gamma_M5()
    g_M6ser = datos.gamma_M6ser()
    g_M7 = datos.gamma_M7()
    g_Mc_pt = datos.gamma_Mc_permanente_transitoria()
    g_Mc_a = datos.gamma_Mc_accidental()
    print(f'{g_M2    = }')
    print(f'{g_M3    = }')
    print(f'{g_M3ser = }')
    print(f'{g_M4    = }')
    print(f'{g_M5    = }')
    print(f'{g_M6ser = }')
    print(f'{g_M7    = }')
    print(f'{g_Mc_pt = }')
    print(f'{g_Mc_a  = }')