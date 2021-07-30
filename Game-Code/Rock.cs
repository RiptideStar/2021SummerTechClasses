using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Rock : MonoBehaviour
{
    float movementSpeed = 5;
    float randomDirectionX;
    float randomDirectionY;
    float randomRotationSpeed;

    // Start is called before the first frame update
    void Start()
    {
        randomDirectionX = Random.Range(-1, 1);
        randomDirectionY = Random.Range(-1, 1);
        randomRotationSpeed = Random.Range(-360, 360);
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
