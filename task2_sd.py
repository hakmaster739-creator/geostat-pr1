import numpy as np

well_dept = [56, 12, 66, 19, 32, 72, 27, 32]

# Крок 1: середнє значення
average = np.average(well_dept)                 # 39.5

# Крок 2: відхилення кожного значення від середнього
deviations = well_dept - average

# Крок 3: квадрати відхилень
squared_deviations = deviations ** 2

# Крок 4: середнє значення квадратів відхилень (дисперсія)
variance = np.mean(squared_deviations)          # 434.5

# Крок 5: квадратний корінь -> SD
SD = np.sqrt(variance)                          # 20.84...

print(average, variance, SD)
