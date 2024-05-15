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


@np.vectorize
def calc_dT(t):
    if t == 0:
        return (c * m_piston) / Q_ex  # delta K
    return 0


def functieVoorDeZuiger(state, t):
    T, v, h = state

    a = F_tot(calc_p(h, T), v)
    dT = calc_dT(t)

    return dT, a, v


vraag_6_resultaat = 1329.6463680447187 + celcius_to_K  # K
state0 = (vraag_6_resultaat, 0, h0)
resultaat = odeint(functieVoorDeZuiger, state0, t)
res_T, res_v, res_h = resultaat.T

fig, ax = plt.subplots(1, 1)

ax.plot(t, res_h)

plt.show()
