"""
EN 1993-1-3:2006

EUROCÓDIGO 3: PROYECTO DE ESTRUCTURAS DE ACERO

PARTE 1-3: REGLAS GENERALES - REGLAS SUPLEMENTARIAS PARA CHAPAS Y ELEMENTOS PLEGADOS EN FRÍO

TABLA 8.4: RESISTENCIAS DE DISEÑO DE TORNILLOS

15/10/2024

__author__ = Pedro Biel

__version__ = 0.0.0

__email__ = pedro.biel@abalsirengineering.com
"""


class ResistenciasDisenoTornillos:
    def __init__(self, d: float, A_s: float, grado: str, d_0: float, t: float, f_u: float, g_M2: float) -> None:
        """
        EN 1993-1-3:2006

        EUROCÓDIGO 3: PROYECTO DE ESTRUCTURAS DE ACERO

        PARTE 1-3: REGLAS GENERALES - REGLAS SUPLEMENTARIAS PARA CHAPAS Y ELEMENTOS PLEGADOS EN FRÍO

        TABLA 8.4: RESISTENCIAS DE DISEÑO DE TORNILLOS

        :param d: [mm] Diámetro de la rosca métrica.
        :param A_s: [mm²] Área de la sección transversal neta a tracción del tornillo.
        :param grado: [] Grado del material según la tabla 3.1.
        :param d_0: [mm] Diámetro del taladro del tornillo.
        :param t: [mm] Espesor de la chapa.
        :param f_u: [N/mm²] Resistencia última a tracción.
        :param g_M2: [] Coeficiente parcial de seguridad para la resistencia de los tornillos según EN 1993-1-8:2005, tabla 2.1.
        """

        self.d = d
        self.A_s = A_s
        self.grado = grado
        self.d_0 = d_0
        self.t = t
        self.f_u = f_u
        self.g_M2 = g_M2

    # Tornillos a cortante

    def coeficiente_alfa_b(self) -> float:
        """
        Coeficiente α.b para el cálculo de la capacidad resistente.

        α.b = min(1,0; e.1/(3d))

        Se toma como valor e.1 el mínimo del rango de validez e.1 = 1,0 * d.0

        :return: alfa_b; []
        """

        rango_validez = RangoValidez(self.d_0)
        e_1: float = rango_validez.rango_validez_e_1()
        alfa_b_1: float = 1.0
        alfa_b_2: float = e_1 / (3 * self.d)
        alfa_b: float = min(alfa_b_1, alfa_b_2)

        return alfa_b

    def coeficiente_k_t(self) -> float:
        """
        Coeficiente k.t para el cálculo de la capacidad resistente.

        k.t = (0,8 t + 1,5) / 2,5 para 0,75 mm ≤ t ≤ 1,25 mm

        k.t = 1,0 para t > 1,25 mm

        Nota: Se considera también t = 0,5 mm ya que está incluido en la lista de espesores de chapa DIN 1543.

        :return: k_t; []
        """

        if self.t <= 1.25:
            k_t: float = (0.8 * self.t + 1.5) / 2.5
        else:
            k_t: float = 1.0

        return k_t

    def capacidad_resitente_F_bRd(self) -> float:
        """
        Capacidad resistente F.bRd para elementos de unión con chapas de espesor t < 3 mm.

        F.b,Rd = 2,5 α.b k.t f.u d t / γ.M2

        :return: F_bRd; [N]
        """

        alfa_b: float = self.coeficiente_alfa_b()
        k_t: float = self.coeficiente_k_t()

        F_bRd: float = 2.5 * alfa_b * k_t * self.f_u * self.d * self.t / self.g_M2

        return F_bRd

    def area_transversal_neta(self) -> float:
        """
        Área de la sección transversal neta de la parte conectada.

        Se considera el área transversal neta unitaria entre dos tornillos.

        A.net = (p.2 - d.0) t

        :return A_net: [mm²]
        """

        rango_validez = RangoValidez(self.d_0)
        p_2: float = rango_validez.rango_validez_p_2()
        A_net: float = (p_2 - self.d_0) * self.t

        return A_net

    def relacion_tornillos_seccion_neta_entre_tornillos_totales(self) -> tuple[float, float, float, float]:
        """
        Relación del nº de tornillos en el área transversal neta y del nº de tornillos totales en la unión.

        r = (nº tornillos en el área transversal neta) / (nº tornillos totales en la unión)

        Nota: Se considera r = 2, 1, 1/2, 1/3

        :return: r; []
        """

        return 2.0, 1.0, 0.5, 1/3

    def coeficiente_u(self) -> float:
        """
        Coeficiente u para el cálculo de la capacidad resistente del área transversal neta.

        :return: u; []
        """

        rango_validez = RangoValidez(self.d_0)
        e_2: float = rango_validez.rango_validez_e_2()
        p_2: float = rango_validez.rango_validez_p_2()
        u_1: float = 2 * e_2
        u_2: float = p_2
        u: float = min(u_1, u_2)

        return u

    def capacidad_resistente_area_transversal_neta_F_nRd(self) -> tuple:
        """
        Capacidad resistente F.nRd del área transversal neta.

        F.n,Rd = (1 + 3 r (d.0 / u - 0,3)) A.net f.u / γ.M2

        F.n,Rd ≤ A.net f.u / γ.M2

        Nota: Se considera r = 1, 1/2, 1/3

        :return: F_nRd; [N]
        """

        r: tuple[float, float, float, float] = self.relacion_tornillos_seccion_neta_entre_tornillos_totales()
        u: float = self.coeficiente_u()
        A_net: float = self.area_transversal_neta()
        F_nRd_1: tuple = tuple((1 + 3 * ri * (self.d_0 / u - 0.3)) * A_net * self.f_u / self.g_M2 for ri in r)
        F_nRd_2: float = A_net * self.f_u / self.g_M2
        F_nRd: tuple = tuple(min(F_nRd_1i, F_nRd_2) for F_nRd_1i in F_nRd_1)

        return F_nRd

    def limite_elastico_tornillo_f_yb(self) -> int:
        """
        Límite elástico del tornillo.

        :return f_yb; [N/mm²]
        """

        n1: int = int(self.grado.split('.', 1)[0])
        n2: int = int(self.grado.split('.', 1)[2])
        f_yb: int = n1 * n2 * 10

        return f_yb

    def resistencia_ultima_traccion_tornillo_f_ub(self) -> int:
        """
        Resistencia última a tracción del tornillo.

        :return: f_ub; [N/mm²]
        """

        n1: int = int(self.grado.split('.', 1)[0])
        f_ub: int = n1 * 100

        return f_ub

    def resistencia_cortante_F_vRd(self) -> float:
        """
        Resistencia de cálculo para elementos de unión sujetos a cortante.

        F.v,Rd = 0,6 f.ub A.s / γ.M2 para grados 4.6, 5.6, 8.8

        F.v,Rd = 0,5 f.ub A.s / γ.M2 para grados 4.8, 5.8, 6.8, 10.9

        :return: F_vRd [N]
        """

        f_ub: int = self.resistencia_ultima_traccion_tornillo_f_ub()
        if self.grado in ('4.6', '5.6', '8.8'):
            F_vRd: float = 0.6 * f_ub * self.A_s / self.g_M2
        elif self.grado in ('4.8', '5.8', '6.8', '10.9'):
            F_vRd: float = 0.5 * f_ub * self.A_s / self.g_M2
        else:
            print('Algo no cuadra.')

        return F_vRd

    # Tornillos a tracción

    def resistencia_traccion_F_tRd(self) -> float:
        """
        Resistencia a tracción para elementos de unión.

        :return: F_tRd; [N]
        """

        f_ub: int = self.resistencia_ultima_traccion_tornillo_f_ub()
        F_tRd: float = 0.9 * f_ub * self.A_s / self.g_M2

        return F_tRd


class RangoValidez:
    def __init__(self, d_0: float) -> None:
        """
        EN 1993-1-3:2006

        EUROCÓDIGO 3: PROYECTO DE ESTRUCTURAS DE ACERO

        PARTE 1-3: REGLAS GENERALES - REGLAS SUPLEMENTARIAS PARA CHAPAS Y ELEMENTOS PLEGADOS EN FRÍO

        TABLA 8.4: RESISTENCIAS DE DISEÑO DE TORNILLOS

        Rango de validez

        :param d_0: [mm] Diámetro del taladro del tornillo.
         """

        self.d_0 = d_0

    def rango_validez_e_1(self) -> float:
        """
        Rango de validez de la distancia del centro del taladro al extremo adyacente, medido en la dirección de
        transmisión de la carga.

        e.1 ≥ 1,0 d.0

        Válido para:

        - Métrica ≥ M6
        - Grados 4.6 a 10.9
        - 0,75 mm ≤ t < 3 mm
        - f.u ≤ 550 N/mm²

        :return e_1_min: [mm] Distancia e.1 mínima.
        """

        e_1_min: float = self.d_0

        return e_1_min

    def rango_validez_e_2(self) -> float:
        """
        Rango de validez de la distancia del centro del taladro al extremo adyacente, medido en ángulo recto respecto a
        la dirección de la transferencia de la carga.

        e.2 ≥ 1,5 d.0

        Válido para:

        - Métrica ≥ M6
        - Grados 4.6 a 10.9
        - 0,75 mm ≤ t < 3 mm
        - f.u ≤ 550 N/mm²

        :return e_2_min: [mm] Distancia e.2 mínima.
        """

        e_2_min: float = 1.5 * self.d_0

        return e_2_min

    def rango_validez_p_1(self) -> float:
        """
        Rango de validez del espacio entre centros en una fila en la dirección de la transferencia de la carga.

        p.1 ≥ 3 d.0

        Válido para:

        - Métrica ≥ M6
        - Grados 4.6 a 10.9
        - 0,75 mm ≤ t < 3 mm
        - f.u ≤ 550 N/mm²

        :return p_1_min: [mm] Espacio p.1 mínimo.
        """

        p_1_min: float = 3 * self.d_0

        return p_1_min

    def rango_validez_p_2(self) -> float:
        """
        Rango de validez del espacio medido perpendicularmente a la dirección de la transferencia de la carga entre
        líneas adyacentes.

        p.2 ≥ 3 d.0

        Válido para:

        - Métrica ≥ M6
        - Grados 4.6 a 10.9
        - 0,75 mm ≤ t < 3 mm
        - f.u ≤ 550 N/mm²

        :return p_2_min: [mm] Espacio p.2 mínimo.
        """

        p_2_min: float = 3 * self.d_0

        return p_2_min


if __name__ == '__main__':
    import random
    from prettytable import PrettyTable
    from src.modelos.dimensiones import Dimensiones
    from src.ISO_DIN_13_rosca_metrica.iso_din_13 import DatosISODIN13

    tabla = PrettyTable()
    tabla.field_names = (
        'Métrica', 'd', 'A.s', 'grado', 'd.0', 't', 'f.u', 'g.M2', 'e.1', 'e.2', 'p.1', 'p.2', 'F.b,Rd', 'F.n,Rd',
        'F.vRd'
    )

    datos = DatosISODIN13()
    metricas = datos.metricas()
    norma_metrica = 'ISO DIN 13'
    tipo_aguero = 'Agujeros redondos normales'
    t = 2
    f_u = 450
    g_M2 = 1.25

    random.seed(42)
    for _ in range(10):
        metrica = random.choice(metricas)
        dimensiones = Dimensiones(metrica, norma_metrica, tipo_aguero)
        d = dimensiones.diametro_nominal()
        d_0 = dimensiones.diametro_agujero()
        A_s = round(dimensiones.area_resistente_traccion())
        grado = random.choice(('4.6', '5.6', '8.8', '4.8', '5.8', '6.8', '10.9'))
        resistencias = ResistenciasDisenoTornillos(d, A_s, grado, d_0, t, f_u, g_M2)
        rango_validez = RangoValidez(d_0)
        e_1 = round(rango_validez.rango_validez_e_1(), 2)
        e_2 = round(rango_validez.rango_validez_e_2(), 2)
        p_1 = round(rango_validez.rango_validez_p_1(), 2)
        p_2 = round(rango_validez.rango_validez_p_2(), 2)
        F_bRd = round(resistencias.capacidad_resitente_F_bRd())
        F_nRd = tuple(round(F) for F in resistencias.capacidad_resistente_area_transversal_neta_F_nRd())
        F_vRd = round(resistencias.resistencia_cortante_F_vRd())
        tabla.add_row([metrica, d, A_s, grado, d_0, t, f_u, g_M2, e_1, e_2, p_1, p_2, F_bRd, F_nRd, F_vRd])
    print(tabla)
