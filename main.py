import pygame

from text_class import Text
from player_class import Player
from screen_class import Screen

pygame.init() # rozpocznij program

def main():

    clock = pygame.time.Clock() # zegar do klatkowania

    ekran = Screen()  # tworzenie okienka
    ekran.set_background()  # ustawianie obrazku jako tlo

    gracz = Player(ekran.window_width, ekran.window_height)  # tworzenie obiektu gracz

    tekst = Text(ekran.window_width, ekran.window_height, ekran.score, ekran.life_points)
    #tekst.initial_subtitles(ekran.window_width, ekran.window_height, ekran.score)

    while ekran.menu_running:
        ekran.drawing_background()  # rysowanie obrazu jako tlo
        ekran.show_menu(tekst) # wyswietlenie menu
        ekran.menu_key_control()  # kontrola klawiatury
        pygame.display.update() # aktualizacja zmian pygame

    while ekran.running:

        # klatkowanie
        clock.tick(ekran.FPS)

        # generowanie obiektow
        ekran.generate_tie_fighters()

        # kontrola klawiszy
        ekran.running = gracz.key_control(ekran)

        # rysowanie na ekranie
        ekran.drawing_background()
        gracz.draw_player(ekran)
        ekran.draw_tie_fighters()

        # przemieszczanie sie
        gracz.move_player()
        ekran.move_tie_fighters()

        # pociski
        ekran.draw_bullets()

        # ograniczenia ruchu
        gracz.move_limitation(ekran.window_width, ekran.window_height)
        ekran.move_limit_tie_fighters()

        # kolizja
        ekran.is_collision()

        # napisy
        ekran.screen.blit(tekst.text_04, tekst.textRect_04)
        ekran.screen.blit(tekst.text_05, tekst.textRect_05)
        tekst.scoreAndLifePoints(ekran.score, ekran.life_points)

        # warunki przegranej
        ekran.haveILost()

        # makes any new updates on the screen visible
        pygame.display.update()

    while ekran.closing_menu:
        ekran.closing_menu = ekran.menu_key_control()  # kontrola klawiatury

        pygame.display.update()

if __name__ == '__main__':
    main()