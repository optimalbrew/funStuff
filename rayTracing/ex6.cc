//https://raytracing.github.io/books/RayTracingInOneWeekend.html

// Adding multiple surfaces.
// changes from previous examples with one sphere
// * Instead of a list or array of "spheres", Shirley suggests a more general approach of creating an "abstract class"
// * hittable.h => The class definition "hittable" with a member function "hit()" (surface objects that a ray can hit)
// * sphere.h => The abstract class (in hittable.h), is used to derive the class 'sphere' in `sphere.h` for spherical surfaces.
// * hittablelist.h => list of surface objects that are hit by rays

#include "vec3.h"
#include "sphere.h"
#include "hittable.h"
#include "hittable_list.h"

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
    
    //a .ppm file starts with P3, then the dimensions (single line), and the max color e.g. 255 (separate line)
    std::cout << "P3\n" << nx << " " << ny << "\n255\n";
    
    vec3 lower_left_corner(-2.0, -1.0, -1.0); //of screen
    vec3 horizontal(4.0, 0.0, 0.0); //dim x in (-2,2)
    vec3 vertical(0.0, 2.0, 0.0); //dim Y in (-1,1)
    vec3 origin(0.0, 0.0, 0.0); //camera
    
    // NEW: the list of hittable surfaces
    hittable *list[2]; // pointer to array (of size 2) of hittable objects 
    list[0] = new sphere(vec3(0,0,-1), 0.5);
    list[1] = new sphere(vec3(0,-100.5,-1), 100); //world surface? LARGE radius, slight 0.5 center offset from radius

    hittable *world = new hittable_list(list, 2);

    //then the pixel values 
    for (int j = ny-1; j >= 0; j--) {
        for (int i = 0; i < nx; i++) {
            
            float u = float(i) / float(nx);
            float v = float(j) / float(ny);
            
            //ray from origin to center of pixel [i,j]
            ray r(origin, lower_left_corner + u*horizontal + v*vertical);
            
            //NEW: 
            //vec3 p = r.point_at_parameter(2.0); //unused?
            vec3 col = color(r, world);

            // same as before
            int ir = int(255.99*col[0]);
            int ig = int(255.99*col[1]);
            int ib = int(255.99*col[2]);
        
            std::cout << ir << " " << ig << " " << ib << "\n";
        }
    }
}
