import numpy as np


class CATPActObject:

    def __init__(self):
        self._judge_route_from = ""
        self._judge_route_to = ""
        self._route_id = ""

class CATPEnvironment:

    def __init__(self):
        pass

    def commit(self):
        pass

    def action(self, act_obj):
        pass

    def _capacity_validate(self, route_id):
        
        if True:
            return -10
