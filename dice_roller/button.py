import pygame

class Button:
    def __init__(self, text, x, y, width, height, callback):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.callback = callback
        self.hovered = False

    def draw(self, surface, font, color, hover_color, border_color, selected=False, selected_color=(0, 255, 0)):
        if selected:
            btn_color = selected_color
        else:
            btn_color = hover_color if self.hovered else color

        pygame.draw.rect(surface, btn_color, self.rect)
        pygame.draw.rect(surface, border_color, self.rect, 2)
        text_surface = font.render(self.text, True, border_color)
        surface.blit(
            text_surface,
            (
                self.rect.x + (self.rect.width - text_surface.get_width()) // 2,
                self.rect.y + (self.rect.height - text_surface.get_height()) // 2
            )
        )

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()