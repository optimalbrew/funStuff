//save output to .ppm file
//clang++ -Wall -std=c++11 ex1.cc -o ex1 && ./ex1 > ex1.ppm

#include <iostream>

int main() {
    //dimensions (# pixels along x and y)
    int nx = 200;
    int ny = 100; //NOT THE SAME: Square matrices can be hard to debug.
    
    //a .ppm file starts with P3, then the dimensions (single line), and the max color e.g. 255 (separate line)
    std::cout << "P3\n" << nx << " " << ny << "\n255\n";
    //then the pixel values 
    for (int j = ny-1; j >= 0; j--) {
        for (int i = 0; i < nx; i++) {
            //use type casting, and create linear scaling
            float r = float(i) / float(nx); //linear in X 
            float g = float(j) / float(ny); //linear in Y
            float b = 0.2;  //constant
            int ir = int(255.99*r);
            int ig = int(255.99*g);
            int ib = int(255.99*b);
            std::cout << ir << " " << ig << " " << ib << "\n";
        }
    }
}

