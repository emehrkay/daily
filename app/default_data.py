# script used to import the default data into the system
import sys

import api.config
from api.bootstrap import MAPPER
from api.model.graph.vertex import *


try:
    gremlin = MAPPER.gremlin
    MAPPER.query(script="g.V().map{it.get().remove()}")

    mark = MAPPER.create_model(data={'username': 'mark', 'password': 'mark', 'email': 'mark.henderson@8trk.com'}, model_class=User)

    MAPPER.save(mark).send()

except Exception as e:
    import traceback
    print(traceback.format_exc())
    traceback.print_stack(file=sys.stdout)
    print(e)