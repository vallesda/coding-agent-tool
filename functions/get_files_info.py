import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    base_working_path = os.path.abspath(working_directory)
    full_working_path = os.path.abspath(os.path.join(working_directory, directory))

    if not full_working_path.startswith(base_working_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(full_working_path):
        return f'Error "{directory}" is not a directory'
    try:
        files_info = []
        for filename in os.listdir(full_working_path):
            filepath = os.path.join(full_working_path, filename)
            filesize = 0
            is_dir = os.path.isdir(filepath)
            filesize = os.path.getsize(filepath)
            files_info.append(
                f"- {filename}: file_size={filesize} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"
    
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrianed to working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),            
        }
    )
)