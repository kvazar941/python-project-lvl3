"""FIle writer module."""
ERROR = "Cannot create file '{0}' at the specified path."


def write_file(way, content_file, mode='w+'):
    """
    Write file.

    Args:
        way: str
        content_file: any
        mode: str
    """
    text_explanation = '\n'.join([
        'Check the permissions on the path to the file.',
        "If it's a network drive,",
        'check if the drive is accessible over the network.',
        'The program terminates.',
        'The page and resource is not loaded.',
    ])
    try:
        with open(way, mode) as file_name:
            file_name.write(content_file)
    except OSError:
        raise OSError(''.join([ERROR.format(way), text_explanation]))
