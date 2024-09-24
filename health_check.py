import psutil
import shutil
import subprocess
import alarmEmails


def check_cpu_usage(period):
    if psutil.cpu_percent(period) > 80:
        return 1
    else:
        return 0

def check_memory_available():
    # Report an error if available memory is less than 100MB.
    if round(psutil.virtual_memory().available / 1000000, ndigits=2) < 100:
        return 1
    else:
        return 0

def check_disk_available():
    # Report an error if available disk space is lower than 20%.
    total_disk = shutil.disk_usage("/").total
    free_disk = shtuil.disk_usage("/").free
    if round(free_disk / total_disk * 100, ndigits=2) < 20:
        return 1
    else:
        return 0

def check_localhost_resolve():
    # if the hostname "localhost" cannot be resolved to "127.0.0.1.
    response = subprocess.run(['ping', '-c 1', 'localhost'], capture_output=True)

    if response.returncode != 0:
        return 1
    else:
        return 0

def send_email(subject):
    sender = "automation@example.com"
    receiver = "student@example.com"
    subject = subject
    body = "Please check your system and resolve the issue as soon as possible."

    message = alarmEmails.generate(sender, receiver, subject, body)
    alarmEmails.send(message)


if __name__ == "__main__":
    # 60 seconds.
    period = 60

    while True:
        # Check CPU usage.
        cpu_alarm = check_cpu_usage(period)
        # Check for available memory.
        memory_alarm = check_memory_available()
        # Check for available disk space.
        disk_alarm = check_disk_available()
        # Check localhost resolved to 127.0.0.1.
        resolve_alarm = check_localhost_resolve()

        if cpu_alarm == 1:
            # Send alarm for CPU subject.
            send_email("Error - CPU usage is over 80%")
        if memory_alarm == 1:
            # Send alarm for memory subject.
            send_email("Error - Available memory is less than 100MB")
        if disk_alarm == 1:
            # Send alarm for disk space subject.
            send_email("Error - Available disk space is less than 20%")
        if resolve_alarm == 1:
            # Send alarm for Localhost resolve to 127.0.0.1.
            send_email("Error - localhost cannot be resolved to 127.0.0.1")
