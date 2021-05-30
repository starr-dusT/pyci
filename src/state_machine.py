# imports
import yaml
import time
import waiting as wt

# Simple state machine where: Waiting -> Ready -> Running -> Finished -|-> Succeeded
#                                                                      |
#                                                                      |-> Failed
#


def waiting(config):
    # TODO
    print("current state: waiting")
    # Next state is ready
    return wt.eval_state(config)


def ready(config):
    # TODO
    print("current state: ready")
    # Next state is running
    return "running"


def running(config):
    # TODO
    print("current state: running")
    # Next state is finished
    return "finished"


def finished(config):
    # TODO
    print("current state: finished")
    # Next state is waiting
    return "waiting"


def cycle_machine(config, states, initial_state):
    next_state = None
    current_state = initial_state

    while 1:
        next_state = states[current_state](config)
        current_state = next_state
        time.sleep(1)


def start_machine(config_location):
    print("starting machine...")
    # Define the machine's states
    states = {"waiting": waiting,
              "ready": ready,
              "running": running,
              "finished": finished}

    # Initalize the config file for passing
    stream = open(config_location, "r")
    config = yaml.safe_load(stream)

    # Start the machine!
    cycle_machine(config, states, "waiting")
