import json

class CharField:
    pass

class MethodField:
    pass


class SingleSerializer(object):
    def __init__(self, query_data, **kwargs):
        self.query_data = query_data
        self.many = kwargs.pop('many', False)

    def get_data(self, query_data):
        serialized_data = {}
        for field, field_obj in self.__class__.__dict__.items():
            if isinstance(field_obj, CharField):
                serialized_data[field] = getattr(query_data, field)
            elif isinstance(field_obj, MethodField):
                field_handler = getattr(self, 'get_{}'.format(field))
                serialized_data[field] = field_handler(query_data)
        return serialized_data

    @property
    def data(self):
        return json.dumps(self.get_data(self.query_data))


class Serializer(SingleSerializer):

    def get_data(self, query_data):
        serialized_data = []
        if not getattr(self, '_data', None):
            if not self.many:
                serialized_data = super(Serializer, self).get_data(query_data)
            else:
                for query_obj in query_data:
                    ret = super(Serializer, self).get_data(query_obj)
                    serialized_data.append(ret)
        self._data = serialized_data
        return self._data

    @property
    def data(self):
        return json.dumps(self.get_data(self.query_data))
