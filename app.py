from logic.solver import solve_ode, plot_solution

def run_ode(self):
    x, e, r, t, title = solve_ode()
    plot_solution(x, e, r, t, title)
