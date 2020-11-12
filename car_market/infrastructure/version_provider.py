class VersionProvider:
    def __init__(self, version_number: str):
        self.__version_number = version_number

    def get_version(self) -> str:
        return self.__version_number
