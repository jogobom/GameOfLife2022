def should_live(is_alive, live_neighbours):
    if live_neighbours == 0 or live_neighbours > 3:
        return False
    else:
        return True
