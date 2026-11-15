
def lru(pages, capacity):
    frames = []
    page_faults = 0
    page_hits = 0
    history = []

    for page in pages:

        if page in frames:
            page_hits += 1
            status = "Hit"

            # Move recently used page to the end
            frames.remove(page)
            frames.append(page)

        else:
            page_faults += 1
            status = "Fault"

            if len(frames) < capacity:
                frames.append(page)
            else:
                # Remove the least recently used page
                frames.pop(0)
                frames.append(page)

        history.append({
            "page": page,
            "frames": frames.copy(),
            "status": status
        })

    return history, page_hits, page_faults
