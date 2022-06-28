def should_live(live_neighbours):
    if live_neighbours == 0 or live_neighbours > 3:
        return False
    else:
        return True
