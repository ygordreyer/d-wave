import dwavebinarycsp
import dwavebinarycsp.factories.constraint.gates as gates
import operator
import dimod
import matplotlib.pyplot as plt
from dwave.system import DWaveSampler, EmbeddingComposite, LeapHybridSampler



csp = dwavebinarycsp.ConstraintSatisfactionProblem(dwavebinarycsp.BINARY)


csp.add_constraint(operator.ne, ['A', 'Anot'])
csp.add_constraint(operator.ne, ['B', 'Bnot'])
csp.add_constraint(operator.ne, ['C', 'Cnot'])
csp.add_constraint(operator.ne, ['D', 'Dnot'])
csp.add_constraint(operator.ne, ['E', 'Enot'])

#5INPUT AND 1
csp.add_constraint(gates.and_gate(['A', 'Bnot', 'AND_1_1']))
csp.add_constraint(gates.and_gate(['Cnot', 'Dnot', 'AND_1_2']))
csp.add_constraint(operator.ne, ['NOT_1_1', 'AND_1_1'])
csp.add_constraint(operator.ne, ['NOT_1_2', 'AND_1_2'])
csp.add_constraint(gates.or_gate(['NOT_1_1', 'NOT_1_2', 'OR_1']))
csp.add_constraint(operator.ne, ['OR_1', 'NOT_OR_1'])
csp.add_constraint(gates.and_gate(['E', 'NOT_OR_1', 'AND_1']))

#5INPUT AND 2
csp.add_constraint(gates.and_gate(['A', 'Bnot', 'AND_2_1']))
csp.add_constraint(gates.and_gate(['Cnot', 'D', 'AND_2_2']))
csp.add_constraint(operator.ne, ['NOT_2_1', 'AND_2_1'])
csp.add_constraint(operator.ne, ['NOT_2_2', 'AND_2_2'])
csp.add_constraint(gates.or_gate(['NOT_2_1', 'NOT_1_2', 'OR_2']))
csp.add_constraint(operator.ne, ['OR_2', 'NOT_OR_2'])
csp.add_constraint(gates.and_gate(['Enot', 'NOT_OR_2', 'AND_2']))

#5INPUT AND 3
csp.add_constraint(gates.and_gate(['A', 'Bnot', 'AND_3_1']))
csp.add_constraint(gates.and_gate(['C', 'Dnot', 'AND_3_2']))
csp.add_constraint(operator.ne, ['NOT_3_1', 'AND_3_1'])
csp.add_constraint(operator.ne, ['NOT_3_2', 'AND_3_2'])
csp.add_constraint(gates.or_gate(['NOT_3_1', 'NOT_3_2', 'OR_3']))
csp.add_constraint(operator.ne, ['OR_3', 'NOT_OR_3'])
csp.add_constraint(gates.and_gate(['E', 'NOT_OR_3', 'AND_3']))

#5INPUT AND 4
csp.add_constraint(gates.and_gate(['A', 'B', 'AND_4_1']))
csp.add_constraint(gates.and_gate(['Cnot', 'Dnot', 'AND_4_2']))
csp.add_constraint(operator.ne, ['NOT_4_1', 'AND_4_1'])
csp.add_constraint(operator.ne, ['NOT_4_2', 'AND_4_2'])
csp.add_constraint(gates.or_gate(['NOT_4_1', 'NOT_4_2', 'OR_4']))
csp.add_constraint(operator.ne, ['OR_4', 'NOT_OR_4'])
csp.add_constraint(gates.and_gate(['Enot', 'NOT_OR_4', 'AND_4']))

#4input OR
csp.add_constraint(gates.or_gate(['AND_1', 'AND_2', 'OR_5_1']))
csp.add_constraint(gates.or_gate(['AND_3', 'AND_4', 'OR_5_2']))
csp.add_constraint(gates.or_gate(['OR_5_1', 'OR_5_2', 'OUT']))


bqm = dwavebinarycsp.stitch(csp)


# ---------- For Quantum Tests ----------
# Set up a D-Wave system as the sampler
# sampler = EmbeddingComposite(DWaveSampler())
# response = sampler.sample(bqm, num_reads=1000)


# ---------- For Hybrid Tests ----------
# sampler = LeapHybridSampler()
# response = sampler.sample(bqm)

# ---------- For Classical Tests ----------
response = dimod.ExactSolver().sample(bqm)
print(response)
