// Run.cpp : Ce fichier contient la fonction 'main'. L'exécution du programme commence et se termine à cet endroit.
//

#include <iostream>
#include <vector>

// Définir la taille de votre carte (par exemple, 10x10)
const int largeurCarte = 16;
const int hauteurCarte = 16;

// Déclarer un tableau bidimensionnel pour représenter la carte
std::vector<std::vector<char>> carte(largeurCarte, std::vector<char>(hauteurCarte, '.'));

// Fonction pour afficher la carte
void afficherCarte() {
    for (int y = 0; y < hauteurCarte; y++) {
        for (int x = 0; x < largeurCarte; x++) {
            std::cout << carte[x][y] << ' ';
        }
        std::cout << std::endl;
    }
}
void initialiserCarteAvecMurs() {
    // Remplir la première ligne et la dernière ligne avec des murs
    for (int x = 0; x < largeurCarte; x++) {
        carte[x][0] = '#';               // Première ligne
        carte[x][hauteurCarte - 1] = '#'; // Dernière ligne
    }

    //murs centraux
    carte[2][2] = '#';
    carte[4][6] = '#';
    carte[8][4] = '#';

    // Remplir la première colonne et la dernière colonne avec des murs
    for (int y = 0; y < hauteurCarte; y++) {
        carte[0][y] = '#';               // Première colonne
        carte[largeurCarte - 1][y] = '#'; // Dernière colonne
    }
}
int main()
{
    initialiserCarteAvecMurs();
  



    // Afficher la carte
    afficherCarte();

    return 0;
}

// Mettre en place votre carte initiale ici
// Par exemple, vous pouvez placer des murs en utilisant '#'

// Exécuter le programme : Ctrl+F5 ou menu Déboguer > Exécuter sans débogage
// Déboguer le programme : F5 ou menu Déboguer > Démarrer le débogage

// Astuces pour bien démarrer : 
//   1. Utilisez la fenêtre Explorateur de solutions pour ajouter des fichiers et les gérer.
//   2. Utilisez la fenêtre Team Explorer pour vous connecter au contrôle de code source.
//   3. Utilisez la fenêtre Sortie pour voir la sortie de la génération et d'autres messages.
//   4. Utilisez la fenêtre Liste d'erreurs pour voir les erreurs.
//   5. Accédez à Projet > Ajouter un nouvel élément pour créer des fichiers de code, ou à Projet > Ajouter un élément existant pour ajouter des fichiers de code existants au projet.
//   6. Pour rouvrir ce projet plus tard, accédez à Fichier > Ouvrir > Projet et sélectionnez le fichier .sln.
