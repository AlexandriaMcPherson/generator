from ..data.ip_addresses import ip_addresses
from .generate_enum import generate_enum

def generate_ip_address(seed, rows):
    return generate_enum(seed, rows, ip_addresses)