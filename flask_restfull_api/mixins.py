


class ListModelMixin(object):
    def list(self, *args, **kwargs):
        print(self.queryset, self.serializer)
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return serializer.data


class RetrieveMixin(object):
    def retrieve(self, *args, **kwargs):
        lookup_field = kwargs.pop('pk', None)
        queryset = self.get_queryset(lookup_field)
        serializer = self.get_serializer(queryset)
        return serializer.data