import numpy as np
import matplotlib.pyplot as plt

from . import config
from .models import *
from .numerical_methods import *

def generate_x_values():
    x_vals = [0]
    x = 0
    for _ in range(config.NUM_STEPS):
        x += config.STEP_SIZE
        x_vals.append(x)
    return x_vals


def solve_ode():
    x_vals = generate_x_values()

    euler_vals = euler(ode_function, config.STEP_SIZE, 0,
                       config.ODE_Y_0, config.NUM_STEPS)

    rk4_vals = rk4(ode_function, config.STEP_SIZE, 0,
                   config.ODE_Y_0, config.NUM_STEPS)

    true_vals = [true_ode_function(x) for x in x_vals]

    return x_vals, euler_vals, rk4_vals, true_vals, "Simple ODE"


def solve_heart_rate():
    x_vals = generate_x_values()

    euler_vals = euler(heart_rate_function, config.STEP_SIZE, 0,
                       config.HEART_RATE_TIME_ZERO, config.NUM_STEPS)

    rk4_vals = rk4(heart_rate_function, config.STEP_SIZE, 0,
                   config.HEART_RATE_TIME_ZERO, config.NUM_STEPS)

    true_vals = [heart_rate_true_function(x) for x in x_vals]

    return x_vals, euler_vals, rk4_vals, true_vals, "Heart Rate"


def plot_solution(x, euler_y, rk4_y, true_y, title):
    plt.figure()
    plt.plot(x, euler_y, label="Euler")
    plt.plot(x, rk4_y, label="RK4")
    plt.plot(x, true_y, label="True")
    plt.legend()
    plt.title(title)
    plt.show()
