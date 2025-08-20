# version3_file_input_single.py

# Open the file and read inputs
with open("inputs_single.txt", "r") as f:
    lines = f.readlines()

# Convert file lines into floats (strip removes \n and spaces)
a = float(lines[0].strip())
b = float(lines[1].strip())
c = float(lines.strip())
t = float(lines.strip())

# Quadratic temperature prediction model
T = a * (t**2) + b * t + c

print(f"Predicted temperature at t={t}: {T:.2f}°C")
