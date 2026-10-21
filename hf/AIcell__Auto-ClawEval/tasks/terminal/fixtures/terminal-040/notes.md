# Reverse Engineering Task

## Goal
Analyze `mystery.py` and predict its output without running it.

## Functions
- `encode(text, shift)`: Caesar cipher for letters, rotates digits by shift mod 10
- `decode(text, shift)`: Reverses the encoding
- `count_vowels(text)`: Counts vowels (a, e, i, o, u) case-insensitively
- `reverse_words(sentence)`: Reverses word order in a sentence
- `checksum(text)`: Sum of ASCII values mod 256

## Test Cases
| Text              | Shift |
|-------------------|-------|
| Hello, World!     | 3     |
| Python3 is great! | 5     |
| abc XYZ 789       | 13    |
| The quick brown fox | 7   |

## Expected Output
See `expected_output.txt` for the full expected output.
