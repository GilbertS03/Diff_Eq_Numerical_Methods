import numpy as np
from . import config

def ode_function(x, y):
    return (2 * x * y) / (1 + x**2)

def true_ode_function(x):
    return 3 * (x**2 + 1)

def heart_rate_function(t, h):
    return -config.HEART_RATE_RECOVERY * (h - config.HEART_RATE_REST)

def heart_rate_true_function(t):
    return config.HEART_RATE_REST + (
        config.HEART_RATE_TIME_ZERO - config.HEART_RATE_REST
    ) * np.exp(-config.HEART_RATE_RECOVERY * t)

def heat_dissipation_function(t, temp):
    return -config.HEAT_DISSIPATION_RATE * (temp - config.HEAT_DISSIPATION_AMBIENT)

def heat_dissipation_true_function(t):
    return config.HEAT_DISSIPATION_AMBIENT + (
        config.HEAT_DISSIPATION_TIME_ZERO - config.HEAT_DISSIPATION_AMBIENT
    ) * np.exp(-config.HEAT_DISSIPATION_RATE * t)

def growth_and_decay_function(t, pop):
    return config.GROWTH_AND_DECAY_RATE * pop

def growth_and_decay_true_function(t):
    return config.GROWTH_AND_DECAY_INIT_POP * np.exp(config.GROWTH_AND_DECAY_RATE * t)
