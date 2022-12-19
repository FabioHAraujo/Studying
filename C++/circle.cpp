#include <graphics.h>

int main() {
    // Initialize the graphics window
    int gd = DETECT, gm;
    initgraph(&gd, &gm, "");

    // Draw a circle at (100, 100) with radius 50
    circle(100, 100, 50);

    // Display the graphics
    getch();
    closegraph();

    return 0;
}
