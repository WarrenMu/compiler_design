# tooling/command_line.py

import sys

def compile_file(file_path):
    # Compile the specified file
    # Your compilation logic goes here
    print("Compiling file:", file_path)

def run_file(file_path):
    # Run the compiled file
    # Your execution logic goes here
    print("Running file:", file_path)

def main():
    if len(sys.argv) < 3:
        print("Usage: python command_line.py [compile|run] <file>")
        return

    action = sys.argv[1]
    file_path = sys.argv[2]

    if action == "compile":
        compile_file(file_path)
    elif action == "run":
        run_file(file_path)
    else:
        print("Invalid action. Use 'compile' or 'run'.")

if __name__ == "__main__":
    main()
