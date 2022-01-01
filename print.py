from transitions import Machine
from transitions.extensions import GraphMachine
from flask import Flask, jsonify, request, abort, send_file
#try:
import pygraphviz as pgv
#except ImportError:
#    raise
#import requests
machine = GraphMachine(
    states=["user", "state1", "state2","state3","state1_1"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "state1",
            "conditions": "is_going_to_state1",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "state2",
            "conditions": "is_going_to_state2",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "state3",
            "conditions": "is_going_to_state3",
        },
        {
            "trigger": "advance",
            "source": "state1",
            "dest": "state1_1",
            "conditions": "is_going_to_state1_1_light_roast",
        },
        {"trigger": "go_back", "source": ["state1","state2", "state3"], "dest": "user"},
        {"trigger": "go_back", "source": "state1_1", "dest": "state1"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)
machine.get_graph().draw("finite_state_machine.png", prog="dot", format="png")