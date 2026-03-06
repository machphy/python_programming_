import subprocess
import os

def convert_dvr_to_mp4(input_file, output_file):
    try:
        command = [
            "ffmpeg",
            "-i", input_file,
            "-vcodec", "libx264",
            "-acodec", "aac",
            output_file
        ]

        subprocess.run(command, check=True)
        print("Conversion completed:", output_file)

    except subprocess.CalledProcessError:
        print("Error during conversion")

def main():
    input_file = input("Enter DVR file path: ")
    
    if not os.path.exists(input_file):
        print("File not found")
        return

    output_file = os.path.splitext(input_file)[0] + ".mp4"
    
    convert_dvr_to_mp4(input_file, output_file)

if __name__ == "__main__":
    main()