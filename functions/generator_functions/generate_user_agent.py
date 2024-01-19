from ..data.user_agents import user_agents
from .generate_enum import generate_enum

def generate_user_agent(seed, rows):
    return generate_enum(seed, rows, user_agents)