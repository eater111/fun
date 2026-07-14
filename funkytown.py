import hashlib
import os
import sys

GREEN = "\033[92m"
RESET = "\033[0m"

def animated_hash(path, algo="sha256", chunk_size=65536):
    h = hashlib.new(algo)

    total_size = os.path.getsize(path)
    processed = 0

    previous = None

    with open(path, "rb") as f:
        while chunk := f.read(chunk_size):
            h.update(chunk)
            processed += len(chunk)

            current = h.hexdigest()

            if previous is None:
                display = current
            else:
                chars = []
                for old, new in zip(previous, current):
                    if old != new:
                        chars.append(f"{GREEN}{new}{RESET}")
                    else:
                        chars.append(new)
                display = "".join(chars)

            percent = processed / total_size * 100

            sys.stdout.write("\033[H\033[J")  # clear screen
            print(f"Algorithm: {algo}")
            print(f"Progress : {percent:6.2f}%")
            print()
            print(display)

            previous = current

    print("\nFinal hash:")
    print(h.hexdigest())

    return h.hexdigest()


if __name__ == "__main__":
    animated_hash("schema.sql")