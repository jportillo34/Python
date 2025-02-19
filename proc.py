import subprocess
import time
import sys

if __name__ == "__main__":
    print("Starting microservices...")

    # Start the microservices
    process_add = subprocess.Popen(["python3", "service_add.py"])
    process_min = subprocess.Popen(["python3", "service_min.py"])

    try:
        # Run the services for some time or until user interrupts
        print("Microservices are running...")
        while True:
            time.sleep(1)  # Keeps the program running
    except KeyboardInterrupt:
        print("\nTerminating microservices...")

    # Terminate the microservices gracefully
    process_add.terminate()
    process_min.terminate()

    # Wait for processes to finish
    process_add.wait()
    process_min.wait()

    print("Microservices stopped. Program ending.")

