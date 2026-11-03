# future

from concurrent.futures import ThreadPoolExecutor
import time

def check_service(service_name):
    print(f"Checking {service_name}...")
    time.sleep(2)  # Simulate network waiting
    return f"{service_name}: healthy"


with ThreadPoolExecutor(max_workers=3) as executor:
    future = executor.submit(check_service, "Customer API") # start the thread

    print("The job has been submitted")
    print("Is it finished?", future.done()) # Check the status
    # True 
    # if the job has finished
    # with an exception
    # by cancellation

    result = future.result() # Retrieve the result / wait / join

    print("Result:", result)

print("All checks completed")