import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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

    euler_error = [abs(true_vals[i] - euler_vals[i]) for i in range(len(true_vals))]

    rk4_error = [abs(true_vals[i] - rk4_vals[i]) for i in range(len(true_vals))]

    return x_vals, euler_vals, rk4_vals, true_vals, euler_error, rk4_error, "Simple ODE"


def solve_heart_rate():
    x_vals = generate_x_values()

    euler_vals = euler(heart_rate_function, config.STEP_SIZE, 0,
                       config.HEART_RATE_TIME_ZERO, config.NUM_STEPS)

    rk4_vals = rk4(heart_rate_function, config.STEP_SIZE, 0,
                   config.HEART_RATE_TIME_ZERO, config.NUM_STEPS)

    true_vals = [heart_rate_true_function(x) for x in x_vals]

    euler_error = [abs(true_vals[i] - euler_vals[i]) for i in range(len(true_vals))]

    rk4_error = [abs(true_vals[i] - rk4_vals[i]) for i in range(len(true_vals))]

    return x_vals, euler_vals, rk4_vals, true_vals, euler_error, rk4_error, "Heart Rate"

def solve_heat_dissipation():
    x_vals = generate_x_values()

    euler_vals = euler(heat_dissipation_function, config.STEP_SIZE, 0,
                       config.HEAT_DISSIPATION_TIME_ZERO, config.NUM_STEPS)

    rk4_vals = rk4(heat_dissipation_function, config.STEP_SIZE, 0,
                    config.HEAT_DISSIPATION_TIME_ZERO, config.NUM_STEPS)

    true_vals = [heat_dissipation_true_function(x) for x in x_vals]

    euler_error = [abs(true_vals[i] - euler_vals[i]) for i in range(len(true_vals))]

    rk4_error = [abs(true_vals[i] - rk4_vals[i]) for i in range(len(true_vals))]

    return  x_vals, euler_vals, rk4_vals, true_vals, euler_error, rk4_error, "Heat Dissipation"

def solve_growth_decay():
    x_vals = generate_x_values()

    euler_vals = euler(growth_and_decay_function, config.STEP_SIZE, 0,
                       config.GROWTH_AND_DECAY_INIT_POP, config.NUM_STEPS)

    rk4_vals = rk4(growth_and_decay_function, config.STEP_SIZE, 0,
                    config.GROWTH_AND_DECAY_INIT_POP, config.NUM_STEPS)

    true_vals = [growth_and_decay_true_function(x) for x in x_vals]

    euler_error = [abs(true_vals[i] - euler_vals[i]) for i in range(len(true_vals))]

    rk4_error = [abs(true_vals[i] - rk4_vals[i]) for i in range(len(true_vals))]

    return  x_vals, euler_vals, rk4_vals, true_vals, euler_error, rk4_error, "Growth/Decay Model"

def plot_solution(x, euler_y, rk4_y, true_y, euler_error, rk4_error, title):
    plt.figure(figsize=(8, 10))

    plt.subplot(2, 1, 1)

    plt.plot(x, euler_y, label="Euler")
    plt.plot(x, rk4_y, label="RK4")
    plt.plot(x, true_y, label="True")
    plt.legend()
    plt.title(title + "(Solution)")
    plt.grid()

    plt.subplot(2, 1, 2)
    plt.plot(x, euler_error, label="Euler Error")
    plt.plot(x, rk4_error, label="RK4 Error")

    plt.title("Error Comparison")
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.show()

def print_results_table(x, euler, rk4, true, euler_err, rk4_err):
    data = {
        "x": x,
        "Euler": euler,
        "RK4": rk4,
        "True": true,
        "Euler Error": euler_err,
        "RK4 Error": rk4_err
    }

    df = pd.DataFrame(data)
    print(df.head(10))
    