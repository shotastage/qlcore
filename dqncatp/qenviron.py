import numpy as np


class CATPActObject:

    def __init__(self):
        self._judge_route_from = ""
        self._judge_route_to = ""
        self._route_id = ""

    # Run defined action
    def run(self):
        pass


class CATPActEvaluate:
    
    def evaluate(self):
        pass


class CATPEnvironment:

    def __init__(self, evaluator, step_t):
        self._evaluator = evaluator
        self._step = step_t
        self._rewords = [ ]

    # Register or memory agent action flow.
    def act(self, act_obj):
        res = act_obj.run()
        rewords = self._evaluator(res)

        self._rewords.append(rewords)
    
    # Calculate environment diff and save environment.
    def commit(self):
        return sum(self._rewords)
    
    # Clear all environment to initial.
    def reset(self):
        total_reword = sum(self._rewords)

    def _capacity_validate(self, route_id):
        if True:
            return -10


