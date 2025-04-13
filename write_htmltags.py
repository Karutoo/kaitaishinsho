import os


def get_html_tags(directory):
    """
    Get the names of markdown files (without extension) in the specified directory.

    Args:
    - directory (str): The directory path.

    Returns:
    - list: A list of command names.
    """
    html_tags = []
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            html_tags.append(f'"{os.path.splitext(filename)[0]}"')
    return html_tags


if __name__ == "__main__":
    # Specify the directory containing markdown files
    directory_path = "html"

    # Get html_tags
    html_tags = get_html_tags(directory_path)

    # Output html_tags to a file
    output_file_path = "html_tags.txt"

    if os.path.exists(output_file_path):
        os.remove(output_file_path)
        print(f"Removed {output_file_path}.")

    with open(output_file_path, 'w') as output_file:
        output_file.write('\n'.join(html_tags))

    print(f"Html_tags have been saved to {output_file_path}.")
