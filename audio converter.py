import os
import subprocess

input_file_name = input("Enter the name of the input video file (with extension): ")
output_file_name = input("Enter the name of the output audio file (with extension): ")

input_file = os.path.join(os.path.expanduser("~"), "Downloads", input_file_name)
output_file = os.path.join(os.path.expanduser("~"), "Downloads", output_file_name)

#Extract audio from the video using FFmpeg
command = [
    "ffmpeg",
    "-ss", "00:00:00", 
    "-i", input_file,
    "-vn",  
    "-c:a", "libmp3lame",  
    "-q:a", "2",  
    output_file
]
subprocess.call(command)

