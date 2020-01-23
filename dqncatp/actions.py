import numpy as np




class CATPAction:

    def __init__(self):
        pass

    def reset(self):
        print("Reset environment")

    # Register agent action to environment
    def act(self, act_obj):
        pass

    # Calculate environment diff
    def commit(self):
        print("Committing environment...")

    def _capacity_validate(self, route_id):
        
        if True:
            return -10
