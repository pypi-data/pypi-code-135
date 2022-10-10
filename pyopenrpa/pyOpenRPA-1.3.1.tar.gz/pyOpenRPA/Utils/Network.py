import requests

def RequestPrettyPrint(inRequest):
    """
    At this point it is completely built and ready
    to be fired; it is "prepared".
    However pay attention at the formatting used in
    this function because it is programmed to be pretty
    printed and may differ from the actual request.
    """
	prepared = inRequest.prepare()
    print('{}\n{}\r\n{}\r\n\r\n{}'.format(
        '-----------START-----------',
        prepared.method + ' ' + prepared.url,
        '\r\n'.join('{}: {}'.format(k, v) for k, v in prepared.headers.items()),
        prepared.body,
    ))