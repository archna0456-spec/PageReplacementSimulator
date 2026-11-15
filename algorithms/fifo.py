def fifo(pages, capacity):
    frames = []
    page_faults = 0
    page_hits = 0
    history = []

    for page in pages:

        if page in frames:
            page_hits += 1
            status = "Hit"

        else:
            page_faults += 1
            status = "Fault"

            if len(frames) < capacity:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)

        history.append({
            "page": page,
            "frames": frames.copy(),
            "status": status
        })

    return history, page_hits, page_faults