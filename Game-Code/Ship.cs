using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Ship : MonoBehaviour
{
    float movementSpeed = 5;
    float rotationSpeed = 210;
    const float dragAmount = 0.997f;

    Vector3 driftVector = new Vector3(1, 0, 0);

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        transform.position += driftVector * Time.deltaTime;
        driftVector *= dragAmount;

        //Rotate ccw upon D
        if (Input.GetKey(KeyCode.D))
        {
            transform.Rotate(0, 0, -rotationSpeed * Time.deltaTime);
        }
        //Rotate cc upon A
        if (Input.GetKey(KeyCode.A))
        {
            transform.Rotate(0, 0, rotationSpeed * Time.deltaTime);
        }
        if (Input.GetKey(KeyCode.W))
        {
            thrust();
        }
    }

    //Thrust Function: it makes the ship vector change to go up :)
    void thrust()
    {
        driftVector += transform.up * movementSpeed * Time.deltaTime;
    }
}