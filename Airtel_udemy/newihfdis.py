import subprocess

def normalize_python_file(file_path):
    try:
        subprocess.run(["black", file_path], check=True)
        print("Code normalized successfully!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    file_name = input("Enter Python file name (e.g., test.py): ")
    normalize_python_file(file_name)
    