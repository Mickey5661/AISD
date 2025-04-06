def process_stack_operations(input_file: str, output_file: str):
    with open(input_file, "r") as infile:
        lines = infile.readlines()

    M = int(lines[0].strip())
    stack = []
    results = []

    for i in range(1, M + 1):
        command = lines[i].strip()
        if command.startswith("+"):
            _, number = command.split()
            stack.append(int(number))
        elif command == "-":
            results.append(str(stack.pop()))

    with open(output_file, "w") as outfile:
        outfile.write("\n".join(results) + "\n")

process_stack_operations("input2.txt", "output2.txt")