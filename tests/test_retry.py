
def retry_action(action_func, max_retries=3, delay=2):
    """
    Helper function to retry a specific Selenium action.
    """
    for attempt in range(max_retries):
        try:
            action_func()
            print(f"Action succeeded on attempt {attempt + 1}")
            return True
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Action failed on attempt {attempt + 1}. Retrying in {delay} seconds...")
            if attempt < max_retries - 1:
                time.sleep(delay)
            else:
                print(f"Action failed after {max_retries} attempts.")
                raise e # Re-raise the last exception if all retries fail
    return False
