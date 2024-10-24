"""
EN 1993-1-8:2005

EUROCÓDIGO 3: PROYECTO DE ESTRUCTURAS DE ACERO

PARTE 1-8: UNIONES

SECCIÓN 3. CONEXIONES CON TORNILLOS O BULONES

PARTE 3.6. RESISTENCIA DE CÁLCULO DE LOS ELEMENTOS INDIVIDUALES DE UNIÓN

TABLA 3.4 RESISTENCIA DE CÁLCULO PARA UN ELEMENTO DE FIJACIÓN SOMETIDO A CORTANTE Y/O TRACCIÓN

06/05/2024

__author__ = Pedro Biel

__version__ = 0.0.0

__email__ = pedro.biel@abalsirengineering.com
"""
import math
from math import pi


class ResistenciaCalculo:

    def __init__(
            self,
            d: float,
            A: float,
            A_s: float,
            grado: str,
            f_ub: int,
            t: float,
            f_u: int,
            g_M2: float,
    ) -> None:
        """
        EN 1993-1-8:2005

        EUROCÓDIGO 3: PROYECTO DE ESTRUCTURAS DE ACERO

        PARTE 1-8: UNIONES

        SECCIÓN 3. CONEXIONES CON TORNILLOS O BULONES

        PARTE 3.6. RESISTENCIA DE CÁLCULO DE LOS ELEMENTOS INDIVIDUALES DE UNIÓN

        TABLA 3.4 RESISTENCIA DE CÁLCULO PARA UN ELEMENTO DE FIJACIÓN SOMETIDO A CORTANTE Y/O TRACCIÓN

        :param d: [mm] Diámetro de la rosca métrica
        :param A: [mm²] Área de la sección bruta del tornillo
        :param A_s: [mm²] Área de la sección transversal neta a tracción del tornillo
        :param grado: [] Grado del material según la tabla 3.1
        :param f_ub: [N/mm²] Resistencia última a tracción del tornillo
        :param t; [mm] Espesor nominal de la chapa de unión
        :param f_u: [N/mm²] Resistencia última a tracción de la chapa
        :param g_M2: [] Coeficiente parcial de seguridad para la resistencia de los tornillos
        """

        if g_M2 <= 0:
            raise ValueError(':( g_M2 debe ser positivo.')
        if f_u <= 0:
            raise ValueError(':( f_u debe ser positivo.')

        self.d = d
        self.A = A
        self.A_s = A_s
        self.grado = grado
        self.f_ub = f_ub
        self.t = t
        self.f_u = f_u
        self.g_M2 = g_M2

    # Resistencia a cortante F.v,Rd
    def coeficiente_cortante_alfa_v(self, plano_cortante_atraviesa_rosca: bool) -> float:
        """
        Coeficiente α.v para el cálculo de la resistencia a cortante.

        :param plano_cortante_atraviesa_rosca: [] Si el plano de cortante atraviesa la parte roscada del tornillo

        :return: alfa_v; []
        """

        if plano_cortante_atraviesa_rosca:
            if self.grado in ('4.6', '5.6', '8.8'):
                alfa_v: float = 0.6
            elif self.grado in ('4.8', '5.8', '6.8', '10.9'):
                alfa_v: float = 0.5
        else:
            alfa_v: float = 0.6

        return alfa_v

    def resistencia_cortante(self, plano_cortante_atraviesa_rosca: bool) -> float:
        """
        Resistencia de cálculo para elementos de unión sujetos a cortante según la tabla 3.4.

        :param plano_cortante_atraviesa_rosca: [] Si el plano de cortante atraviesa la parte roscada del tornillo

        :return: F_vRd; [N]
        """

        alfa_v = self.coeficiente_cortante_alfa_v(plano_cortante_atraviesa_rosca)
        if plano_cortante_atraviesa_rosca:
            A: float = self.A_s
        else:
            A: float = self.A
        F_vRd: float = alfa_v * self.f_ub * A / self.g_M2

        return F_vRd

    # Capacidad resistente F.b,Rd
    def coeficiente_k_1(self, e_2: float, p_2: float, d_0: float, posicion: str) -> float:
        """
        Coeficiente k.1 para tornillos perpendiculares a la dirección de la transmisión de la carga.

        :param e_2: [mm] Distancia desde el centro de un taladro al extremo adyacente, medido en ángulo recto respecto
         a la dirección de la transferencia de la carga
        :param p_2: [mm] Espacio medido perpendicularmente a la dirección de la transferencia de la carga entre las
         líneas adyacentes de los pasadores o elementos de fijación
        :param d_0: [mm] Diámetro del taladro del tornillo
        :param posicion: [] Posición de los tornillos: situados en los bordes exteriores (edge) o en el interior (inner)
         de las alineaciones de tornillos en la dirección de la carga

        :return: k_1; []
        """

        if d_0 <= 0:
            raise ValueError(':( d_0 debe ser positivo.')

        if posicion == 'edge':  # Tornillos alineados perpendicularmente a la dirección de la carga situados en las
            # alineaciones exteriores
            k_11: float = 2.8 * e_2 / d_0 - 1.7
            k_12: float = 1.4 * p_2 / d_0 - 1.7
            k_13: float = 2.5
            k_1: float = min(k_11, k_12, k_13)
        elif posicion == 'inner':  # Tornillos alineados perpendicularmente a la dirección de la carga situados en
            # las alineaciones interiores
            k_11: float = 1.4 * p_2 / d_0 - 1.7
            k_12: float = 2.5
            k_1: float = min(k_11, k_12)
        else:
            # print('Algo ha ido mal :(')
            raise ValueError(':( Posición no válida. Debe ser "edge" o "inner".')

        return k_1

    def coeficiente_alfa_d(self, e_1: float, p_1: float, d_0: float, posicion: str) -> float:
        """
        Coeficiente α.d para tornillos alineados en la dirección de la transmisión de la carga.

        :param e_1: [mm] Distancia desde el centro de un taladro al extremo adyacente, medido en la dirección de la
         transferencia de la carga
        :param p_1: [mm] Espacio medido en la dirección de la transferencia de la carga entre las líneas adyacentes de
         los pasadores o elementos de fijación
        :param d_0: [mm] Diámetro del taladro del tornillo
        :param posicion: [] Posición de los tornillos: situados en el borde final (end) o en el interior (inner) de las
         alineaciones de tornillos perpendiculares a la dirección de la carga

        :return: alfa_d; []
        """

        if d_0 <= 0:
            raise ValueError(':( d_0 debe ser positivo.')

        if posicion == 'end':  # Tornillos alineados en la dirección de la carga situados en la alineación final
            alfa_d: float = e_1 / (3 * d_0)
        elif posicion == 'inner':  # Tornillos alineados en la dirección de la carga situados en las alineaciones interiores
            alfa_d: float = p_1 / (3 * d_0) - 1 / 4
        else:
            print('Algo ha ido mal :(')

        return alfa_d

    def coeficiente_alfa_b(self, e_1: float, p_1: float, d_0: float, posicion: str) -> float:
        """
        Coeficiente α.b para tornillos alineados en la dirección de la transmisión de la carga  y situados en el extremo
        final de la alineación.

        :param e_1: [mm] Distancia desde el centro de un taladro al extremo adyacente, medido en la dirección de la
         transferencia de la carga
        :param p_1: [mm] Espacio medido en la dirección de la transferencia de la carga entre las líneas adyacentes de
         los pasadores o elementos de fijación
        :param d_0: [mm] Diámetro del taladro del tornillo
        :param posicion: [] Posición de los tornillos: situados en el borde final (end) o en el interior (inner) de las
         alineaciones de tornillos perpendiculares a la dirección de la carga

        :return: alfa_b; []
        """

        if d_0 <= 0:
            raise ValueError(':( d_0 debe ser positivo.')

        alfa_d: float = self.coeficiente_alfa_d(e_1, p_1, d_0, posicion)
        alfa_b: float = min(alfa_d, self.f_ub / self.f_u, 1.0)

        return alfa_b

    def capacidad_resistente_F_bRd(
            self, e_1: float, e_2: float, p_1: float, p_2: float, d_0: float, posicion_k1: str, posicion_ad: str
    ) -> float:
        """
        Capacidad resistente para elementos de unión según la tabla 3.4.

        :param e_1: [mm] Distancia desde el centro de un taladro al extremo adyacente, medido en la dirección de la
         transferencia de la carga
        :param e_2: [mm] Distancia desde el centro de un taladro al extremo adyacente, medido en ángulo recto respecto
         a la dirección de la transferencia de la carga
        :param p_1: [mm] Espacio medido en la dirección de la transferencia de la carga entre las líneas adyacentes de
         los pasadores o elementos de fijación
        :param p_2: [mm] Espacio medido perpendicularmente a la dirección de la transferencia de la carga entre las
         líneas adyacentes de los pasadores o elementos de fijación
        :param d_0: [mm] Diámetro del taladro del tornillo
        :param posicion_ad: [] Posición de los tornillos: situados en los bordes exteriores (edge) o en el interior
         (inner) de las alineaciones de tornillos en la dirección de la carga
        :param posicion_k1: [] Posición de los tornillos: situados en el borde final (end) o en el interior (inner) de
         las alineaciones de tornillos perpendiculares a la dirección de la carga

        :return: F_bRd; [N]
        """

        k_1: float = self.coeficiente_k_1(e_2, p_2, d_0, posicion_k1)
        alfa_b: float = self.coeficiente_alfa_b(e_1, p_1, d_0, posicion_ad)
        F_bRd: float = k_1 * alfa_b * self.f_u * self.d * self.t / self.g_M2

        return F_bRd

    def capacidad_resistente_taladro_holgura_F_bRd(
            self, e_1: float, e_2: float, p_1: float, p_2: float, d_0: float, posicion_k1: str, posicion_ad: str
    ) -> float:
        """
        Capacidad resistente para elementos de unión según la tabla 3.4, nota 2: Taladros con holgura (oversized holes).

        :param e_1: [mm] Distancia desde el centro de un taladro al extremo adyacente, medido en la dirección de la
         transferencia de la carga
        :param e_2: [mm] Distancia desde el centro de un taladro al extremo adyacente, medido en ángulo recto respecto
         a la dirección de la transferencia de la carga
        :param p_1: [mm] Espacio medido en la dirección de la transferencia de la carga entre las líneas adyacentes de
         los pasadores o elementos de fijación
        :param p_2: [mm] Espacio medido perpendicularmente a la dirección de la transferencia de la carga entre las
         líneas adyacentes de los pasadores o elementos de fijación
        :param d_0: [mm] Diámetro del taladro del tornillo
        :param posicion_ad: [] Posición de los tornillos: situados en los bordes exteriores (edge) o en el interior
         (inner) de las alineaciones de tornillos en la dirección de la carga
        :param posicion_k1: [] Posición de los tornillos: situados en el borde final (end) o en el interior (inner) de
         las alineaciones de tornillos perpendiculares a la dirección de la carga

        :return: F_bRd; [N]
        """

        F_bRd: float = self.capacidad_resistente_F_bRd(e_1, e_2, p_1, p_2, d_0, posicion_k1, posicion_ad)
        F_bRd_oversized: float = 0.8 * F_bRd

        return F_bRd_oversized

    def capacidad_resistente_taladro_rasgado_F_bRd(
            self, e_1: float, e_2: float, p_1: float, p_2: float, d_0: float, posicion_k1: str, posicion_ad: str
    ) -> float:
        """
        Capacidad resistente para elementos de unión según la tabla 3.4, nota 2: Taladros rasgados (slotted holes)
        cuando el eje longitudinal del taladro es perpendicular a la dirección de la fuerza transmitida.

        :param e_1: [mm] Distancia desde el centro de un taladro al extremo adyacente, medido en la dirección de la
         transferencia de la carga
        :param e_2: [mm] Distancia desde el centro de un taladro al extremo adyacente, medido en ángulo recto respecto
         a la dirección de la transferencia de la carga
        :param p_1: [mm] Espacio medido en la dirección de la transferencia de la carga entre las líneas adyacentes de
         los pasadores o elementos de fijación
        :param p_2: [mm] Espacio medido perpendicularmente a la dirección de la transferencia de la carga entre las
         líneas adyacentes de los pasadores o elementos de fijación
        :param d_0: [mm] Diámetro del taladro del tornillo
        :param posicion_ad: [] Posición de los tornillos: situados en los bordes exteriores (edge) o en el interior
         (inner) de las alineaciones de tornillos en la dirección de la carga
        :param posicion_k1: [] Posición de los tornillos: situados en el borde final (end) o en el interior (inner) de
         las alineaciones de tornillos perpendiculares a la dirección de la carga

        :return: F_bRd; [N]
        """

        if posicion_k1 not in ['edge', 'inner']:
            raise ValueError('Posición no válida. Debe ser "end" o "inner".')
        if posicion_ad not in ['end', 'inner']:
            raise ValueError('Posición no válida. Debe ser "edge" o "inner".')

        F_bRd: float = self.capacidad_resistente_F_bRd(e_1, e_2, p_1, p_2, d_0, posicion_k1, posicion_ad)
        F_bRd_slotted: float = 0.6 * F_bRd

        return F_bRd_slotted

    # Resistencia a tracción F.t,Rd
    def coeficiente_k_2(self, cabeza_avellanada: bool) -> float:
        """
        Coeficiente k.2.

        :param cabeza_avellanada: [] Tornillo con cabeza avellanada

        :return: k_2; []
        """

        if cabeza_avellanada:
            k_2: float = 0.63
        else:
            k_2: float = 0.9

        return k_2

    def resistencia_traccion_F_tRd(self, cabeza_avellanada: bool) -> float:
        """
        Resistencia a tracción para elementos de unión según la tabla 3.4.

        :param cabeza_avellanada: [] Tornillo con cabeza avellanada

        :return: F_tRd; [N]
        """

        k_2: float = self.coeficiente_k_2(cabeza_avellanada)
        F_tRd: float = k_2 * self.f_ub * self.A_s / self.g_M2

        return F_tRd

    # Resistencia a punzonamiento B.p,Rd
    def media_de_distancias_entre_vertices_y_caras_planas_d_m(self, s: float):
        """
        Media de las distancias entre los vértices y entre las caras planas de la cabeza del tornillo o de la tuerca, la
        que sea menor.

        El valor del diámetro medio d.m se calcula del siguiente modo: La distancia entre planos s de la tuerca se
        indica en la norma ISO 898-2. Ignorando de forma aproximada el redondeo de las esquinas para un hexágono
        perfecto, la relación entre la distancia entre puntos s' y la distancia entre planos s es s' = s / cos(30°) =
        1,1547 s.

        :param s: [mm] Media de las distancias entre los vértices y entre las caras planas de la cabeza del tornillo o
         de la tuerca, la que sea menor. En el caso de tornillos de cabeza hexagonal se toma la distancia entre caras
         planas.

        :return: d_m
        """

        d_m: float = 1.07735 * s  # https://eurocodeapplied.com/design/en1993/bolt-design-properties

        return d_m

    def resistencia_punzonamiento_B_pRd(self, s) -> float:
        """
        Resistencia a punzonamiento para elementos de unión según la tabla 3.4.

        :param s: [mm] Media de las distancias entre los vértices y entre las caras planas de la cabeza del tornillo o
         de la tuerca, la que sea menor. En el caso de tornillos de cabeza hexagonal se toma la distancia entre caras
         planas.

        :return: B_pRd; [N]
        """

        d_m: float = self.media_de_distancias_entre_vertices_y_caras_planas_d_m(s)
        B_pRd: float = 0.6 * pi * d_m * self.t * self.f_u / self.g_M2

        return B_pRd


if __name__ == '__main__':

    import random
    from prettytable import PrettyTable

    random.seed(42)
    tabla1 = PrettyTable()
    tabla1.field_names = ['d', 'A', 'A.s', 'grado', 'f.ub', 'f.u', 'γ.M2', 'corta rosca', 'α.v', 'F.v,Rd']
    tabla2 = PrettyTable()
    tabla2.field_names = ['d', 'A', 'A.s', 'grado', 'f.ub', 'f.u', 'γ.M2', 'd.0', 't', 'e.1', 'e.2', 'p.1', 'p.2', 'pos k1', 'pos α.d', 'k.1', 'α.d', 'α.b', 'F.bRd', 'F.bRd,holgura', 'F.bRd,rasgado']
    tabla3 = PrettyTable()
    tabla3.field_names = ['d', 'A', 'A.s', 'grado', 'f.ub', 'f.u', 'γ.M2', 'avellanada', 'k.2', 'F.t,Rd']
    tabla4 = PrettyTable()
    tabla4.field_names = ['d', 'A', 'A.s', 'grado', 'f.ub', 'f.u', 'γ.M2', 's', 'd.m', 'B.p,Rd']

    for _ in range(10):
        d = random.randint(12, 40)
        A = round(math.pi * d ** 2 / 4)
        A_s = round(0.85 * A)
        grado = random.choice(['4.6', '4.8', '5.6', '5.8', '8.8', '10.9'])
        f_ub = int(float(grado)) * 100
        t = random.randint(10, 30)
        f_u = random.choice([360, 410, 470, 550])
        g_M2 = 1.25
        resistencias = ResistenciaCalculo(d, A, A_s, grado, f_ub, t, f_u, g_M2)

        # Resistencia a cortante F.v,Rd
        plano_cortante_atraviesa_rosca = random.choice([True, False])
        a_v = resistencias.coeficiente_cortante_alfa_v(plano_cortante_atraviesa_rosca)
        F_vRd = round(resistencias.resistencia_cortante(plano_cortante_atraviesa_rosca))

        # Capacidad resistente F.b,Rd
        d_0 = d + 2
        e_1 = 1.2 * d_0
        e_2 = 1.2 * d_0
        p_1 = round(2.2 * d_0, 1)
        p_2 = 2.4 * d_0
        posicion_k1 = random.choice(['edge', 'inner'])
        posicion_alfad = random.choice(['end', 'inner'])
        k_1 = round(resistencias.coeficiente_k_1(e_2, p_2, d_0, posicion_k1), 3)
        a_d = round(resistencias.coeficiente_alfa_d(e_1, p_1, d_0, posicion_alfad), 3)
        a_b = round(resistencias.coeficiente_alfa_b(e_1, p_1, d_0, posicion_alfad), 3)
        F_bRd = round(resistencias.capacidad_resistente_F_bRd(e_1, e_2, p_1, p_2, d_0, posicion_k1, posicion_alfad))
        F_bRd_holgura = round(resistencias.capacidad_resistente_taladro_holgura_F_bRd(e_1, e_2, p_1, p_2, d_0, posicion_k1, posicion_alfad))
        F_bRd_rasgado = round(resistencias.capacidad_resistente_taladro_rasgado_F_bRd(e_1, e_2, p_1, p_2, d_0, posicion_k1, posicion_alfad))

        # Resistencia a tracción F.t,Rd
        cabeza_avellanada = random.choice([True, False])
        k_2 = resistencias.coeficiente_k_2(cabeza_avellanada)
        F_tRd = round(resistencias.resistencia_traccion_F_tRd(cabeza_avellanada))

        # Resistencia a punzonamiento B.p,Rd
        s = 1.5 * d
        d_m = round(resistencias.media_de_distancias_entre_vertices_y_caras_planas_d_m(s), 1)
        B_pRd = round(resistencias.resistencia_punzonamiento_B_pRd(s))

        # Tablas
        tabla1.add_row([d, A, A_s, grado, f_ub, f_u, g_M2, plano_cortante_atraviesa_rosca, a_v, F_vRd])
        tabla2.add_row([d, A, A_s, grado, f_ub, f_u, g_M2, d_0, t, e_1, e_2, p_1, p_2, posicion_k1, posicion_alfad, k_1, a_d, a_b, F_bRd, F_bRd_holgura, F_bRd_rasgado])
        tabla3.add_row([d, A, A_s, grado, f_ub, f_u, g_M2, cabeza_avellanada, k_2, F_tRd])
        tabla4.add_row([d, A, A_s, grado, f_ub, f_u, g_M2, s, d_m, B_pRd])
    print(tabla1)
    print(tabla2)
    print(tabla3)
    print(tabla4)
