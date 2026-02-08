import agent0_sdk
import inspect

print("--- agent0_sdk members ---")
for name, obj in inspect.getmembers(agent0_sdk):
    if not name.startswith('_'):
        print(f"{name}: {type(obj)}")

if hasattr(agent0_sdk, 'core'):
    print("\n--- agent0_sdk.core members ---")
    for name, obj in inspect.getmembers(agent0_sdk.core):
        if not name.startswith('_'):
            print(f"{name}: {type(obj)}")

if hasattr(agent0_sdk, 'core') and hasattr(agent0_sdk.core, 'sdk'):
    print("\n--- agent0_sdk.core.sdk.Agent0SDK members ---")
    if hasattr(agent0_sdk.core.sdk, 'Agent0SDK'):
        for name, func in inspect.getmembers(agent0_sdk.core.sdk.Agent0SDK, predicate=inspect.isfunction):
            print(f"Method: {name}{inspect.signature(func)}")
        for name, func in inspect.getmembers(agent0_sdk.core.sdk.Agent0SDK, predicate=inspect.ismethod):
            print(f"Method (inst): {name}")
