

import time


def rows_after(after):
    time.sleep(3)
    rows = []
    i = after
    for _ in range(10):
        i = i + 1
        rows.append({"id": i, "thing": str(i**3)})
    return rows
