from pydantic import BaseModel, Field
import json
import json
from langchain_core.agents import AgentActionMessageLog, AgentFinish

class Inventory(BaseModel):
    axe: int
    fibers: int
    stone: int
    wood: int
    stick: int

class PlayerInfo(BaseModel):
    health: str
    hunger: str
    thirst: str
    energy: str

class ActionRequest(BaseModel):
    action: str
    status: str
    message: str
    inventory: Inventory
    player_info: PlayerInfo

from typing import List
from pydantic import BaseModel, Field

class NextAction(BaseModel):
    # Define the input data for the NextAction function
    action: str 
    observation: str
    
