import numpy as np
from hepdata_lib import Submission, Table, Variable

def singleLQs(submission):
    #Prepare
    table = Table("Acceptance times efficiency for single leptoquarks")
    table.location = ""
    table.description = "Single scalar leptoquark (LQs) total selection efficiency, accounting for both the decay branching fraction and the event selection, for events that pass the signal region requirements and any of the top quark or b jet categories defined in the search."
    data = np.loadtxt("input/singleLQs.txt", skiprows=2)

    #Indepedent variable (x axis)
    resonance_mass = Variable("LQs mass", is_independent=True, is_binned=False, units="GeV")
    resonance_mass.values = data[:,0]
    table.add_variable(resonance_mass)

    #Variables
    eff_LQl0p5 = Variable("Branching fraction x Acceptance", is_independent=False, is_binned=False)
    eff_LQl0p5.values = data[:,1]/100
    eff_LQl0p5.add_qualifier("Process", "LQs $\lambda$ = 0.5")
    table.add_variable(eff_LQl0p5)

    eff_LQl1p0 = Variable("Branching fraction x Acceptance", is_independent=False, is_binned=False)
    eff_LQl1p0.values = data[:,2]/100
    eff_LQl1p0.add_qualifier("Process", "LQs $\lambda$ = 1.0")
    table.add_variable(eff_LQl1p0)

    eff_LQl1p5 = Variable("Branching fraction x Acceptance", is_independent=False, is_binned=False)
    eff_LQl1p5.values = data[:,3]/100
    eff_LQl1p5.add_qualifier("Process", "LQs $\lambda$ = 1.5")
    table.add_variable(eff_LQl1p5)

    eff_LQl2p0 = Variable("Branching fraction x Acceptance", is_independent=False, is_binned=False)
    eff_LQl2p0.values = data[:,4]/100
    eff_LQl2p0.add_qualifier("Process", "LQs $\lambda$ = 2.0")
    table.add_variable(eff_LQl2p0)

    eff_LQl2p5 = Variable("Branching fraction x Acceptance", is_independent=False, is_binned=False)
    eff_LQl2p5.values = data[:,5]/100
    eff_LQl2p5.add_qualifier("Process", "LQs $\lambda$ = 2.5")
    table.add_variable(eff_LQl2p5)

    #Submission
    submission.add_table(table)


