//https://raytracing.github.io/books/RayTracingInOneWeekend.html

// the core of a ray tracer is to send rays through pixels and compute what color is seen in the direction of those rays.
// start with camera at (0,0,0). Y goes up, X goes right. Image screen is pushed back 1 unit (100 pixels) along Z axis from camera.
// the ray direction is intentionally not a unit vector.
// the ray goes to the 'center' of the pixel (this will be changed in more advanced versions, anti-aliasing) 


#include "ray.h" // which includes vec3.h

#include <iostream>

//create color values as blend of white and blue dependong on y-value
vec3 color(const ray& r) {
    vec3 white = vec3(1.0,1.0,1.0);
    vec3 blue = vec3(0.5, 0.7, 1.0); 
    vec3 unit_direction = unit_vector(r.direction()); //given ray, compute unit direction
    float t = 0.5*(unit_direction.y() + 1.0);  //t in (0.1) cos y in (-1,1) in example
    return (1.0 - t)*white + t*blue; //blend the colors, linear interpolation
}


int main() {
    //dimensions (# pixels along x and y)
    int nx = 200; //x in -2,2
    int ny = 100; // y in -1,1
    
    //a .ppm file starts with P3, then the dimensions (single line), and the max color e.g. 255 (separate line)
    std::cout << "P3\n" << nx << " " << ny << "\n255\n";
    
    vec3 lower_left_corner(-2.0, -1.0, -1.0); //of screen
    vec3 horizontal(4.0, 0.0, 0.0); //dim x in (-2,2)
    vec3 vertical(0.0, 2.0, 0.0); //dim Y in (-1,1)
    vec3 origin(0.0, 0.0, 0.0); //camera
    
    //then the pixel values 
    for (int j = ny-1; j >= 0; j--) {
        for (int i = 0; i < nx; i++) {
            
            float u = float(i) / float(nx);
            float v = float(j) / float(ny);
            
            //ray from origin to center of pixel [i,j]
            ray r(origin, lower_left_corner + u*horizontal + v*vertical);
            vec3 col = color(r);
            

            int ir = int(255.99*col[0]);
            int ig = int(255.99*col[1]);
            int ib = int(255.99*col[2]);
        
            std::cout << ir << " " << ig << " " << ib << "\n";
        }
    }
}
