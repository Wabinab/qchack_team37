from qiskit import *


def random_number_generator(num_qubits):
    """
    Generate and return a list of random numbers. 
    
    Not exactly as discussed in https://www.nature.com/articles/s41598-019-56706-2 as I made modifications. 
    Also there are lots of flaws for this random number generator without correct implementation. 
    """
    n = num_qubits
    
    rnd_gen = QuantumCircuit(n)

    rnd_gen.h(range(n - 1))

    for i in range(n - 1):
        rnd_gen.cnot(i, n - 1)  # Because qubit starts from 0 and ends at 19. 

    rnd_gen.measure_all()
    
    answer = run_for_result(rnd_gen)
    
    random_numbers = [key for key in answer.keys()]
    
    return random_numbers


def run_for_result(qc, backend=None):
    """
    Run on simulator and plot. 
    :var qc: Quantum Circuit. 
    """
    
    qobj = assemble(qc, shots=1000)
    
    if backend == None: 
        backend = Aer.get_backend("qasm_simulator")
    else:
        backend = backend
    
    results = backend.run(qobj).result()
    answer = results.get_counts()  # Counts retrieval. 
    
    return answer