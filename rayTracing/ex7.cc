//https://raytracing.github.io/books/RayTracingInOneWeekend.html

// Antialiasing: Smooth out edges by randomly sampling pixel colors.
// * "random.h" => generate prng  
// * "camera.h" => Shirley also introduces a camera class to generalize that location. 

#include "vec3.h"
#include "sphere.h"
#include "hittable.h"
#include "hittable_list.h"
#include "random.h"
#include "camera.h"

#include <iostream>
#include <cfloat>
//#include "float.h"

//modified from before to take additional input
vec3 color(const ray& r,
            hittable *world     // NEW
        ) {
    hit_record rec;

    if (world->hit(r, 0.0, MAXFLOAT, rec)) {
        return 0.5 * vec3(rec.normal.x() + 1, rec.normal.y() + 1, rec.normal.z() + 1);
    } 
    else{
        //mostlty same as before for background
        vec3 white = vec3(1.0,1.0,1.0);
        vec3 blue = vec3(0.5, 0.7, 1.0); 
        vec3 unit_direction = unit_vector(r.direction()); //given ray, compute unit direction
        
        float t = 0.5*(unit_direction.y() + 1.0);  //t in (0.1) cos y in (-1,1) in example
        return (1.0 - t)*white + t*blue; //blend the colors, linear interpolation
    }   
}


int main() {
    //dimensions (# pixels along x and y)
    int nx = 200; //x in -2,2
    int ny = 100; // y in -1,1
    
    // NEW
    int ns = 100; // for random sampling of pixel (anti-aliasing)

    //a .ppm file starts with P3, then the dimensions (single line), and the max color e.g. 255 (separate line)
    std::cout << "P3\n" << nx << " " << ny << "\n255\n";
    
    camera cam; // NEW (had fixed origin previously)
    
    hittable *list[2]; // pointer to array (of size 2) of hittable objects 
    list[0] = new sphere(vec3(0,0,-1), 0.5);
    list[1] = new sphere(vec3(0,-100.5,-1), 100); //world surface? LARGE radius, slight 0.5 center offset from radius

    hittable *world = new hittable_list(list, 2);

    //then the pixel values 
    for (int j = ny-1; j >= 0; j--) {
        for (int i = 0; i < nx; i++) {
            vec3 col(0.0, 0.0, 0.0);  // NEW
            //NEW: random sampling of colors    
            for (int s = 0; s < ns; s++){
                float u = float(i + random_double()) / float(nx);
                float v = float(j + random_double()) / float(ny); 

                ray r = cam.get_ray(u, v);
                col += color(r, world);    
            }
            //take the average
            col /= float(ns); 

            // same as before
            int ir = int(255.99*col[0]);
            int ig = int(255.99*col[1]);
            int ib = int(255.99*col[2]);
        
            std::cout << ir << " " << ig << " " << ib << "\n";
        }
    }
}
