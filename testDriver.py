##Dillon Patel and Rei Thao ProjectPhase 2.2
import sys

from Scanner import tokenize

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python test_driver.py input.txt output.txt")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]



if __name__ == "__main__":
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
        for line in input_file:
            line = line.strip()
            output_file.write(f"Line: {line}\n")
            try:
                tokens = tokenize(line)
                for token_type, token_value in tokens:
                    output_file.write(f"{token_value} : {token_type}\n")
            except Exception as e:
                output_file.write(f"ERROR READING '{e}'\n")
