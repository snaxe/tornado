import json
from sqlalchemy.ext.declarative import DeclarativeMeta

class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        fields=None
        if isinstance(obj.__class__, DeclarativeMeta):
            isvisited=False
            try:
                isvisited=obj.__getattribute__("visited")
            except:
                isvisited=False
            # an SQLAlchemy class
            if isvisited!=True:
                fields={}
                """Creates issue for recursive nesting. Need to create mp instead for parent-child relation visited field"""
                obj.visited = True
                for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata' and x!='visited']:
                    data = obj.__getattribute__(field)
                    try:
                        # this will fail on non-encodable values, like other classes
                        fields[field] = json.loads(json.dumps(data,cls=AlchemyEncoder))
                    except TypeError:
                        fields[field] = None
                # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)