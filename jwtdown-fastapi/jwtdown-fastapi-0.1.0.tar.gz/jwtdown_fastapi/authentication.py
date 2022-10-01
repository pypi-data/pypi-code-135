"""Utility classes to use for authentication in FastAPI.

The purpose of this module is to reduce the boilerplate
authentication code written for FastAPI. It is based on the
code that you can find at `OAuth2 with Password (and
hashing), Bearer with JWT tokens
<https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/>`_.
"""

from abc import ABC, abstractmethod
from fastapi import (
    APIRouter,
    Cookie,
    Depends,
    HTTPException,
    Request,
    Response,
    status,
)
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
import re
from typing import Any, Optional, Tuple, Union


password_key_matcher = re.compile(".*?password.*", re.IGNORECASE)


class Token(BaseModel):
    """Represents a bearer token."""

    access_token: str
    """Contains the encoded JWT"""

    token_type: str = "Bearer"
    """This is set to "Bearer" because it's a bearer token."""


class BadAccountDataError(RuntimeError):
    """Occurs when account data cannot be converted to a
    dictionary.

    Raised when trying to convert account data into a
    subject claim and a dictionary of account data.
    """

    pass


class Authenticator(ABC):
    """Provides authentication for FastAPI endpoints.


    Here's an example of creating the authenticator from a
    secret key stored in an environment variable.

    .. highlight:: python
    .. code-block:: python

        import os
        from jwtdown_fastapi import Authenticator


        class MyAuth(Authenticator):
            # Implement the abstract methods


        auth = MyAuth(os.environ["SECRET_KEY"])

    Parameters
    ----------
    key: ``str``
         The cryptographically strong signing key for JWTs.
    algorithm: ``str``
               The algorithm to use to sign JWTs. Defaults
               to HS256.
    cookie_name: ``str``
                 The name of the cookie to set in the
                 browser. Defaults to the value of
                 ``fastapi_token``.
    path: ``str``
          The path that authentication requests will go to.
          Defaults to "token".
    """

    def __init__(
        self,
        key: str,
        /,
        algorithm: str = "HS256",
        cookie_name: str = "fastapi_token",
        path: str = "token",
    ) -> Optional[dict]:
        self.cookie_name = cookie_name or self.COOKIE_NAME
        self.key = key
        self.algorithm = algorithm
        self.path = path
        self.scheme = OAuth2PasswordBearer(tokenUrl=path, auto_error=False)
        self._router = None
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

        async def try_account_data(
            self,
            bearer_token: Optional[str] = Depends(self.scheme),
            cookie_token: Optional[str] = (
                Cookie(default=None, alias=self.cookie_name)
            ),
        ):
            token = bearer_token
            if not token and cookie_token:
                token = cookie_token
            try:
                payload = jwt.decode(token, key, algorithms=[algorithm])
                return payload["account"]
            except (JWTError, AttributeError):
                pass
            return None

        setattr(
            self,
            "try_get_current_account_data",
            try_account_data.__get__(self, self.__class__),
        )

        async def account_data(
            self,
            data: dict = Depends(self.try_get_current_account_data),
        ) -> Optional[dict]:
            if data is None:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid token",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            return data

        setattr(
            self,
            "get_current_account_data",
            account_data.__get__(self, self.__class__),
        )

        async def login(
            self,
            response: Response,
            request: Request,
            form: OAuth2PasswordRequestForm = Depends(),
            account_getter=Depends(self.get_account_getter),
        ) -> Token:
            return await Authenticator.login(
                self,
                response,
                request,
                form,
                account_getter,
            )

        setattr(
            self,
            "login",
            login.__get__(self, self.__class__),
        )

    COOKIE_NAME = "fastapi_token"
    """The override value for the cookie name set by the
    authenticator.

    You can override the cookie name used by the
    authenticator with code like this.

    .. highlight:: python
    .. code-block:: python

        import os
        from jwtdown_fastapi import Authenticator


        class MyAuth(Authenticator):
            COOKIE_NAME = "custom_cookie_name"

            # Implement the abstract methods
    """

    @abstractmethod
    def get_account_getter(self, account_getter: Any) -> Any:
        """Gets the thing that gets account data for your
        application

        **You MUST implement this method in your custom
        class!**

        This method can be used to resolve your account
        getter, or just for returning the function or object
        that you use to get your account data.

        A typical implementation of this is just to use
        dependency injection for the thing you want from
        FastAPI, then return it. In the following code
        example, you have some class named
        ``AccountRepository`` that you use to get your
        account data. The implementation would look like
        this:

        .. highlight:: python
        .. code-block:: python

            def get_account_getter(
                self,
                account_repo: AccountRepository = Depends(),
            ) -> AccountRepository:
                return account_repo
        """
        pass

    @abstractmethod
    async def get_account_data(
        self,
        username: str,
        account_getter: Any,
    ) -> Optional[Union[BaseModel, dict]]:
        """Get the user based on a username.

        **You MUST implement this method in your custom
        class!**

        This method uses the ``account_getter`` returned
        from ``get_account_getter`` as the third argument.
        It's the job of this method to get the account data
        for the provided ``username``. ``username`` **can be
        an email!**

        .. highlight:: python
        .. code-block:: python

            def get_account_data(
                self,
                username: str,
                account_repo: AccountRepository,
            ) -> Account:
                return account_repo.get(username)

        Parameters
        ----------
        username: ``str``
            This is the value passed as the ``username`` in
            the log in form. It is the value that uniquely
            identifies a user in your application, such as a
            username or email.
        account_getter: ``Optional[Any]``
            Whatever thing you returned from
            ``account_getter``.

        Returns
        -------
        account_data: ``Optional[Union[BaseModel, dict]]``
            If the account information exists, it should
            return a Pydantic model or dictionary. If the
            account information does not exist, then this
            should return ``None``.
        """
        pass

    @abstractmethod
    def get_hashed_password(
        self,
        account_data: Union[BaseModel, dict],
    ) -> Optional[str]:
        """Gets the hashed password from account data.

        **You MUST implement this method in your custom
        class!**

        Just return the hashed password from the data that
        you get from your data store for the account.

        .. highlight:: python
        .. code-block:: python

            def get_hashed_password(self, account: Account):
                return account.hashed_password

        Parameters
        ----------
        account_data: ``Union[BaseModel, dict]``
            This will be whatever value is returned from
            ``get_account_data``

        Returns
        -------
        hashed_password: ``str``
            This is the hashed password stored when creating
            an account (because you should not store
            passwords in the clear anywhere)
        """
        pass

    def get_account_data_for_cookie(
        self,
        account_data: Union[BaseModel, dict],
    ) -> Tuple[str, dict]:
        """Converts account data to a dictionary

        This default implementation can accept either a
        Pydantic model or a dictionary. The value _must_
        contain the "email" property/key for the subject
        claim of the JWT that is generated from this data.

        If the resulting dictionary contains a key that is
        "*password*", then it will remove that key from the
        data for the cookie.

        .. highlight:: python
        .. code-block:: python

            # Implement this method if your account model
            # does NOT have an email property on/in it.
            def get_account_data_for_cookie(
                self,
                account: AccountOut
            ) -> Tuple[str, dict]:
                return account.username, account.dict()

        Parameters
        ----------
        account_data: ``Union[BaseModel, dict]``
            This will be whatever value is returned from
            get_account_data

        Raises
        ------
        BadAccountDataError
            If the account_data cannot be converted into a
            dictionary.

        Returns
        -------
        sub: ``str``
            This is the value for the "sub" claim of the
            JWT.
        data: ``dict``
            This is the data that will be encoded into the
            "account" claim of the JWT.
        """
        data = self._convert_to_dict(account_data)
        return data["email"], {
            key: value
            for key, value in data.items()
            if not password_key_matcher.match(key)
        }

    def hash_password(self, plain_password) -> str:
        """Hashes a password for secure storage.

        Use this method to hash your passwords so that they
        can later be verified by the authentication
        mechanism used by the ``Authenticator``.

        Use this method if you allow people to sign up for
        an account, for example. See the Quick Start.
        """
        return self.pwd_context.hash(plain_password)

    @property
    def router(self):
        """Get a FastAPI router that has login and logout
        handlers.

        Use this property to get a router to automatically
        register the ``login`` and ``logout`` path handlers
        for your application.

        .. highlight:: python
        .. code-block:: python

            from authenticator import authenticator
            from fastapi import APIRouter

            app = FastAPI()
            app.include_router(authenticator.router)
        """
        if self._router is None:
            router = APIRouter()
            router.post(f"/{self.path}", response_model=Token)(self.login)
            router.delete(f"/{self.path}", response_model=bool)(self.logout)
            self._router = router
        return self._router

    async def try_get_current_account_data(
        self,
        bearer_token: Optional[str] = Depends(OAuth2PasswordBearer("token")),
        cookie_token: Optional[str] = (
            Cookie(default=None, alias=COOKIE_NAME)
        ),
    ) -> dict:
        """Get account data for a request

        This method will return the dictionary that is in
        the "account" claim of the JWT found in either the
        Authorization header or the cookie.

        Use this method as a ``Depends`` when you want to
        get the current persons's account information from
        their token.

        If the token does not exist, you'll get a ``None``.

        .. highlight:: python
        .. code-block:: python

            @router.get("/api/things")
            async def get_things(
                account_data: Optional[dict] = Depends(authenticator.try_get_current_account_data),
            ):
                if account_data:
                    return personalized_list
                return general_list

        Returns
        -------
        data: ``dict``
            Returns the account data from the bearer token
            in the Authorization header or token. If the
            function can't decode the token, then it returns
            ``None``.
        """
        pass

    async def get_current_account_data(
        self,
        account: dict = Depends(try_get_current_account_data),
    ) -> dict:
        """Get account data for a request

        Like try_get_current_account_data, but raises an
        error if the account data cannot be found.

        Use this method as a ``Depends`` when you want to
        **protect** and endpoint to only be accessible by
        an someone that's got a JWT from logging in.

        If the token does not exist, the method will raise
        a 401 error.

        .. highlight:: python
        .. code-block:: python

            @router.post("/api/things")
            async def create_thing(
                account_data: dict = Depends(authenticator.get_current_account_data),
            ):
                pass

        Raises
        ------
        HTTPException
            If account data cannot be decoded from the JWT.

        Returns
        -------
        data: ``dict``
            Returns the account data from the bearer token
            in the Authorization header or token. If the
            function can't decode the token, then it returns
            ``None``.
        """
        pass

    async def login(
        self,
        response: Response,
        request: Request,
        form: OAuth2PasswordRequestForm = Depends(),
        account_getter=Depends(get_account_getter),
    ) -> Token:
        account = await self.get_account_data(form.username, account_getter)
        if not account:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        hashed_password = self.get_hashed_password(account)
        if not self.pwd_context.verify(form.password, hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        sub, data = self.get_account_data_for_cookie(account)
        data = self._convert_to_dict(data)
        jwt_data = {"sub": sub, "account": data}
        encoded_jwt = jwt.encode(jwt_data, self.key, algorithm=self.algorithm)
        samesite, secure = self._get_cookie_settings(request)
        response.set_cookie(
            key=self.cookie_name,
            value=encoded_jwt,
            httponly=True,
            samesite=samesite,
            secure=secure,
        )
        token = {"access_token": encoded_jwt, "token_type": "Bearer"}
        return token

    async def logout(self, request: Request, response: Response):
        samesite, secure = self._get_cookie_settings(request)
        response.delete_cookie(
            key=self.cookie_name,
            httponly=True,
            samesite=samesite,
            secure=secure,
        )
        return True

    def _get_cookie_settings(self, request: Request):
        headers = request.headers
        samesite = "none"
        secure = True
        if "origin" in headers and "localhost" in headers["origin"]:
            samesite = "lax"
            secure = False
        return samesite, secure

    def _convert_to_dict(self, data):
        if hasattr(data, "dict") and callable(data.dict):
            data = data.dict()
        if not isinstance(data, dict):
            raise BadAccountDataError(
                message="Account data is not dictionary-able",
                account_data=data,
            )
        return data
