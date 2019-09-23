//https://raytracing.github.io/books/RayTracingInOneWeekend.html

//Modify ex3 to include a sphere that a ray touches.
// A sphere has the form x^2 + y^2 + z^2 = R^2. (when centered at 0)
// A sphere of radius R centered at C is 'touched' by a ray going from A->B if there is a scalar t such that
// $ t^2 \cdot dot(B,B) + 2t \cdot dot(B,A-C) + dot(A-C,A-C) - R^2 = 0  $
// If the quadratic has two real solutions (for t), then the ray intersects the sphere, a single solution is a tangent, and complex solutions imply no intersection.


#include "ray.h" // which includes vec3.h

#include <iostream>


// Does a ray r, "hit" the sphere (center, radius)? returns Bool to indicate hit
bool hit_sphere(const vec3& center, float radius, const ray& r) {
    vec3 oc = r.origin() - center;
    float a = dot(r.direction(), r.direction());
    float b = 2.0 * dot(oc, r.direction());
    float c = dot(oc, oc) - radius*radius;
    float discriminant = b*b - 4*a*c;
    return (discriminant > 0); //so tangents are out
}


//Modify the pixel color() function from ex3 : returns vec3 (to represent RGB color)
vec3 color(const ray& r) {
    // modification for hitting a sphere
    if (hit_sphere(vec3(0,0,-1), 0.5, r))   
            //this is a sphere centered at x=0,y=0,  z = -1, i.e. at center of the screen and radius 0.5. Diameter is 1, compare with Y-range = 2.
    return vec3(1, 0, 0);   //color the sphere, i.e. hit points 'red'
    // that's it. Rest is still the same

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
