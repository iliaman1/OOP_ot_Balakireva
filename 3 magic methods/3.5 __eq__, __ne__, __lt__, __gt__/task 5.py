class FileAcceptor:
    def __init__(self, *args: str) -> None:
        self.list_ext = list(args)

    def __add__(self, other):
        res = self.list_ext + other.list_ext
        return FileAcceptor(*res)

    def __call__(self, filename, *args, **kwargs):
        for i in self.list_ext:
            if f".{i}" in filename:
                return True

        return False


filenames = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls"]

acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
res = acceptor_images + acceptor_docs
filenames = list(filter(acceptor_images + acceptor_docs, filenames))
print(filenames)


