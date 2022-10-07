import aiohttp
import requests
from .models.email_status import EmailStatus


class AioPizzaValidator:
    def __init__(self, session=None):
        """
        Asynchronous Pizza Validator client.
        """
        self.session = session or aiohttp.ClientSession()

    async def close(self):
        """
        Close the session.
        """
        await self.session.close()

    async def validate(self, email: str) -> EmailStatus:
        """
        Validate email.
        Return a EmailStatus object.
        """
        mode = "email" if "@" in email else "domain"

        response = await self.session.get(f"https://api.mailcheck.ai/{mode}/{email}")
        if response.status != 200:
            raise Exception(f"Error: {response.status} - Fail to validate domain.")

        data = await response.json()
        return EmailStatus(**data)

    async def is_disposable(self, email: str) -> bool:
        """
        Validate email.
        Return a boolean.
        """

        email_status = await self.validate(email)
        return email_status.disposable


class PizzaValidator:
    @staticmethod
    def validate(email: str) -> EmailStatus:
        """
        Validate email.
        Return a EmailStatus object.
        """

        mode = "email" if "@" in email else "domain"

        response = requests.get(f"https://api.mailcheck.ai/{mode}/{email}")
        if response.status_code != 200:
            raise Exception(f"Error: {response.status} - Fail to validate domain.")

        data = response.json()
        return EmailStatus(**data)

    @staticmethod
    def is_disposable(email: str) -> bool:
        """
        Validate domain.
        Return a boolean.
        """

        email_status = PizzaValidator.validate(email)
        return email_status.disposable
