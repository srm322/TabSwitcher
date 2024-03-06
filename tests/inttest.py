import socket

def check_internet_connection():
    try:
        # Try to establish a connection to a well-known host (e.g., Google's DNS server)
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return True  # Internet connection is available
    except socket.error:
        return False  # No internet connection

# Example usage:
if check_internet_connection():
    print("Internet connection is available.")
else:
    print("No internet connection.")
    # Optionally, you can exit the program here
    exit()
