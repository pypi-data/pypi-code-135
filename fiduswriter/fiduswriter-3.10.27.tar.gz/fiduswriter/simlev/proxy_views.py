import time

from tornado.web import RequestHandler
from tornado.httpclient import AsyncHTTPClient
from base.django_handler_mixin import DjangoHandlerMixin
from django.conf import settings

from publish.models import Publication

class Proxy(DjangoHandlerMixin, RequestHandler):
    async def post(self, _relative_url):
        user = self.get_current_user()
        if not user.is_authenticated:
            self.set_status(401)
            self.finish()
            return
        body = self.request.body
        headers=self.request.headers
        url = f"{settings.SIMLEV_URL}/api/publish_post/?api_key={settings.SIMLEV_API_KEY}"
        http = AsyncHTTPClient()
        response = await http.fetch(url, method="POST", body=body, headers=headers, request_timeout=88)
        if response.error:
            self.write(response.body)
            self.set_status(response.code)
            self.finish()
            return
        doc_id = self.get_argument('doc_id', None)
        publication, created = Publication.objects.get_or_create(
            document_id=doc_id,
            defaults={"submitter_id": user.id}
        )
        if created:
            self.set_status(201)
        else:
            self.set_status(200)
        publication.status = "published"
        message = {
            "type": "publish",
            "message": self.get_argument("message", ""),
            "user": user.readable_name,
            "time": time.time(),
        }
        publication.messages.append(message)
        publication.save()
        self.write({'message': message})
        self.finish()
