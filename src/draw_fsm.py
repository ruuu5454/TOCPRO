from fsm import TocMachine

machine = TocMachine(
    states=[
        "user",
        "check",
        "dateInfo",
    ],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "check",
            "conditions": "is_going_to_check",
        },
        {
            "trigger": "advance",
            "source": "check",
            "dest": "dateInfo",
            "conditions": "is_going_to_dateInfo",
        },
        {
            "trigger": "go_back",
            "source": [
                "dateInfo",
            ],
            "dest": "user"
        },
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

machine.get_graph().draw("fsm.png", prog="dot", format="png")
