# Reverse Engineering Task

## Goal
Predict the output of `analyze.py` without running it.

## Rules
- Premium category: value * 1.1
- Standard category: value * 0.9
- Total is sum of all adjusted values
- Average is total / number of records

## Sample Calculation
- Alice (premium): 100 * 1.1 = 110.0
- Bob (standard): 200 * 0.9 = 180.0
- Carol (premium): 150 * 1.1 = 165.0
- Dave (standard): 80 * 0.9 = 72.0
- Eve (premium): 300 * 1.1 = 330.0
- Total: 857.0
- Average: 857.0 / 5 = 171.4
