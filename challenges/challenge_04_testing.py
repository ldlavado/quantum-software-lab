"""Challenge 4: Quantum Testing

Objective: Distinguish deterministic from probabilistic results using pytest.

Time: 8-10 minutes
Level: Intermediate
"""

import pytest
from qiskit import QuantumCircuit
from quantum_lab.simulator import run_circuit


def circuit_h_then_h() -> QuantumCircuit:
    """Deterministic circuit: H + H returns to |0>."""
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.h(0)
    qc.measure(0, 0)
    return qc


def circuit_single_h() -> QuantumCircuit:
    """Probabilistic circuit: single H."""
    qc = QuantumCircuit(1, 1)
    qc.h(0)
    qc.measure(0, 0)
    return qc


# TODO: Complete or fix the tests below.
# Run with: pytest -q challenges/challenge_04_testing.py

def test_double_hadamard_is_deterministic():
    """H + H must return only 0 in ideal simulation."""
    qc = circuit_h_then_h()
    counts = run_circuit(qc, shots=1024, seed=42)
    # This assertion is correct
    assert counts.get("0", 0) == 1024


def test_single_hadamard_is_probabilistic():
    """Single H should be roughly 50/50. Do not require exact equality."""
    qc = circuit_single_h()
    counts = run_circuit(qc, shots=1024, seed=42)
    count_0 = counts.get("0", 0)
    # TODO: Fix this intentionally wrong assertion that demands exact 512
    # assert count_0 == 512   # <-- This is too strict and will fail due to statistical variation
    assert abs(count_0 - 512) < 100  # Reasonable margin


def test_grover_marks_correct_state():
    """After one Grover iteration the marked state should dominate."""
    # Import the function from the challenge (student must complete it)
    from challenges.challenge_03_grover import grover_circuit
    qc = grover_circuit("11")
    counts = run_circuit(qc, shots=1024, seed=42)
    # The marked state "11" should have the large majority of shots
    assert counts.get("11", 0) > 800


if __name__ == "__main__":
    pytest.main([__file__, "-q"])
