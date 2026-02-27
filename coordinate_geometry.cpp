#include <iostream>
#include <cmath>

int main() {
    double x1, y1, x2, y2;

    std::cout << "1. Noktanin koordinatlarini girin (x1 y1): ";
    std::cin >> x1 >> y1;

    std::cout << "2. Noktanin koordinatlarini girin (x2 y2): ";
    std::cin >> x2 >> y2;


    double mesafe = std::sqrt(std::pow(x2 - x1, 2) + std::pow(y2 - y1, 2));

    std::cout << "\nNoktalar: (" << x1 << ", " << y1 << ") ve (" << x2 << ", " << y2 << ")" << std::endl;


    std::cout << "Aradaki Mesafe: " << mesafe << std::endl;

    return 0;
}