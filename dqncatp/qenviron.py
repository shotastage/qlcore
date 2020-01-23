import numpy as np


class CATPActObject:

    def __init__(self):
        self._judge_route_from = ""
        self._judge_route_to = ""
        self._route_id = ""

class CATPEnvironment:

    def __init__(self):
        self._rewords = [ ]

    # Register or memory agent action flow.
    def act(self, act_obj):
        pass
    
    # Calculate environment diff and save environment.
    def commit(self):
        return sum(self._rewords)
    
    # Clear all environment to initial.
    def reset(self):
        total_reword = sum(self._rewords)

    def _capacity_validate(self, route_id):
        if True:
            return -10
