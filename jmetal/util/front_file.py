from jmetal.core.solution import FloatSolution

"""
.. module:: Front file
   :platform: Unix, Windows
   :synopsis: Utils to read reference frontiers from files.

.. moduleauthor:: Antonio J. Nebro <ajnebro@uma.es>
"""


def read_front_from_file(file_name: str):
    """ Reads a front from a file and returns a list.
    """
    front = []
    with open(file_name) as file:
        for line in file:
            vector = [float(x) for x in line.split()]
            front.append(vector)
    return front


def read_front_from_file_as_solutions(file_path: str):
    """ Reads a front from a file and returns a list of solution objects.

    :return: List of solution objects.
    """
    front = []
    with open(file_path) as file:
        for line in file:
            vector = [float(x) for x in line.split()]
            solution = FloatSolution(2, 2, 0, [], [])
            solution.objectives = vector

            front.append(solution)

    return front
