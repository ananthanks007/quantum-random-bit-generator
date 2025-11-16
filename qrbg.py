import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator


def quantum_random_bit(N):
    qr = QuantumRegister(N, 'q')
    cr = ClassicalRegister(N, 'c')
    qc = QuantumCircuit(qr, cr)
    qc.h(qr) # Applying Hadamard gate to all qubits
    qc.measure(qr, cr)


    sim = AerSimulator()
    job = sim.run(qc, shots=1)
    result = job.result()
    random_bit = list(result.get_counts().keys())[0]
    return random_bit



