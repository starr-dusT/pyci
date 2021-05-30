# Simple state machine where: Waiting -> Ready -> Running -> Finished -|-> Succeeded
#                                                                      |
#                                                                      |-> Failed
#

def waiting():
    # TODO
    print("current state: waiting")
    # Next state is ready
    return "ready"


def ready():
    # TODO
    print("current state: running")
    # Next state is running
    return "running"


def running():
    # TODO
    print("current state: finished")
    # Next state is finished
    return "finished"


def finished():
    # TODO
    print("current state: waiting")
    # Next state is waiting
    return "waiting"


states = {"waiting": waiting,
          "ready": ready,
          "running": running,
          "finished": finished}
