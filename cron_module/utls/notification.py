

class Notification:
    """
    Класс для сигнализирования
    """

    def global_notification(self) -> None:
        """
        Глобальное уведомление
        """
        pass

    def local_notification(self) -> None:
        """
        Локальное уведомление
        """
        pass
    
    def main_notification(self, type_func: str) -> None:
        """
        Метод реализации глобального и локального уведомления
        """

        func_dict = {
            "global": self.global_notification,
            "local": self.local_notification,
        }

        return func_dict[type_func]()
    
    def __init__(self) -> None:
        pass
