import numpy as np

from config import *
from util import *


def vraag1():
    return P_env + kpa_to_bar((m_piston * g) / A)  # bar


def vraag2():
    p = bar_to_kpa(vraag1())  # kPa
    V = (np.pi * (D_piston / 2) ** 2) * h0  # m^3
    return (p * V) / (R * T_env) * 1000  # gram


def vraag3():
    m = vraag2() / 1000  # kg
    return (T_env - celcius_to_K) + Q_ex / (m * c)  # deg C


def vraag4():
    V = (np.pi * (D_piston / 2) ** 2) * h0  # m^3
    T = vraag3() + celcius_to_K
    m = vraag2() / 1000  # kg
    return kpa_to_bar((R * T * m) / V)  # bar


def vraag5():
    m = vraag2() / 1000  # kg
    p1 = bar_to_kpa(vraag4())  # kPa
    p2 = bar_to_kpa(vraag1())  # kPa
    kappa = 1.4
    return (m / A) * ((p1 / p2) * ((A * h0) / m) ** kappa) ** (1 / kappa)  # m


def vraag6():
    p = bar_to_kpa(vraag1())  # kPa
    V = vraag5() * A  # m^3
    m = vraag2() / 1000  # kg
    return (p * V) / (R * m) - celcius_to_K  # C
