filename = input("Enter the file name: ")
media={
    "png":"image/png",
    "jpg":"image/jpg",
    "jpeg":"image/jpeg",
    "txt":"file/txt",
    "docx":"file/docx",
    "pdf":"file/pdf",
    "gif":"image/gif",
    "exe":"app/exe",
    "py":"file/py",
    "java":"file/java",
}
extension = filename.split(".")[-1]
if extension in media:
    print(media[extension]) 






