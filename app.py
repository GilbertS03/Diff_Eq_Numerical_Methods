from tkinter import *
from ui.main_menu import MainMenu
from ui.input_pages import ChangeValuesPage

from logic.solver import (
    solve_ode,
    solve_heart_rate,
    solve_heat_dissipation,
    solve_growth_decay,
    plot_solution
)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Differential Equations Visualizer")
        self.root.geometry("500x500")

        # Container for frames
        container = Frame(root)
        container.pack(fill="both", expand=True)

        self.frames = {}

        # Register all pages here
        for F in (MainMenu, ChangeValuesPage):
            name = F.__name__
            frame = F(container, self)
            self.frames[name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def run_ode(self):
        print("Running ODE...")
        x, e, r, t, title = solve_ode()
        plot_solution(x, e, r, t, title)

    def run_heart_rate(self):
        print("Running Heart Rate...")
        x, e, r, t, title = solve_heart_rate()
        plot_solution(x, e, r, t, title)

    def run_heat(self):
        print("Running Heat Dissipation...")
        x, e, r, t, title = solve_heat_dissipation()
        plot_solution(x, e, r, t, title)

    def run_growth(self):
        print("Running Growth/Decay...")
        x, e, r, t, title = solve_growth_decay()
        plot_solution(x, e, r, t, title)


if __name__ == "__main__":
    root = Tk()
    app = App(root)
    app.show_frame("MainMenu")
    root.mainloop()