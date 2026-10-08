# Business Brief – Quantum Random Number Generator

## 1. Customer

Potential customers include organizations that require reliable random numbers for security-sensitive applications, such as:

- Cybersecurity companies
- Financial institutions
- Secure communication providers
- Authentication and identity-management systems
- Research and technology organizations

## 2. Cost of the Problem

Many conventional random-number generators are algorithmic and produce pseudorandom values. For applications where the quality and unpredictability of randomness are important, relying only on algorithmic generation can create security and trust concerns.

Weak or predictable randomness can become a risk in applications such as cryptographic key generation, authentication, and secure communication.

## 3. Proposed Solution

This project provides a Quantum Random Number Generator using a one-qubit quantum circuit.

A Hadamard gate places the qubit into an equal superposition of 0 and 1. Measuring the qubit produces a random bit.

The implementation generates 10,000 bits and evaluates the output using bit balance and a chi-square statistical test. A classical Python random generator is also tested using the same number of bits for comparison.

## 4. Experimental Result

The quantum generator produced:

- 5,015 zeros
- 4,985 ones
- 49.85% ones
- Chi-square p-value: 0.7642

The classical generator produced:

- 4,962 zeros
- 5,038 ones
- 50.38% ones
- Chi-square p-value: 0.4473

Both outputs were consistent with the expected 50/50 distribution in this experiment.

## 5. Value / Result

The project demonstrates how quantum measurement can be used to generate random bits and provides a measurable comparison against a classical random-number generator.

The approach can serve as a foundation for exploring quantum randomness in cybersecurity, secure communications, authentication, and other applications requiring high-quality random values.

## 6. Limitations

The current implementation uses Qiskit's StatevectorSampler simulator rather than a physical quantum processor. Therefore, the experiment demonstrates the quantum circuit and its statistical behavior but does not by itself establish physical quantum entropy.

A future version can run the circuit on real IBM Quantum hardware.

## 7. Future Opportunity

The system can be extended to:

- Generate larger random-bit sequences
- Run on real quantum hardware
- Apply additional randomness tests
- Explore integration with cryptographic systems
- Investigate practical security applications