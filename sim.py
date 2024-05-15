import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint, trapz

from config import *
from util import *


def calc_polytrop_const(p, V):
    return p * (V / m_piston) ** n


p0 = vraag4_resultaat = bar_to_kpa(11.208200882187015)  # kPa
V0 = h0 * A
polytrop_c = calc_polytrop_const(p0, V0)
state0 = (0, h0)


def F_tot_no_resist(p, v):
    F_g = m_piston * g  # N
    # F_f = c_w * v  # N
    F_pressure_out = bar_to_kpa(P_env) * A  # N
    F_pressure_in = p * A  # N

    return -F_g - F_pressure_out + F_pressure_in  # N


def F_tot(p, v):
    F_g = m_piston * g  # N
    F_f = c_w * v  # N
    F_pressure_out = bar_to_kpa(P_env) * A  # N
    F_pressure_in = p * A  # N

    return -F_g - F_f - F_pressure_out + F_pressure_in  # N


def calc_p(V):
    return polytrop_c / (V / m_piston) ** n  # kPa


@np.vectorize
def calc_dT(t):
    if t == 0:
        return (c * m_piston) / Q_ex  # delta K
    return 0


def pistonNoResist(state, t):
    v, h = state
    V = A * h  # m^3
    p = calc_p(V)
    a = F_tot_no_resist(p, v)
    return a, v


def piston(state, t):
    v, h = state
    V = A * h  # m^3
    p = calc_p(V)
    a = F_tot(p, v)
    return a, v


t = np.linspace(0, 0.5, 20_000)
res_no_resist = odeint(pistonNoResist, state0, t)
res_no_resist_v, res_no_resist_h = res_no_resist.T
res_no_resist_p = calc_p(res_no_resist_h * A)

print("max h - no resist: ", np.max(res_no_resist_h))
print("min p - no resist (bar): ", kpa_to_bar(np.min(res_no_resist_p)))

res = odeint(piston, state0, t)
res_v, res_h = res.T
res_p = calc_p(res_h * A)

print("where t = 0.5, h - resist: ", res_h[-1])
print("max v - resist (WRONG?): ", np.max(res_v))
fig, ax = plt.subplots(2, 2)

ax[0][0].plot(t, res_no_resist_h)
ax[0][1].plot(t, res_no_resist_p)
ax[1][0].plot(t, res_h)

plt.show()
