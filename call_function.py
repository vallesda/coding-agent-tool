from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_files_content import schema_get_file_content
from functions.write_files_content import schema_write_file
from functions.run_python import schema_run_python_file

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file,
    ]
)