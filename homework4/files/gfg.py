from homework4.file_executor import create, write, delete

create.create_file(file_name=input("how you call file: "), extension=input("your extension: "))
write.write(file=input("type where your file: "), body=input("type text: "))
delete.delete_file(file=input("what delete: "))
