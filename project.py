import numpy as np
import matplotlib.pyplot as plt

# GLOBAL CONSTANTS
# Menu Choices
ODE = 1
HR_ODE = 2
HD_ODE = 3
OS_ODE = 4
CHANGE_VALUES = 5
QUIT = -1
# Calculation Constants
STEP_SIZE = 0.5
NUM_STEPS = 5
NUM_DECIMALS = 5
MIN_NUM_STEPS = 3
MAX_STEP_SIZE = 1
MIN_NUM_DECIMALS = 3
# Initial Values for ODE's
ODE_X_0 = 0
ODE_Y_0 = 3
# Average heart rate recovery
HEART_RATE_RECOVERY = .12
HEART_RATE_REST = 60
HEART_RATE_X_ZERO = 0
HEART_RATE_TIME_ZERO = 170
# PLOT VARIABLES
ODE_TITLE = 'ODE_Plot.png'
HEART_RATE_TITLE = 'Heart_Rate_Plot.png'
HEAT_DISSAPTION_TITLE = 'Heat_Dissapation_Plot.png'
OSCILLATION_TITLE = 'Oscillation_Plot.png'

# ODE FUNCTIONS
def ode_function(x, y):
    # Initial value: y(0) = 3
    # (2*x*y)/(1+x^2)
    num = 2*x*y
    denom = 1 + x**2
    return num/denom

def true_ode_function(x):
    return 3 * (x**2 + 1)

def heart_rate_function(time, heart_rate):
    # dH/dt = -k(H-H_rest)
    # H(0) = 170 (HEAVY ACTIVITY)
    # H_REST = 60
    return -HEART_RATE_RECOVERY*(heart_rate - HEART_RATE_REST)

def heart_rate_true_function(t):
    # H(t) = H_rest + (H_0-H_rest)*e^(-kt)
    return HEART_RATE_REST + (HEART_RATE_TIME_ZERO - HEART_RATE_REST)*np.exp(-HEART_RATE_RECOVERY * t)

# METHODS
def euler(function, step_size, starting_x, starting_y, num_steps):
    x = starting_x
    y = starting_y
    x_values = [x]
    y_values = [y]
    for _ in range(num_steps):
        slope = function(x, y)
        # Move x forward in step size
        x = x + step_size

        # Update y using the Euler step
        y = round(y + (step_size*slope), NUM_DECIMALS)

        x_values.append(x)
        y_values.append(y)
    return y_values

def rk4(function, step_size, starting_x, starting_y, num_steps):
    x = starting_x
    y = starting_y
    x_values = [x]
    y_values = [y]
    for _ in range(num_steps):
        k_1 = function(x, y)
        k_2 = function(x + (step_size/2), y + (step_size*k_1/2))
        k_3 = function(x + (step_size/2), y + (step_size*k_2/2))
        k_4 = function(x + step_size, y + (step_size*k_3))

        # x_n+1
        x = x + step_size

        h = step_size/6

        # y_n+1
        y = round(y + h*(k_1 + 2*k_2 + 2*k_3 + k_4), NUM_DECIMALS)

        x_values.append(x)
        y_values.append(y)
    return y_values

def get_real_values(function, step_size, starting_x, num_steps):
    x = starting_x
    x_values = [x]
    y = function(x)
    y_values = [y]
    for _ in range(num_steps):
        x = x + step_size
        y = function(x)
        x_values.append(x)
        y_values.append(y)
    return y_values

# USER STEPS, SIZE, AND DECIMAL PLACES
def get_step_size_and_num_steps():
    try:
        global STEP_SIZE, NUM_STEPS, NUM_DECIMALS

        STEP_SIZE = float(input(f"How small do you want the steps to be? (Smaller numbers mean more accurate results and must be less than {MAX_STEP_SIZE}): "))
        while STEP_SIZE > MAX_STEP_SIZE:
            print(f"Step size cannot be greater than {MAX_STEP_SIZE}, please try again")
            STEP_SIZE = float(input(f"How small do you want the steps to be? (Smaller numbers mean more accurate results and must be less than {MAX_STEP_SIZE}): "))

        NUM_STEPS = int(input(f"How many steps would you like to take: (Must be greater than {MIN_NUM_STEPS}) "))
        while NUM_STEPS < MIN_NUM_STEPS:
            print(f"Number of steps cannot be less than {MIN_NUM_STEPS}, please try again")
            NUM_STEPS = int(input(f"How many steps would you like to take: (Must be greater than {MIN_NUM_STEPS}) "))

        NUM_DECIMALS = int(input(f"How many decimals out would you like to go: (Must be greater than {MIN_NUM_DECIMALS}) "))
        while NUM_DECIMALS < MIN_NUM_DECIMALS:
            print(f"Number of decimal places cannot be less than {MIN_NUM_DECIMALS}. Please try again.")
            NUM_DECIMALS = int(input(f"How many decimals out would you like to go: (Must be greater than {MIN_NUM_DECIMALS}) "))

        print(f"Now using Step Size: {STEP_SIZE}, Number of Steps: {NUM_STEPS}, and decimal points out: {NUM_DECIMALS} ")
    except ValueError:
        print("Incorrect data type. Defaulting to step size = 0.5, number steps = 5")
        STEP_SIZE = 0.5 
        NUM_STEPS = 5
        NUM_DECIMALS = 5
        print(f"Now using Step Size: {STEP_SIZE}, Number of Steps: {NUM_STEPS}, and decimal points out: {NUM_DECIMALS} ")

def ode():
    # Initial values: f(0) = 3
    x_values = []
    x = 0
    x_values.append(x)

    for _ in range(0, NUM_STEPS):
        x += STEP_SIZE
        x_values.append(x)
    
    euler_y_values = euler(ode_function, STEP_SIZE, ODE_X_0, ODE_Y_0, NUM_STEPS)
    rk4_y_values = rk4(ode_function, STEP_SIZE, ODE_X_0, ODE_Y_0, NUM_STEPS)
    real_y_values = get_real_values(true_ode_function, STEP_SIZE, ODE_X_0, NUM_STEPS)

    chart_creator(x_values, euler_y_values, rk4_y_values, real_y_values, ODE_TITLE)

def heart_rate_ode():
    x_values = []
    x = 0
    x_values.append(x)

    for _ in range(0, NUM_STEPS):
        x += STEP_SIZE
        x_values.append(x)
    
    euler_y_values = euler(heart_rate_function, STEP_SIZE, HEART_RATE_X_ZERO, HEART_RATE_TIME_ZERO, NUM_STEPS)
    rk4_y_values = rk4(heart_rate_function, STEP_SIZE, HEART_RATE_X_ZERO, HEART_RATE_TIME_ZERO, NUM_STEPS)
    real_y_values = get_real_values(heart_rate_true_function, STEP_SIZE, HEART_RATE_X_ZERO, NUM_STEPS)

    chart_creator(x_values, euler_y_values, rk4_y_values, real_y_values, HEART_RATE_TITLE)

def heat_dissapation_ode():
    pass

def oscillation_ode():
    pass

def chart_creator(x_values, euler_y_values, rk4_y_values, true_y_values, title):
    x_points = np.array(x_values)
    euler_y_points = np.array(euler_y_values)
    rk4_y_points = np.array(rk4_y_values)
    true_y_points = np.array(true_y_values)

    font1 = {'family':'serif','color':'blue','size':15}
    font2 = {'family':'serif','color':'darkred','size':15}
    plt.figure(figsize=(8, 8))
    plt.title("ODE: (2*x*y)/(1+x^2). TRUE vs EULER vs RK4", fontdict = font1)

    plt.plot(x_points, euler_y_points, color='green', label='Euler\' Line')
    plt.plot(x_points, rk4_y_points, color='red', label='RK4 Line')
    plt.plot(x_points, true_y_points, color='purple', label='True Line')
    plt.legend()
    plt.savefig(title)
    plt.show()
    
def menu():
    menu = f"{QUIT}. Quit\n{ODE}. View ODE: (dy/dx) = (2xy)/(1+x^2) with Answer: y = 3(x^2 + 1)\n" \
    f"{HR_ODE}. View Heart Rate ODE\n{HD_ODE}. View PC Heat dissapation ODE\n{OS_ODE}. View Oscillation ODE\n"\
    f"{CHANGE_VALUES}. Change values for Number of Steps and Step size\n"
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
            elif choice == CHANGE_VALUES:
                get_step_size_and_num_steps()
            else:
                print("Not a valid choice, please try again")
        except ValueError:
            print("Invalid data type, please try again")
    print("Goodbye!!!")
main()