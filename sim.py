import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint, trapz

from config import *
from util import *

t = np.linspace(0, 0.5, 20_000)


def F_tot(pressure, v):
    F_g = m_piston * g  # N
    F_f = c_w * v  # N
    F_pressure_out = bar_to_kpa(P_env) * A  # N
    F_pressure_in = pressure * A  # N

    return -F_g - F_f - F_pressure_out + F_pressure_in  # N


def functieVoorDeZuiger():
    a = 0


resultaat = odeint(functieVoorDeZuiger, (), t)
