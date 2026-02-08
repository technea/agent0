import agent0_sdk
from agent0_sdk import SDK
import inspect

print("--- agent0_sdk.SDK Methods ---")
methods = inspect.getmembers(SDK, predicate=inspect.isfunction)
for name, func in methods:
    print(f"Method: {name}{inspect.signature(func)}")

print("\n--- agent0_sdk.SDK Init ---")
print(inspect.signature(SDK.__init__))

# Find where Agent is defined
from agent0_sdk.core.models import Agent
print("\n--- agent0_sdk.core.models.Agent ---")
print(inspect.signature(Agent.__init__))
for field in Agent.__fields__:
    print(f"Field: {field}")
