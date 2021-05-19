import numpy as np
from hepdata_lib import Submission, Table, Variable

def pairLQ(submission):
    #Prepare
    table = Table("pair LQ")
    table.location = ""
    table.description = "Pair leptoquark (LQ) total selection efficiency, accounting for both the decay branching fraction and the event selection, for events that pass the signal region requirements and any of the top quark or b jet categories defined in the search."
    data = np.loadtxt("input/pairLQ.txt", skiprows=2)

    #Indepedent variable (x axis)
    resonance_mass = Variable("LQ mass", is_independent=True, is_binned=False, units="GeV")
    resonance_mass.values = data[:,0]
    table.add_variable(resonance_mass)

    #First var
    eff_bulkg = Variable("Branching fraction x Acceptance", is_independent=False, is_binned=False)
    eff_bulkg.values = data[:,1]/100
    table.add_variable(eff_bulkg)

    #Submission
    submission.add_table(table)


