class MysqlRepository:
    def __init__(self) -> None:
        self.__data = {
            "Aroudo": "Aroldo silva something here"
        }
        
    def select_by_name(self, name: str):
        if name in self.__data:
            return self.__data[name]
        return None
