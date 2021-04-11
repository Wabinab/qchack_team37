from qiskit import *
from numpy.random import randint
import numpy as np


def encode_message(bits, bases):
    """Creates a list of QC each repr a single qubit in Alice's message."""
    message = []
    
    n = len(bits)
    
    for i in range(n):
        qc = QuantumCircuit(1, 1)

        if bits[i] == 1:
            qc.x(0)
        if bases[i] == 1:
            qc.h(0)
        qc.barrier()
        message.append(qc)
    return message


def measure_message(message, bases):
    """Applies corr measurement and simulates the result of measuring each qubit.
    Return measurement results."""
    backend = Aer.get_backend("qasm_simulator")
    
    n = len(bases)

    measurements = []
    for q in range(n):
        if bases[q] == 1:  # measure X basis
            message[q].h(0)
        message[q].measure(0, 0)

        qasm_sim = Aer.get_backend("qasm_simulator")
        qobj = assemble(message[q], shots=1, memory=True)

        # qasm_sim = provider.get_backend("ibmq_quito")
        # transpiled_qc = transpile(message[q], qasm_sim, optimization_level=3)
        # qobj = assemble(transpiled_qc, shots=1, memory=True)
        job = qasm_sim.run(qobj)
        # job_monitor(job, interval=2)

        result = job.result()
        measured_bit = int(result.get_memory()[0])
        measurements.append(measured_bit)

    return measurements


def remove_garbage(a_bases, b_bases, bits):
    """Throw entry away if different bases measured. Retain same basis bits.
    :return good bits."""
    good_bits = []
    
    n = len(a_bases)

    for q in range(n):
        if a_bases[q] == b_bases[q]:
            good_bits.append(bits[q])

    return good_bits


def sample_bits(bits, selection):
    sample = []

    for i in selection:
        i = np.mod(i, len(bits))
        sample.append(bits.pop(i))
    return sample