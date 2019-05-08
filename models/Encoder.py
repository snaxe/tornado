import json
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm.collections import InstrumentedList
class AlchemyEncoder(json.JSONEncoder):
    def __init__(self, options=None, **kwargs):
        super(AlchemyEncoder, self).__init__(**kwargs)
        self.options = options

    def default(self, obj):
        fields = None
        if isinstance(obj.__class__, DeclarativeMeta):
            if '_visited' not in dir(obj) or not obj._visited:
                fields={}
                obj._visited = True
                for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                    data = obj.__getattribute__(field)
                    if not isinstance(data.__class__, DeclarativeMeta) and not issubclass(data.__class__,InstrumentedList):
                        try:
                            fields[field] = json.loads(json.dumps(data))
                        except TypeError:
                            fields[field] = None
                    elif field not in self.options['expand']:
                        try:
                            fields[field] = None
                        except TypeError:
                            fields[field] = None
                    else:
                        try:
                            fields[field] = json.loads(json.dumps(data,cls=AlchemyEncoder,options=self.options))
                        except TypeError:
                            fields[field] = None

            return fields

        return json.JSONEncoder.default(self, obj)