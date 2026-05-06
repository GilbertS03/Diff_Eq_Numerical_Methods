from tkinter import *
from .input_pages import ChangeValuesPage

class MainMenu(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        Label(self, text="Differential Equations Visualizer",
              font=("Arial", 16)).pack(pady=20)

        Button(self, text="Simple ODE",
               command=controller.run_ode).pack(pady=5)

        Button(self, text="Heart Rate Model",
               command=controller.run_heart_rate).pack(pady=5)

        Button(self, text="Heat Dissipation",
               command=controller.run_heat).pack(pady=5)

        Button(self, text="Growth / Decay",
               command=controller.run_growth).pack(pady=5)

        Button(self, text="Change Parameters",
               command=lambda: controller.show_frame("ChangeValuesPage")).pack(pady=15)

        Button(self, text="Quit",
               command=controller.root.destroy).pack(pady=10)
