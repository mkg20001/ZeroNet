try:
    from FileServer import FileServer
    from FileRequest import FileRequest
except Exception as errr:
    from File.FileServer import FileServer
    from File.FileRequest import FileRequest
