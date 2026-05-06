from tkinter import *
from logic import config

class ChangeValuesPage(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        Label(self, text="Update Parameters",
              font=("Arial", 16)).pack(pady=20)

        Label(self, text="Step Size (h)").pack()
        self.step_entry = Entry(self)
        self.step_entry.insert(0, str(config.STEP_SIZE))
        self.step_entry.pack()

        Label(self, text="Number of Steps").pack()
        self.steps_entry = Entry(self)
        self.steps_entry.insert(0, str(config.NUM_STEPS))
        self.steps_entry.pack()

        Label(self, text="Decimal Precision").pack()
        self.decimals_entry = Entry(self)
        self.decimals_entry.insert(0, str(config.NUM_DECIMALS))
        self.decimals_entry.pack()

        Label(self, text="Growth/Decay Initial Population").pack()
        self.pop_entry = Entry(self)
        self.pop_entry.insert(0, str(config.GROWTH_AND_DECAY_INIT_POP))
        self.pop_entry.pack()

        Label(self, text="Growth/Decay Rate (k)").pack()
        self.rate_entry = Entry(self)
        self.rate_entry.insert(0, str(config.GROWTH_AND_DECAY_RATE))
        self.rate_entry.pack()

        Button(self, text="Save",
               command=self.save_values).pack(pady=10)

        Button(self, text="Back",
               command=lambda: controller.show_frame("MainMenu")).pack()

    def save_values(self):
        try:
            config.STEP_SIZE = float(self.step_entry.get())
            config.NUM_STEPS = int(self.steps_entry.get())
            config.NUM_DECIMALS = int(self.decimals_entry.get())

            config.GROWTH_AND_DECAY_INIT_POP = float(self.pop_entry.get())
            config.GROWTH_AND_DECAY_RATE = float(self.rate_entry.get())

            print("Updated config!")

        except ValueError:
            print("Invalid input")
