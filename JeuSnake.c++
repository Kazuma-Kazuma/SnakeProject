#include <SDL2/SDL.h>

if (SDL_Init(SDL_INIT_VIDEO | SDL_INIT_TIMER) != 0) {
    std::cerr << "Erreur lors de l'initialisation de SDL : " << SDL_GetError() << std::endl;
    return 1;
}

SDL_Window* window = SDL_CreateWindow("Ma fenêtre", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 640, 480, SDL_WINDOW_SHOWN);
if (!window) {
    std::cerr << "Erreur lors de la création de la fenêtre : " << SDL_GetError() << std::endl;
    SDL_Quit();
    return 1;
}

SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);
if (!renderer) {
    std::cerr << "Erreur lors de la création du rendu : " << SDL_GetError() << std::endl;
    SDL_DestroyWindow(window);
    SDL_Quit();
    return 1;
}

// Effacer le rendu avec une couleur de fond blanche
SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
SDL_RenderClear(renderer);

// Dessiner une ligne rouge
SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255);
SDL_RenderDrawLine(renderer, 0, 0, 640, 480);

// Mettre à jour l'affichage
SDL_RenderPresent
