# 5. import these
from rest_framework.decorators import api_view
from rest_framework.response import Response

# 6. define a view (this is like router.get() in express node-js) but you add the url elsewhere
# 7. go to urls.py
@api_view(["GET"])
def hello_world(request):
    return Response("Hello World!")
