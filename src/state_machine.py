# imports
import time
import waiting as wt
import config as config

# Simple state machine where: Waiting -> Ready -> Running -> Finished -|-> Succeeded
#                                                                      |
#                                                                      |-> Failed
#


def waiting():
    # TODO
    print("current state: waiting")
    # Next state is ready
    return wt.eval_state()


def ready():
    # TODO
    print("current state: ready")
    # Next state is running
    return "running"


def running():
    # TODO
    print("current state: running")
    # Next state is finished
    return "finished"


def finished():
    # TODO
    print("current state: finished")
    # Next state is waiting
    return "waiting"


def cycle_machine(states, initial_state):
    # Initialize current and next states
    next_state = None
    current_state = initial_state

    # Start an infinite loop
    while 1:
        next_state = states[current_state]()
        current_state = next_state
        time.sleep(1)


def start_machine():
    print("starting machine...")
    # Define the machine's states
    states = {"waiting": waiting,
              "ready": ready,
              "running": running,
              "finished": finished}

    # Start the machine!
    cycle_machine(states, "waiting")
