
def optimal(pages, capacity):
    frames = []
    page_faults = 0
    page_hits = 0
    history = []

    for i, page in enumerate(pages):

        if page in frames:
            page_hits += 1
            status = "Hit"

        else:
            page_faults += 1
            status = "Fault"

            if len(frames) < capacity:
                frames.append(page)

            else:
                future_pages = pages[i + 1:]
                farthest = -1
                page_to_replace = None

                for frame_page in frames:
                    if frame_page not in future_pages:
                        page_to_replace = frame_page
                        break

                    next_use = future_pages.index(frame_page)

                    if next_use > farthest:
                        farthest = next_use
                        page_to_replace = frame_page

                frames.remove(page_to_replace)
                frames.append(page)

        history.append({
            "page": page,
            "frames": frames.copy(),
            "status": status
        })

    return history, page_hits, page_faults
