import numpy as np
import matplotlib.pyplot as plot

ODE = 1
HR_ODE = 2
HD_ODE = 3
OS_ODE = 4
QUIT = -1

def ode_function(x, y):
    num = 2*x*y
    denom = 1 + x**2
    return num/denom

def true_ode_function(x):
    return 3 * (x**2 + 1)

def euler(function, step_size, starting_x, num_steps):
    y_values = []
    x_values = []
    slope = 0
    for step in range(0, num_steps):
        pass

def rk4():
    pass

def ode():
    pass

def heart_rate_ode():
    pass

def heat_dissapation_ode():
    pass

def oscillation_ode():
    pass

def menu():
    menu = f"{QUIT}. Quit\n{ODE}. View ODE: (dy/dx) = (2xy)/(1+x^2) with Answer: y = 3(x^2 + 1)\n" \
    f"{HR_ODE}. View Heart Rate ODE\n{HD_ODE}. View PC Heat dissapation ODE\n{OS_ODE}. View Oscillation ODE\n"
    return menu

def main():
    running = True
    while running:
        try:
            choice = int(input(menu()))
            if choice == QUIT:
                running = False
            elif choice == ODE:
                ode()
            elif choice == HR_ODE:
                heart_rate_ode()
            elif choice == HD_ODE:
                heat_dissapation_ode()
            elif choice == OS_ODE:
                oscillation_ode()
            else:
                print("Not a valid choice, please try again")
        except ValueError:
            print("Invalid data type, please try again")
    print("Goodbye!!!")
main()