from flask.views import MethodView
from .mixins import ListModelMixin, RetrieveMixin

class APIView:
    queryset = None
    serializer = None

    def get_queryset(self, lookup_field=None):
        if not lookup_field:
            return self.queryset
        else:
            print(self.queryset[int(lookup_field)], '***************************')
            return self.queryset[int(lookup_field)]
    def get_serializer(self, queryset, **kwargs):
        return self.serializer(queryset, **kwargs)


class ListView(MethodView, APIView, ListModelMixin):

    def get(self, *args, **kwargs):
        return self.list(*args, **kwargs)


class RetrieveView(MethodView, APIView, RetrieveMixin):

    def get(self, *args, **kwargs):
        return self.retrieve(*args, **kwargs)