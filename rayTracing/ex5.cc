//https://raytracing.github.io/books/RayTracingInOneWeekend.html

// Ex4 introduced rays hitting spherical surface, but all hit points had the same shade/color.
// Use normal vectors for colors/shading
// A normal vector starts from sphere's center C and ends at the hit point P (where ray from camera meets surface).  
// P and C are vectors from origin (camera). Thus the normal vector N = P - C (cos C + N = P)
// Sometimes it is useful to obtain the unit normal, Then we can map x,y,z (of a unit vector) to some RGB in (0,1) scaling of 255.

#include "ray.h" // which includes vec3.h

#include <iostream>

// MOdification from ex4. Arguments do not change. 
// Modify hit_sphere from (earlier bool in ex4, whether ray hits) to float. This actually returns the scalar t, which solves the quadratic A+tB is on sphere surface. 
float hit_sphere(const vec3& center, float radius, const ray& r) {
    vec3 oc = r.origin() - center;
    float a = dot(r.direction(), r.direction());
    float b = 2.0 * dot(oc, r.direction());
    float c = dot(oc, oc) - radius*radius;
    float discriminant = b*b - 4*a*c;
    
    //changes from ex4 here
    if (discriminant < 0){  //no hit
        return -1.0;
    } 
    else {
        return (-b - sqrt(discriminant) )/(2.0 * a); //pick the closest hit point, i.e. not  ((-b + sqrt(D))/2a)
    }
}

//Mod from ex4: the previous example simply colored all points on the spherical surface the same color. 
// We change that now.
//Modify the pixel color() function from ex3 : returns vec3 (to represent RGB color)
vec3 color(const ray& r) {
    //use modified hit_sphere to grab the parameter
    float t = hit_sphere(vec3(0,0,-1), 0.5, r);
    if (t > 0) {
        vec3 N = unit_vector(r.point_at_parameter(t) - vec3(0,0,-1)); //N = P-C
        return 0.5*vec3(N.x()+1, N.y()+1, N.z()+1); //rgb as 0.5 + 1/2 of unit vector directional component. So each is in (0,1)  
    }    
   
    //mostlty same as ex4
    vec3 white = vec3(1.0,1.0,1.0);
    vec3 blue = vec3(0.5, 0.7, 1.0); 
    vec3 unit_direction = unit_vector(r.direction()); //given ray, compute unit direction
    
    //The only change here is we drop 'float' in front of t (already defined above)
    t = 0.5*(unit_direction.y() + 1.0);  //t in (0.1) cos y in (-1,1) in example
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
