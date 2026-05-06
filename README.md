# Differential Equations Numerical Methods Visualizer

A Python application that demonstrates numerical methods for solving differential equations, featuring Euler's method and the Runge-Kutta 4th order method (RK4). The application provides an interactive GUI to visualize solutions and compare numerical approximations with analytical solutions.

## Features

- **Numerical Methods Implementation**:
  - Euler's Method
  - Runge-Kutta 4th Order (RK4) Method

- **Differential Equation Models**:
  - Simple ODE: dy/dx = (2xy)/(1+x²)
  - Heart Rate Recovery Model
  - Heat Dissipation Model
  - Population Growth/Decay Model

- **Visualization**:
  - Interactive plots comparing numerical solutions with analytical solutions
  - Error analysis between methods
  - Results tables with step-by-step calculations

- **GUI Interface**:
  - Tkinter-based user interface
  - Easy navigation between different models
  - Parameter configuration options

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/Diff_Eq_Numerical_Methods.git
cd Diff_Eq_Numerical_Methods
```

2. Create a virtual environment:

```bash
python -m venv .venv
```

3. Activate the virtual environment:

- Windows:

```bash
.venv\Scripts\activate
```

- Linux/Mac:

```bash
source .venv/bin/activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

## Dependencies

- numpy==2.4.4
- matplotlib==3.10.9
- pandas (for data handling)
- tkinter (built-in with Python)

## Usage

Run the application:

```bash
python app.py
```

The GUI will open with a main menu. Select a differential equation model to solve and visualize.

## Project Structure

```
├── app.py                 # Main application entry point
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── logic/                # Core logic and calculations
│   ├── __init__.py
│   ├── config.py         # Configuration parameters
│   ├── models.py         # Differential equation definitions
│   ├── numerical_methods.py  # Euler and RK4 implementations
│   └── solver.py         # Solution orchestration
└── ui/                   # User interface components
    ├── __init__.py
    ├── input_pages.py    # Input configuration pages
    └── main_menu.py      # Main navigation menu
```

## Mathematical Background

### Euler's Method

A first-order numerical procedure for solving ordinary differential equations with a given initial value. It is the most basic explicit method for numerical integration of ordinary differential equations.

### Runge-Kutta 4th Order Method

A widely used method for solving differential equations numerically. It provides better accuracy than Euler's method by evaluating the derivative at multiple points within each time step.
