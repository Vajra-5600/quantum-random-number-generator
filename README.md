# Quantum Random Number Generator (QRNG)

## F1 – Quantum Random Number Generator

A quantum random number generator (QRNG) uses quantum measurement to generate random bits. This project implements a simple 1-qubit QRNG using Qiskit and compares its output with a classical Python random number generator.

## Problem Statement

Classical random number generators use mathematical algorithms to produce pseudorandom values. This project explores quantum measurement as a source of random bits and evaluates whether the generated bits follow the expected 50/50 distribution.

## Solution

The project uses a single qubit initialized in the `|0⟩` state.

The quantum circuit is:

```text
|0⟩
  │
  H
  │
Measure
  │
  ├── 0
  └── 1