import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint, trapz

from config import *
from util import *

t = np.linspace(0, 0.5, 20_000)


def F_tot(p, v):
    F_g = m_piston * g  # N
    F_f = c_w * v  # N
    F_pressure_out = bar_to_kpa(P_env) * A  # N
    F_pressure_in = p * A  # N

    return -F_g - F_f - F_pressure_out + F_pressure_in  # N


def calc_p(h, T):
    V = A * h  # m^3

    return (R * T) / V  # kPa


def calc_dT(Q):
    return (c * m_piston) / Q  # delta K


def functieVoorDeZuiger(state):
    T, Q, v, h = state

    a = F_tot(calc_p(h, T), v)
    dT = calc_dT(Q)

    dQ = 0
    return dT, dQ, a, v


resultaat = odeint(functieVoorDeZuiger, (), t)
