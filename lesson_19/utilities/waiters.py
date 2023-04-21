import time


def wait_until(predicate: callable, timeout: int = 100, frequency=0.1):
    start = time.time()
    while True:
        try:
            result = predicate()
            if result:
                return result
        except:
            time.sleep(frequency)
        if time.time() - start > timeout:
            break
    raise TimeoutError("Object is not found")
