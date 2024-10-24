"""
EN 1993-1-8:2005

EUROCÓDIGO 3: PROYECTO DE ESTRUCTURAS DE ACERO

PARTE 1-8: UNIONES

SECCIÓN 3. CONEXIONES CON TORNILLOS O BULONES

PARTE 3.5. DISPOSICIÓN DE LOS TALADROS PARA LOS TORNILLOS

06/05/2024

__author__ = Pedro Biel

__version__ = 0.0.0

__email__ = pedro.biel@abalsirengineering.com
"""

class DisposicionTaladros:

    def __init__(self, d_0: float, t: float) -> None:
        """
        EN 1993-1-8 EUROCÓDIGO 3: PROYECTO DE ESTRUCTURAS DE ACERO

        PARTE 1-8: UNIONES

        SECCIÓN 3. CONEXIONES CON TORNILLOS O BULONES

        PARTE 3.5. DISPOSICIÓN DE LOS TALADROS PARA LOS TORNILLOS

        :param d_0: [mm] Diámetro del taladro del tornillo
        :param t: [mm] Espesor de la chapa
        """

        if d_0 <= 0:
            raise ValueError(":( El diámetro del taladro debe ser mayor que cero.")
        if t <= 0:
            raise ValueError(":( El espesor de la chapa debe ser mayor que cero.")

        self.d_0 = d_0
        self.t = t

    # e.1
    def distancia_centro_extremo_direccion_carga_minima(self) -> float:
        """
        Distancia mínima desde el centro de un taladro del pasador o elemento de sujeción al extremo adyacente de
        cualquier elemento, medido en la dirección de transmisión de la carga. Figura A26.3.1.

        :return: e_1; [mm]
        """

        e_1 = 1.2 * self.d_0

        return e_1

    def distancia_centro_extremo_direccion_carga_maxima_en10025_ambiente_exterior(self) -> float:
        """
        Distancia máxima desde el centro de un taladro del pasador o elemento de sujeción al extremo adyacente de
        cualquier elemento, medido en la dirección de transmisión de la carga, para aceros conforme EN 10025 expuestos
        al ambiente exterior u otros agentes corrosivos. Figura A26.3.1.

        :return: e_1; [mm]
        """

        e_1 = 4 * self.t + 40

        return e_1

    def distancia_centro_extremo_direccion_carga_maxima_en10025_no_ambiente_exterior(self) -> str:
        """
        Distancia máxima desde el centro de un taladro del pasador o elemento de sujeción al extremo adyacente de
        cualquier elemento, medido en la dirección de transmisión de la carga, para aceros conforme EN 10025 no
        expuestos al ambiente exterior u otros agentes corrosivos. Figura A26.3.1.

        :return: e_1; [mm]
        """

        e_1 = '--'

        return e_1

    def distancia_centro_extremo_direccion_carga_maxima_en10025_5(self) -> float:
        """
        Distancia máxima desde el centro de un taladro del pasador o elemento de sujeción al extremo adyacente de
        cualquier elemento, medido en la dirección de transmisión de la carga, para aceros conforme EN 10025-5 sin
        proteger. Figura A26.3.1.

        :return: e_1; [mm]
        """

        e_11 = 8 * self.t
        e_12 = 125
        e_1 = max(e_11, e_12)

        return e_1

    # e.2
    def distancia_centro_extremo_direccion_perpendicular_carga_minima(self) -> float:
        """
        Distancia mínima desde el centro de un taladro del pasador o elemento de sujeción al borde adyacente de cualquier
        elemento, medido en ángulo recto respecto a la dirección de la transferencia de la carga. Figura A26.3.1.

        :return: e_2; [mm]
        """

        e_2 = 1.2 * self.d_0

        return e_2

    def distancia_centro_extremo_direccion_perpendicular_carga_maxima_en10025_ambiente_exterior(self) -> float:
        """
        Distancia máxima desde el centro de un taladro del pasador o elemento de sujeción al extremo adyacente de
        cualquier elemento, medido en ángulo recto respecto a la dirección de la transferencia de la carga, para aceros
        conforme EN 10025 expuestos al ambiente exterior u otros agentes corrosivos. Figura A26.3.1.

        :return: e_2; [mm]
        """

        e_2 = 4 * self.t + 40

        return e_2

    def distancia_centro_extremo_direccion_perpendicular_carga_maxima_en10025_no_ambiente_exterior(self) -> str:
        """
        Distancia máxima desde el centro de un taladro del pasador o elemento de sujeción al extremo adyacente de
        cualquier elemento, medido en ángulo recto respecto a la dirección de la transferencia de la carga, para aceros
        conforme EN 10025 no expuestos al ambiente exterior u otros agentes corrosivos. Figura A26.3.1.

        :return: e_2; [mm]
        """

        e_2 = '--'

        return e_2

    def distancia_centro_extremo_direccion_perpendicular_carga_maxima_en10025_5(self) -> float:
        """
        Distancia máxima desde el centro de un taladro del pasador o elemento de sujeción al extremo adyacente de
        cualquier elemento, medido en ángulo recto respecto a la dirección de la transferencia de la carga, para aceros
        conforme EN 10025-5 sin proteger. Figura A26.3.1.

        :return: e_2; [mm]
        """

        e_21 = 8 * self.t
        e_22 = 125
        e_2 = max(e_21, e_22)

        return e_2

    # e.3
    def distancia_eje_taladro_alargado_extremo_minima(self) -> float:
        """
        Distancia mínima desde el eje de un taladro alargado al extremo o borde adyacente de cualquier elemento.
        Figura A26.3.1.

        :return: e_3; [mm]
        """

        e_3 = 1.5 * self.d_0

        return e_3

    def distancia_eje_taladro_alargado_extremo_maxima_en10025_ambiente_exterior(self) -> str:
        """
        Distancia máxima desde el eje de un taladro alargado al extremo o borde adyacente de cualquier elemento, para
        aceros conforme EN 10025 expuestos al ambiente exterior u otros agentes corrosivos. Figura A26.3.1.

        :return: e_3; [mm]
        """

        e_3 = '--'

        return e_3

    def distancia_eje_taladro_alargado_extremo_maxima_en10025_no_ambiente_exterior(self) -> str:
        """
        Distancia máxima desde el eje de un taladro alargado al extremo o borde adyacente de cualquier elemento, para
        aceros conforme EN 10025 no expuestos al ambiente exterior u otros agentes corrosivos. Figura A26.3.1.

        :return: e_3; [mm]
        """

        e_3 = '--'

        return e_3

    def distancia_eje_taladro_alargado_extremo_maxima_en10025_5(self) -> str:
        """
        Distancia máxima desde el eje de un taladro alargado al extremo o borde adyacente de cualquier elemento, para
        aceros conforme EN 10025-5 sin proteger. Figura A26.3.1.

        :return: e_3; [mm]
        """

        e_3 = '--'

        return e_3

    # e.4
    def distancia_centro_radio_alargado_extremo_minima(self) -> float:
        """
        Distancia mínima desde el centro del radio de un taladro alargado al extremo o al borde adyacente de cualquier
        elemento. Figura A26.3.1.

        :return: e_4; [mm]
        """

        e_4 = 1.5 * self.d_0

        return e_4

    def distancia_centro_radio_alargado_extremo_maxima_en10025_ambiente_exterior(self) -> str:
        """
        Distancia máxima desde el centro del radio de un taladro alargado al extremo o al borde adyacente de cualquier
        elemento, para aceros conforme EN 10025 expuestos al ambiente exterior u otros agentes corrosivos.
        Figura A26.3.1.

        :return: e_4; [mm]
        """

        e_4 = '--'

        return e_4

    def distancia_centro_radio_alargado_extremo_maxima_en10025_no_ambiente_exterior(self) -> str:
        """
        Distancia máxima desde el centro del radio de un taladro alargado al extremo o al borde adyacente de cualquier
        elemento, para aceros conforme EN 10025 no expuestos al ambiente exterior u otros agentes corrosivos.
        Figura A26.3.1.

        :return: e_4; [mm]
        """

        e_4 = '--'

        return e_4

    def distancia_centro_radio_alargado_extremo_maxima_en10025_5(self) -> str:
        """
        Distancia máxima desde el centro del radio de un taladro alargado al extremo o al borde adyacente de cualquier
        elemento, para aceros conforme EN 10025-5 sin proteger. Figura A26.3.1.

        :return: e_4; [mm]
        """

        e_4 = '--'

        return e_4

    # p.1
    def espacio_entre_centros_minimo(self) -> float:
        """
        Espacio mínimo entre centros de pasadores o elementos de fijación en una fila en la dirección de la
        transferencia de la carga. Figura A26.3.1.

        :return: p_1; [mm]
        """

        p_1 = 2.2 * self.d_0

        return p_1

    def espacio_entre_centros_maximo_en10025_ambiente_exterior(self) -> float:
        """
        Espacio máximo desde el centro del radio de un taladro alargado al extremo o al borde adyacente de cualquier
        elemento, para aceros conforme EN 10025 expuestos al ambiente exterior u otros agentes corrosivos.
        Figura A26.3.1.

        :return: p_1; [mm]
        """

        p_11 = 14 * self.t
        p_12 = 200
        p_1 = min(p_11, p_12)

        return p_1

    def espacio_entre_centros_maximo_en10025_no_ambiente_exterior(self) -> float:
        """
        Espacio máximo desde el centro del radio de un taladro alargado al extremo o al borde adyacente de cualquier
        elemento, para aceros conforme EN 10025 no expuestos al ambiente exterior u otros agentes corrosivos.
        Figura A26.3.1.

        :return: p_1; [mm]
        """

        p_11 = 14 * self.t
        p_12 = 200
        p_1 = min(p_11, p_12)

        return p_1

    def espacio_entre_centros_maximo_en10025_5(self) -> float:
        """
        Espacio máximo desde el centro del radio de un taladro alargado al extremo o al borde adyacente de cualquier
        elemento, para aceros conforme EN 10025-5 sin proteger. Figura A26.3.1.

        :return: p_1; [mm]
        """

        p_11 = 14 * self.t
        p_12 = 175
        p_1 = min(p_11, p_12)

        return p_1

    # p.1,0
    def espacio_entre_centros_fila_exterior_minimo(self) -> str:
        """
        Espacio mínimo entre centros de pasadores o elementos de fijación en una fila en la dirección de la
        transferencia de la carga. Figura A26.3.1.

        :return: p_10; [mm]
        """

        p_10 = '--'

        return p_10

    def espacio_entre_centros_fila_exterior_maximo_en10025_ambiente_exterior(self) -> float:
        """
        Espacio máximo entre los centros de los pasadores o elementos de fijación en una fila exterior en la dirección
        de la transferencia de la carga, para aceros conforme EN 10025 expuestos al ambiente exterior u otros agentes
        corrosivos. Figura A26.3.1.

        :return: p_10; [mm]
        """

        p_101 = 14 * self.t
        p_102 = 200
        p_10 = min(p_101, p_102)

        return p_10

    def espacio_entre_centros_fila_exterior_maximo_en10025_no_ambiente_exterior(self) -> str:
        """
        Espacio máximo entre los centros de los pasadores o elementos de fijación en una fila exterior en la dirección
        de la transferencia de la carga, para aceros conforme EN 10025 no expuestos al ambiente exterior u otros
        agentes corrosivos. Figura A26.3.1.

        :return: p_10; [mm]
        """

        p_10 = '--'

        return p_10

    def espacio_entre_centros_fila_exterior_maximo_en10025_5(self) -> str:
        """
        Espacio máximo entre los centros de los pasadores o elementos de fijación en una fila exterior en la dirección
        de la transferencia de la carga, para aceros conforme EN 10025-5 sin proteger. Figura A26.3.1.

        :return: p_10; [mm]
        """

        p_10 = '--'

        return p_10

    # p.1,i
    def espacio_entre_centros_fila_interior_minimo(self) -> str:
        """
        Espacio mínimo entre los centros de los pasadores o elementos de fijación en una fila interior en la
        dirección de la transferencia de la carga. Figura A26.3.1.

        :return: p_1i; [mm]
        """

        p_1i = '--'

        return p_1i

    def espacio_entre_centros_fila_interior_maximo_en10025_ambiente_exterior(self) -> float:
        """
        Espacio máximo entre los centros de los pasadores o elementos de fijación en una fila interior en la
        dirección de la transferencia de la carga, para aceros conforme EN 10025 expuestos al ambiente exterior u otros
        agentes corrosivos. Figura A26.3.1.

        :return: p_1i; [mm]
        """

        p_1i1 = 28 * self.t
        p_1i2 = 200
        p_1i = min(p_1i1, p_1i2)

        return p_1i

    def espacio_entre_centros_fila_interior_maximo_en10025_no_ambiente_exterior(self) -> str:
        """
        Espacio máximo entre los centros de los pasadores o elementos de fijación en una fila interior en la
        dirección de la transferencia de la carga, para aceros conforme EN 10025 no expuestos al ambiente exterior u
        otros agentes corrosivos. Figura A26.3.1.

        :return: p_1i; [mm]
        """

        p_1i = '--'

        return p_1i

    def espacio_entre_centros_fila_interior_maximo_en10025_5(self) -> str:
        """
        Espacio máximo entre los centros de los pasadores o elementos de fijación en una fila interior en la dirección
        de la transferencia de la carga, para aceros conforme EN 10025-5 sin proteger. Figura A26.3.1.

        :return: p_1i; [mm]
        """

        p_1i = '--'

        return p_1i

    # p.2
    def espacio_medio_perpendicular_carga_minimo(self) -> float:
        """
        Espacio mínimo medido perpendicularmente a la dirección de la transferencia de la carga entre las líneas
        adyacentes de los pasadores o elementos de fijación. Figura A26.3.1.

        :return: p_2; [mm]
        """

        p_2 = 2.4 * self.d_0

        return p_2

    def espacio_medio_perpendicular_carga_maximo_en10025_ambiente_exterior(self) -> float:
        """
        Espacio máximo medido perpendicularmente a la dirección de la transferencia de la carga entre las líneas
        adyacentes de los pasadores o elementos de fijación, para aceros conforme EN 10025 expuestos al ambiente
        exterior u otros agentes corrosivos. Figura A26.3.1.

        :return: p_2; [mm]
        """

        p_21 = 14 * self.t
        p_22 = 200
        p_2 = min(p_21, p_22)

        return p_2

    def espacio_medio_perpendicular_carga_maximo_en10025_no_ambiente_exterior(self) -> float:
        """
        Espacio máximo medido perpendicularmente a la dirección de la transferencia de la carga entre las líneas
        adyacentes de los pasadores o elementos de fijación, para aceros conforme EN 10025 no expuestos al ambiente
        exterior u otros agentes corrosivos. Figura A26.3.1.

        :return: p_2; [mm]
        """

        p_21 = 14 * self.t
        p_22 = 200
        p_2 = min(p_21, p_22)

        return p_2

    def espacio_medio_perpendicular_carga_maximo_en10025_5(self) -> float:
        """
        Espacio máximo medido perpendicularmente a la dirección de la transferencia de la carga entre las líneas
        adyacentes de los pasadores o elementos de fijación, para aceros conforme EN 10025-5 sin proteger.
        Figura A26.3.1.

        :return: p_2; [mm]
        """

        p_21 = 14 * self.t
        p_22 = 175
        p_2 = min(p_21, p_22)

        return p_2


if __name__ == '__main__':

    import random
    from prettytable import PrettyTable

    for _ in range(5):
        d_0 = random.randint(10, 40)
        t = random.randint(10, 30)
        print('\n')
        print(f'{d_0 = } mm')
        print(f'{t   = } mm')
        tabla = PrettyTable()
        distancias = ['e.1', 'e.2', 'e.3', 'e.4', 'p.1', 'p.1,0', 'p.1,i', 'p.2']
        tabla.add_column('distancia', distancias)
        disposicion_taladros = DisposicionTaladros(d_0, t)
        e_1 = disposicion_taladros.distancia_centro_extremo_direccion_carga_minima()
        e_2 = disposicion_taladros.distancia_centro_extremo_direccion_perpendicular_carga_minima()
        e_3 = disposicion_taladros.distancia_eje_taladro_alargado_extremo_minima()
        e_4 = disposicion_taladros.distancia_centro_radio_alargado_extremo_minima()
        p_1 = disposicion_taladros.espacio_entre_centros_minimo()
        p_10 = disposicion_taladros.espacio_entre_centros_fila_exterior_minimo()
        p_1i = disposicion_taladros.espacio_entre_centros_fila_interior_minimo()
        p_2 = disposicion_taladros.espacio_medio_perpendicular_carga_minimo()
        tabla.add_column('mínimo [mm]', [e_1, e_2, e_3, e_4, p_1, p_10, p_1i, p_2])
        e_1 = disposicion_taladros.distancia_centro_extremo_direccion_carga_maxima_en10025_ambiente_exterior()
        e_2 = disposicion_taladros.distancia_centro_extremo_direccion_perpendicular_carga_maxima_en10025_ambiente_exterior()
        e_3 = disposicion_taladros.distancia_eje_taladro_alargado_extremo_maxima_en10025_ambiente_exterior()
        e_4 = disposicion_taladros.distancia_centro_radio_alargado_extremo_maxima_en10025_ambiente_exterior()
        p_1 = disposicion_taladros.espacio_entre_centros_maximo_en10025_ambiente_exterior()
        p_10 = disposicion_taladros.espacio_entre_centros_fila_exterior_maximo_en10025_ambiente_exterior()
        p_1i = disposicion_taladros.espacio_entre_centros_fila_interior_maximo_en10025_ambiente_exterior()
        p_2 = disposicion_taladros.espacio_medio_perpendicular_carga_maximo_en10025_ambiente_exterior()
        tabla.add_column('máximo 1 [mm]', [e_1, e_2, e_3, e_4, p_1, p_10, p_1i, p_2])
        e_1 = disposicion_taladros.distancia_centro_extremo_direccion_carga_maxima_en10025_no_ambiente_exterior()
        e_2 = disposicion_taladros.distancia_centro_extremo_direccion_perpendicular_carga_maxima_en10025_no_ambiente_exterior()
        e_3 = disposicion_taladros.distancia_eje_taladro_alargado_extremo_maxima_en10025_no_ambiente_exterior()
        e_4 = disposicion_taladros.distancia_centro_radio_alargado_extremo_maxima_en10025_no_ambiente_exterior()
        p_1 = disposicion_taladros.espacio_entre_centros_maximo_en10025_no_ambiente_exterior()
        p_10 = disposicion_taladros.espacio_entre_centros_fila_exterior_maximo_en10025_no_ambiente_exterior()
        p_1i = disposicion_taladros.espacio_entre_centros_fila_interior_maximo_en10025_no_ambiente_exterior()
        p_2 = disposicion_taladros.espacio_medio_perpendicular_carga_maximo_en10025_no_ambiente_exterior()
        tabla.add_column('máximo 2 [mm]', [e_1, e_2, e_3, e_4, p_1, p_10, p_1i, p_2])
        e_1 = disposicion_taladros.distancia_centro_extremo_direccion_carga_maxima_en10025_5()
        e_2 = disposicion_taladros.distancia_centro_extremo_direccion_perpendicular_carga_maxima_en10025_5()
        e_3 = disposicion_taladros.distancia_eje_taladro_alargado_extremo_maxima_en10025_5()
        e_4 = disposicion_taladros.distancia_centro_radio_alargado_extremo_maxima_en10025_5()
        p_1 = disposicion_taladros.espacio_entre_centros_maximo_en10025_5()
        p_10 = disposicion_taladros.espacio_entre_centros_fila_exterior_maximo_en10025_5()
        p_1i = disposicion_taladros.espacio_entre_centros_fila_interior_maximo_en10025_5()
        p_2 = disposicion_taladros.espacio_medio_perpendicular_carga_maximo_en10025_5()
        tabla.add_column('máximo 3 [mm]', [e_1, e_2, e_3, e_4, p_1, p_10, p_1i, p_2])
        print(tabla)
