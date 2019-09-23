//The ray class:
//just defining a ray as a combo of a starting vector (origin) + a scalar * direction vector
//the scalar parameter `t` is an argument to the function, which then returns the new point in the space

#ifndef RAYH
#define RAYH
#include "vec3.h"

class ray
{
    public:
        ray() {}
        ray(const vec3& a, const vec3& b) { A = a; B = b; }
        vec3 origin() const       { return A; }
        vec3 direction() const    { return B; }
        
        // `+` and `*` are defiend (overloaded) in vec3.h
        vec3 point_at_parameter(float t) const { return A + t*B; } 

        vec3 A;
        vec3 B;
};

#endif