// sphere.h is based on the abstract class of `hittable` surfaces

#ifndef SPHEREH
#define SPHEREH

#include "hittable.h"

// class sphere derived from class hittable
class sphere: public hittable {
    public:
        sphere() {}
        sphere(vec3 cen, float r) : center(cen), radius(r) {}; // equivalently {center = c; radius = r;};

        virtual bool hit(const ray& r,
            float t_min,
            float t_max,
            hit_record& rec) const;
        vec3 center;
        float radius;
}; 


// implement hit(): this is just an extension of hit_sphere used in previous examples (ex4 and 5)
bool sphere::hit(const ray& r, float t_min, float t_max, hit_record& rec) const {
    // copied from hit_sphere() in previous ex4,5  
    vec3 oc = r.origin() - center;
    float a = dot(r.direction(), r.direction());
    float b = 2.0 * dot(oc, r.direction());
    float c = dot(oc, oc) - radius*radius;
    float discriminant = b*b - 4*a*c;

    if (discriminant > 0){
        // check the closest solution to the quadratic first
        float temp = (-b - sqrt(discriminant) )/(2.0 * a); // different from Shirley's he cancels off some 2's (above also). Mine is unchanged
        if (temp < t_max && temp > t_min ){
            rec.t = temp;
            rec.p = r.point_at_parameter(rec.t);
            rec.normal = (rec.p - center)/ radius; //why divide by radius? Ah, to convert it to unit normal
            return true;
        }
        // check the other solution to the quadratic
        temp = (-b + sqrt(discriminant) )/(2.0 * a); 
        if (temp < t_max && temp > t_min ){
            rec.t = temp;
            rec.p = r.point_at_parameter(rec.t);
            rec.normal = (rec.p - center)/ radius;
            return true;
        }
    }
    // if neither solution is within the bounds, then there is no record of a hit
    return false;

}

#endif