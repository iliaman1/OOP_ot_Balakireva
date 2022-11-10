CURRENT_OS = 'windows'  # 'windows', 'linux'


class WindowsFileDialog:
    def __init__(self, title: str, path: str, exts: tuple):
        self.__title = title
        self.__path = path
        self.__exts = exts


class LinuxFileDialog:
    def __init__(self, title: str, path: str, exts: tuple):
        self.__title = title
        self.__path = path
        self.__exts = exts


class FileDialogFactory:
    def __new__(cls, *args, **kwargs):
        return cls.create_windows_filedialog(args[0], args[1],
                                             args[2]) if CURRENT_OS == 'windows' else cls.create_linux_filedialog(
            args[0], args[1], args[2])

    @staticmethod
    def create_windows_filedialog(title: str, path: str, exts: tuple):
        return WindowsFileDialog(title, path, exts)

    @staticmethod
    def create_linux_filedialog(title: str, path: str, exts: tuple):
        return LinuxFileDialog(title, path, exts)
