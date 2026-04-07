# Statistical Engineering Project

## Overview
This project implements a statistical engine and Monte Carlo simulation.

## Features
- Mean, Median, Mode
- Variance (sample & population)
- Standard deviation
- Outlier detection
- Monte Carlo simulation

## Mathematical Logic
Variance:
Sample: Σ(x - x̄)² / (n - 1)  
Population: Σ(x - μ)² / N  

Median:
- Odd → middle value  
- Even → average of two middle values  

## How to Run
python main.py

## Testing
python -m unittest

## Acceptance Checklist
✔ Handles empty list  
✔ Handles invalid data  
✔ Correct variance calculation  
✔ Detects outliers  
✔ Tests included  
