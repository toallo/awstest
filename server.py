import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_startup_callback():
    """Send a callback notification to toallo.com when the server starts."""
    callback_url = "https://toallo.com/callback"
    try:
        logging.info(f"Sending startup callback to {callback_url}")
        
        # Try to use requests library first, fall back to urllib if not available
        try:
            import requests
            response = requests.get(callback_url)
            status_code = response.status_code
            if status_code == 200:
                logging.info(f"Callback successful: {status_code}")
            else:
                logging.warning(f"Callback returned non-200 status code: {status_code}")
        except ImportError:
            # Fall back to urllib if requests is not available
            import urllib.request
            import urllib.error
            try:
                with urllib.request.urlopen(callback_url) as response:
                    status_code = response.getcode()
                    if status_code == 200:
                        logging.info(f"Callback successful: {status_code}")
                    else:
                        logging.warning(f"Callback returned non-200 status code: {status_code}")
            except urllib.error.URLError as e:
                raise Exception(f"URLError: {str(e)}")
            except urllib.error.HTTPError as e:
                logging.warning(f"HTTPError: {e.code} - {e.reason}")
    except Exception as e:
        logging.error(f"Failed to send callback: {str(e)}")

# Send the startup callback
send_startup_callback()

# Continue with the original server code
print("hello")
