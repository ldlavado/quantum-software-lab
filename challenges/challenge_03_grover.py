"""Challenge 3: Grover with 2 qubits (educational)

Objective: Implement a simplified Grover search that marks one state.

Time: 10-12 minutes
Level: Intermediate

This is a didactic example only. It does not demonstrate practical
speedup over a classical CPU for four options.
"""

from qiskit import QuantumCircuit
from quantum_lab.simulator import run_circuit, get_statevector
from quantum_lab.utils import format_counts


def oracle_mark_11() -> QuantumCircuit:
    """Oracle that marks the state |11> by applying a phase of -1.

    For educational purposes, a simple Z on both qubits when both are 1
    can be approximated, but we use a controlled-Z equivalent.
    """
    oracle = QuantumCircuit(2, name="Oracle")
    # Mark |11> with a phase flip (equivalent to CZ for this case)
    oracle.cz(0, 1)
    return oracle


def diffusion_operator() -> QuantumCircuit:
    """Incomplete diffusion operator for 2 qubits.

    TODO: Complete the diffusion (inversion about the mean):
    - H on both qubits
    - X on both qubits
    - CZ (or controlled phase)
    - X on both qubits
    - H on both qubits
    """
    diff = QuantumCircuit(2, name="Diffusion")

    # TODO: H on both
    # diff.h([0, 1])

    # TODO: X on both
    # diff.x([0, 1])

    # TODO: Controlled phase (CZ)
    # diff.cz(0, 1)

    # TODO: X on both
    # diff.x([0, 1])

    # TODO: H on both
    # diff.h([0, 1])

    return diff


def grover_circuit(marked: str = "11") -> QuantumCircuit:
    """Build one iteration of Grover for 2 qubits.

    Args:
        marked: Which state to mark (default "11"). Currently only "11" is fully supported.
    """
    qc = QuantumCircuit(2, 2)

    # Initial superposition
    qc.h([0, 1])

    # Oracle
    if marked == "11":
        qc.compose(oracle_mark_11(), inplace=True)
    # Optional extension: implement other oracles

    # Diffusion
    qc.compose(diffusion_operator(), inplace=True)

    # Measure
    qc.measure([0, 1], [0, 1])
    return qc


def main():
    print("=== Challenge 3: Grover (2 qubits, educational) ===\n")
    print("PREDICT: After one iteration, which state should have probability close to 1?\n")

    qc = grover_circuit("11")
    # Uncomment after completing the diffusion TODOs
    # counts = run_circuit(qc, shots=1024, seed=42)
    # print(format_counts(counts))

    print("\nREFLECT:")
    print("- Did the marked state dominate?")
    print("- This is a teaching example. It is NOT evidence of practical quantum speedup")
    print("  for a search space of only 4 elements.")
    print("- Grover does not 'read all states at once'.")


if __name__ == "__main__":
    main()
