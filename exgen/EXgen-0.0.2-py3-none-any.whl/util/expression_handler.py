from typing import Any, Dict, List
import numpy as np
from math import *
from lcapy import Circuit

NetlistObject = object

def init_var(var_def: Dict[str, Any]) -> float:
    
    if var_def["dist"] == "uniform":
        val = np.random.rand()*(var_def["max"]-var_def["min"]) + var_def["min"]
    elif var_def["dist"] == "normal":
        val = np.random.randn()*(var_def["max"]-var_def["min"]) + var_def["min"]
    elif var_def["dist"] == "exact":
        val = var_def["val"]

    if "round" in var_def.keys() and var_def["round"]:
        val = np.round(val)
    
    return val

def init_var_vals(var_defs: Dict[str,Dict[str, int]]) -> Dict[str, float]:

    var_vals = {}
    for var in var_defs.keys():
        val = init_var(var_defs[var])
        var_vals[var] = val

    return var_vals

def get_unknonws_from_elements(elements_list: List[str]) -> List[str]:

    elements = [x for x in elements_list if x[0] not in ['W', 'X']]

    unknonws = []

    for element in elements:
        
        if element[0] == 'V':
            unknonws += [f"I{element}"]  
        elif element[0] == 'I':
            unknonws += [f"V{element}"]  
        else:
            unknonws += [f"I{element}", f"V{element}"]  
    
    return unknonws

def generate_equations(schematic: NetlistObject) -> Dict[str, str]: 

    equations = {}

    unknowns = get_unknonws_from_elements(schematic.elements.keys())

    for x in unknowns:
        unknown_type = x[0]
        element = x[1:]
        equations[x] = str(eval(f"schematic.{element}.{unknown_type}.expr['t']"))

    return equations

def evaluate_equations(equations: Dict[str, str], var_defs: Dict[str,Dict[str, int]]) -> Dict[str, float]:

    variables = init_var_vals(var_defs)

    # assign variables in working memory : 
    for y,x in variables.items():
        equation = f"{y} = {x}"
        eval(compile(equation, filename="equation", mode="exec"))

    # execute equations : 
    for y,x in equations.items():
        equation = f"{y} = {x}"
        eval(compile(equation, filename="equation", mode="exec"))
        variables[y] = eval(y)

    return variables

def solve(task: Dict[str, Any], draw: bool=False) -> Dict[str, float]:

    schematic = Circuit(task["netlist"])

    equations = generate_equations(schematic)
    solutions = evaluate_equations(equations=equations, var_defs=task["var_defs"])

    if draw:
        schematic.draw(task["schematic_path"], style="european")

    return solutions

