//https://raytracing.github.io/books/RayTracingInOneWeekend.html

//Simlar to ex1, R is linear in X, G in Y, and Blue is a constant. But implemented using the created vector lib.

#include "vec3.h"

#include <iostream>


int main() {
    //dimensions (# pixels along x and y)
    int nx = 200;
    int ny = 100;
    
    //a .ppm file starts with P3, then the dimensions (single line), and the max color e.g. 255 (separate line)
    std::cout << "P3\n" << nx << " " << ny << "\n255\n";
    //then the pixel values 
    for (int j = ny-1; j >= 0; j--) {
        for (int i = 0; i < nx; i++) {
            //create a vector instance for each pixel
            vec3 col(float(i) / float(nx), float(j) / float(ny), 0.2);
            int ir = int(255.99*col[0]);
            int ig = int(255.99*col[1]);
            int ib = int(255.99*col[2]);
        
            std::cout << ir << " " << ig << " " << ib << "\n";
        }
    }
}
