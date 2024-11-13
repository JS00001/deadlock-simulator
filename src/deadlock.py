from .simulations.simulation_3 import simulation_3
from .simulations.simulation_2 import simulation_2
from .simulations.simulation_1 import simulation_1

def simulate_deadlock():
    print("-----------------")
    print("Running Simulation #1 (Deadlock Detected & Resolved)")
    print("-----------------")
    simulation_1()

    print("-----------------")
    print("Running Simulation #2 (Deadlock Not Detected)")
    print("-----------------")
    simulation_2()

    print("-----------------")
    print("Running Simulation #3 (Deadlock Detected & Resolved)")
    print("-----------------")
    simulation_3()



