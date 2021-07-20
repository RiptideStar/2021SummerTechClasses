using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Manifold : MonoBehaviour
{
    float halfWidth = 10.5f;
    float halfHeight = 6;
    void Update()
    {
        if (transform.position.x > halfWidth)
            transform.position = new Vector3(-halfWidth, transform.position.y, transform.position.z);
        if (transform.position.x < -halfWidth)    
            transform.position = new Vector3(halfWidth, transform.position.y, transform.position.z);
        if (transform.position.y < -halfHeight)    
            transform.position = new Vector3(transform.position.x, halfHeight, transform.position.z);
        if (transform.position.y > halfHeight)    
            transform.position = new Vector3(transform.position.x, -halfHeight, transform.position.z);        
    }
}
