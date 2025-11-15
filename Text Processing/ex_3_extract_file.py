file_path = input().split("\\")
file_name, extension = file_path[-1].split(".")
print(f"File name: {file_name}\n"
      f"File extension: {extension}")
