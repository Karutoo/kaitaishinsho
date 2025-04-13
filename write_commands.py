import os


def get_command_names(directory):
    """
    Get the names of markdown files (without extension) in the specified directory.

    Args:
    - directory (str): The directory path.

    Returns:
    - list: A list of command names.
    """
    command_names = []
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            command_names.append(f'"{os.path.splitext(filename)[0]}"')
    return command_names


if __name__ == "__main__":
    # Specify the directory containing markdown files
    directory_path = "command"

    # Get command names
    command_names = get_command_names(directory_path)

    # Output command names to a file
    output_file_path = "commands.txt"

    if os.path.exists(output_file_path):
        os.remove(output_file_path)
        print(f"Removed {output_file_path}.")

    with open(output_file_path, 'w') as output_file:
        output_file.write('\n'.join(command_names))

    print(f"Command names have been saved to {output_file_path}.")
