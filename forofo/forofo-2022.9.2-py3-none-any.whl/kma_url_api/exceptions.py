from fastapi.exceptions import HTTPException as FastAPIHTTPException


# DataGoKr Base Exception
class KmaUrlApiException(FastAPIHTTPException):
    status_code: int = 200

    def __init__(
        self,
        headers: dict,
    ):
        super().__init__(
            status_code=self.status_code,
            detail=f"KmaUrlApiException [{headers['resultCode']}] {headers['resultMsg']}",
            headers=headers,
        )

    def __str__(self):
        return self.detail
