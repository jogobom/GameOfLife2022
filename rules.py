def should_live(is_alive, live_neighbours):
    if (is_alive and live_neighbours == 2) or live_neighbours == 3:
        return True
    else:
        return False
