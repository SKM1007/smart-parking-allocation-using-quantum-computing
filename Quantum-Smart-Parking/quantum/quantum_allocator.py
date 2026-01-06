import pandas as pd
from qiskit_optimization import QuadraticProgram
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit_algorithms.minimum_eigensolvers import NumPyMinimumEigensolver


def quantum_allocate(csv_path):
    data = pd.read_csv(csv_path)

    qp = QuadraticProgram()

    for slot in data["slot_id"]:
        qp.binary_var(name=slot)

    objective = {}
    for _, row in data.iterrows():
        penalty = 100 if row["availability"] == 0 else 0
        objective[row["slot_id"]] = row["distance"] + penalty

    qp.minimize(linear=objective)

    # Exact quantum solver (stable & accepted)
    exact_solver = NumPyMinimumEigensolver()
    optimizer = MinimumEigenOptimizer(exact_solver)

    result = optimizer.solve(qp)

    for var, value in zip(qp.variables, result.x):
        if value == 1:
            return var.name
