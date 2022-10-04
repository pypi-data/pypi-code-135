from abc import ABC, abstractmethod


class IAuthProvider(ABC):
    @abstractmethod
    def authorize(self, username: str, password: str) -> str:
        """
        Авторизует пользователя
        :return: Токен авторизации
        """

    @abstractmethod
    def authenticate(self, auth_token: str) -> int:
        """
        Аутентифицирует пользователя
        :param auth_token: токен авторизации
        :return: ID пользователя
        """
