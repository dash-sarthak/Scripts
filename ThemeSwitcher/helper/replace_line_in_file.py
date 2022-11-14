def replace_line(file_path: str, line_nr: int, new_line: str):
    """Replaces line in a file

    Args:
        file_path (str): path to the file
        line_nr (int): line number of the line to be replaced
        new_line (str): string containing the new line
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    lines[line_nr] = new_line + '\n'

    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(lines)
