#ifndef HITTABLEH
#define HITTABLEH

#include "ray.h"

/*
It is common (in ray tracing) to restrict attention to surfaces that are within a certain distance (t_min, t_max) from the camera.
The lower bound is not necessarily positive! 
*/

struct hit_record {
    float t;    //
    vec3 p;     //this is a hit point
    vec3 normal;    //compute the normal at that hit point
};

// The class def
// Recall: A class is made abstract by declaring at least one of its functions as pure virtual function. 
// A pure virtual function is specified by placing "= 0" in its de
// The idea is to represent some common functionality (like interfaces), which will be implented in derived classes

class hittable {
    public:
        virtual bool hit(
            const ray& r,
            float t_min,
            float t_max,
            hit_record& rec
        ) const = 0;    //"pure" virtual function = 0, const => immutatable. But must be implemented in a derived class. e.g. sphere.h
};

#endif