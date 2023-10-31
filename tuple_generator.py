# Define the range for the variable
min_variable = 1
max_variable = 500

# Specify the file name
file_name = "output_lines.txt"

# Generate the lines with the "VARIABLE" in a sequence and write them to the file
with open(file_name, 'w') as file:
    for variable in range(min_variable, max_variable + 1):
        line = f"  - name: Iteration {variable}\n    check:\n      - user: user:anne\n        object: organization:acme\n        assertions:\n          member: true\n      - user: user:anne\n        object: group:everyone\n        assertions:\n          member: true\n      - user: user:john\n        object: folder:general\n        assertions:\n          viewer: true\n      - user: user:anne\n        object: document:welcome\n        assertions:\n          viewer: true\n      - user: user:peter\n        object: document:welcome\n        assertions:\n          viewer: true\n"
        file.write(line + "\n")

print(f"{max_variable} lines written to {file_name}")
