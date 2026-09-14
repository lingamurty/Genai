#I dont want all fields to be Required

from langgraph.graph import StateGraph, START, END
from typing import TypedDict,  NotRequired
from dataclasses import dataclass
from pydantic import BaseModel, Field

class InterestState(TypedDict,total=False):
    """This represents the state
    """
    principal: float|int
    time: int|float
    rate: int|float
    simple_interest:  NotRequired[float]
    compund_interest:  NotRequired[float]

def simple_interest(state: InterestState) -> InterestState:
    state['simple_interest'] = (state['principal'] * state['rate'] * state['time']) / 100
    return state

def compound_interest(state: InterestState) -> InterestState:
    amount = state['principal'] * ((1 + (state['rate'] / 100)) ** state['time'])
    
    # Subtract principal to get just the interest
    state['compund_interest'] = amount - state['principal']
    return state

state_graph = StateGraph(InterestState)
state_graph.add_node("si", simple_interest)
state_graph.add_node("ci", compound_interest)

state_graph.add_edge(START, "si")
state_graph.add_edge("si", "ci")
state_graph.add_edge("ci", END)

graph = state_graph.compile()

def collect_input(name, description) -> str:
    value = input(f"Enter {name} < {description} >")
    return value

if __name__ == "__main__":
    principal = float(collect_input("principal", "total amount"))
    time = float(collect_input("time", "total time in years"))
    rate = float(collect_input("rate", "annual rate of intrest"))
    print(principal)
    print(time)
    print(rate)
    state = InterestState(principal=principal, time=time, rate=rate)
    print("state:=",state)
    result = graph.invoke(state)
    print(result)