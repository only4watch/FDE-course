from concurrent.futures import ThreadPoolExecutor
import time

def check_service(service_name):
    print(f"Checking {service_name}...")
    time.sleep(2)  # Simulate network waiting
    return f"{service_name}: healthy"

services = [
    "Customer API",
    "Payment API",
    "Inventory API",
    "Weather API",
    "Notification API"
]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(check_service, services)

    for result in results:
        print(result)

print("All checks completed")