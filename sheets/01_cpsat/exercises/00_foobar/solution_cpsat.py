from data_schema import Instance, Solution
from ortools.sat.python import cp_model


def solve(instance: Instance) -> Solution:
    """
    Implement your solver for the problem here!
    """
    numbers = instance.numbers
    min_num = min(numbers)
    max_num = max(numbers)

    model = cp_model.CpModel()

    x = model.NewIntVar(min_num, max_num, "x")
    y = model.NewIntVar(min_num, max_num, "y")

    model.Maximize(x-y)

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    assert (status == cp_model.OPTIMAL)
    print(f"x={solver.Value(x)},  y={solver.Value(y)}")

    return Solution(
        number_a=solver.Value(y),
        number_b=solver.Value(x),
        distance=abs(solver.Value(y) - solver.Value(x)),
    )
