def read_file(path):
    """Read and return the contents of a file."""
    try:
        with open(path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "File not found"


def write_file(path, content):
    """Write content to a file."""
    with open(path, "w") as f:
        f.write(content)
        return "File written successfully"


def append_file(path, content):
    """Append content to a file."""
    with open(path, "a") as f:
        f.write(content)
        return "Content appended successfully"
