using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Bullet : MonoBehaviour
{
    float zoom_speed = 12;
    float max_distance = 12;
    float distanceTraveled = 0;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        transform.position += transform.up * zoom_speed * Time.deltaTime;

        // distance = speed * time
        distanceTraveled += zoom_speed * Time.deltaTime;

        if (distanceTraveled > max_distance)
        {
            Destroy(gameObject);
        }
    }
}
