from dwave.system import DWaveSampler, EmbeddingComposite, LeapHybridSampler



# ---------- For Quantum Tests ----------
# sampler_auto = EmbeddingComposite(DWaveSampler(solver={'qpu': True}))

# ---------- For Hybrid Tests ----------
sampler_auto = LeapHybridSampler()

# Set Q for the problem QUBO
linear = {('E', 'E'): 3}
# ( 8AB + 8AC + 8AD − 4AE + 8BC + 8BD − 4BE + 8CD − 4CE − 4DE + 3E + 1)
quadratic = {('A', 'B'): 8, ('A', 'C'): 8, ('A', 'D'): 8, ('A', 'E'): -4, ('B', 'C'): 8,
             ('B', 'D'): 8, ('B', 'E'): -4, ('C', 'D'): 8, ('C', 'E'): -4, ('D', 'E'): -4}
Q = dict(linear)
Q.update(quadratic)



# ---------- For Quantum Tests ----------
# Minor-embed and sample 1000 times on a default D-Wave system

# sampleset = sampler_auto.sample_qubo(Q, num_reads=1000)


# ---------- For Hybrid Tests ----------
sampleset = sampler_auto.sample_qubo(Q)




print(sampleset)
