class pyGameHandler(object):
    def __init__(s, window_dimensions):
        pygame.init()
        s.display = pygame.display.set_mode(*window_dimensions)
        s.display.fill(COLOR_WHITE)

    def set_title(s, title):
        pygame.display.set_caption(title)
