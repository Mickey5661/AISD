def process_votes(input_file, output_file):
    votes = {}

    with open(input_file, 'r') as infile:
        for line in infile:
            candidate, count = line.strip().split()
            count = int(count)
            if candidate in votes:
                votes[candidate] += count
            else:
                votes[candidate] = count

    with open(output_file, 'w') as outfile:
        for candidate in sorted(votes.keys()):
            outfile.write(f"{candidate} {votes[candidate]}\n")

def main():
    process_votes('input5.txt', 'output5.txt')

if __name__ == "__main__":
    main()