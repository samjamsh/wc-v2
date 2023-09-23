try:
    from sys import argv

    exit(f"use: python3 {argv[0]} filename") if len(argv) == 1 else print("",end="");

    files_name = argv[1:]

    for file_name in files_name:

        file_lenght = 0 # bytes lenght
        file_breaklines = 0 # \n lenght
        file_lines = 0 # file writted lines or exacly file used lines

        with open(file_name, "rb", buffering=1024 * 1024) as file_bytes:

            for bytes in file_bytes:

                file_lenght += len(bytes) # incrementing total bytes lenght by current being read bytes lenght

                file_breaklines += 1 # incrementing 1 to total \n's by each time the file/data is read (filedata is being read line by line)

                if bytes != "\n".encode() or len(bytes) > 1: file_lines += 1

            print(f"the file has {file_breaklines} breaklines \\n  |  {file_lines} lines  |  {file_lenght} bytes")

except Exception as error:
    exit(error)
