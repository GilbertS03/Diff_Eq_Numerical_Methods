from . import config

def euler(function, step_size, starting_x, starting_y, num_steps):
    x = starting_x
    y = starting_y
    y_values = [y]

    for _ in range(num_steps):
        slope = function(x, y)
        x += step_size
        y = round(y + step_size * slope, config.NUM_DECIMALS)
        y_values.append(y)

    return y_values


def rk4(function, step_size, starting_x, starting_y, num_steps):
    x = starting_x
    y = starting_y
    y_values = [y]

    for _ in range(num_steps):
        k1 = function(x, y)
        k2 = function(x + step_size/2, y + step_size*k1/2)
        k3 = function(x + step_size/2, y + step_size*k2/2)
        k4 = function(x + step_size, y + step_size*k3)

        x += step_size
        y = round(y + (step_size/6)*(k1 + 2*k2 + 2*k3 + k4),
                  config.NUM_DECIMALS)

        y_values.append(y)

    return y_values
