def copy_first_line(src_path: str, dest_path: str) -> None:
    first_line =""
    with open(src_path, "r") as file:
        first_line = file.readline().strip()

    with open(dest_path, "w") as file:
            file.write(first_line)

