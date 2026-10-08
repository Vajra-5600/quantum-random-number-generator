from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler
from scipy.stats import chi2
import matplotlib.pyplot as plt
import pandas as pd
import random
SHOTS = 10000
sampler = StatevectorSampler(
    default_shots=SHOTS,
    seed=42
)
qc = QuantumCircuit(1)
qc.h(0)
qc.measure_all()
result = sampler.run([qc]).result()
counts = result[0].data.meas.get_counts()
print("Quantum counts:")
print(counts)
quantum_bits = []
for bit, count in counts.items():
    quantum_bits.extend([int(bit)] * count)
print("Total quantum bits:", len(quantum_bits))
print("First 50 bits:")
print(quantum_bits[:50])
zeros = quantum_bits.count(0)
ones = quantum_bits.count(1)
zero_percentage = zeros / SHOTS * 100
one_percentage = ones / SHOTS * 100
print("Zeros:", zeros)
print("Ones:", ones)
print(f"0 percentage: {zero_percentage:.2f}%")
print(f"1 percentage: {one_percentage:.2f}%")
imbalance = abs(zero_percentage - one_percentage)
print(f"Absolute imbalance: {imbalance:.2f}%")
expected = SHOTS / 2
chi_square = (
    (zeros - expected) ** 2 / expected + (ones - expected) ** 2 / expected)
p_value = chi2.sf(chi_square, df=1)
print("Chi-square statistic:", chi_square)
print("p-value:", p_value)
if p_value > 0.05:
    print("PASS: Output is consistent with a 50/50 distribution.")
else:
    print("FLAG: Output shows significant deviation from 50/50.")
    random.seed(42)
classical_bits = [
    random.getrandbits(1)
    for _ in range(SHOTS)
]
print("Total classical bits:", len(classical_bits))
print("First 50 bits:")
print(classical_bits[:50])
classical_zeros = classical_bits.count(0)
classical_ones = classical_bits.count(1)
classical_zero_percentage = classical_zeros / SHOTS * 100
classical_one_percentage = classical_ones / SHOTS * 100
print("Classical zeros:", classical_zeros)
print("Classical ones:", classical_ones)
print(f"0 percentage: {classical_zero_percentage:.2f}%")
print(f"1 percentage: {classical_one_percentage:.2f}%")
expected = SHOTS / 2
classical_chi_square = (
    (classical_zeros - expected) ** 2 / expected + (classical_ones - expected) ** 2 / expected )
classical_p_value = chi2.sf(classical_chi_square,df=1)
print("Classical Chi-square:", classical_chi_square)
print("Classical p-value:", classical_p_value)
if classical_p_value > 0.05:
    print("PASS: Classical output is consistent with 50/50.")
else:
    print("FLAG: Classical output shows deviation from 50/50.")
comparison = pd.DataFrame({
    "Generator": [
        "Qiskit Quantum",
        "Python Random"
    ],
    "Zeros": [
        zeros,
        classical_zeros
    ],
    "Ones": [
        ones,
        classical_ones
    ],
    "0 Percentage": [
        zero_percentage,
        classical_zero_percentage
    ],
    "1 Percentage": [
        one_percentage,
        classical_one_percentage
    ],
    "Chi-Square": [
        chi_square,
        classical_chi_square
    ],
    "P-Value": [
        p_value,
        classical_p_value
    ]
})
print("\nComparison Table:")
print(comparison.to_string(index=False))
generators = ["Qiskit Quantum", "Python Random"]
one_percentages = [
    one_percentage,
    classical_one_percentage
]
plt.figure(figsize=(8,5))
bars = plt.bar(
    generators,
    one_percentages
)
plt.axhline(
    50,
    linestyle="--",
    label="Ideal 50%"
)
plt.ylabel("Percentage of 1s")
plt.xlabel("Random Number Generator")
plt.title("Quantum vs Classical Random Number Generation")
plt.ylim(45, 55)
plt.legend()
for bar, value in zip(bars, one_percentages):
    plt.text(
        bar.get_x() + bar.get_width()/2,
        value + 0.1,
        f"{value:.2f}%",
        ha="center"
    )
plt.tight_layout()
plt.savefig(
    "qrng_comparison.png",
    dpi=300
)
plt.show()
