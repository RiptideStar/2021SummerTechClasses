using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Rock : MonoBehaviour
{
    float movementSpeed = 5;
    float randomDirectionX;
    float randomDirectionY;
    float randomRotationSpeed;

    private MainLogic mainRef;

    public MainLogic MainRef
    {
        set { mainRef = value; }
    }

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
        transform.Rotate(0, 0, randomRotationSpeed * Time.deltaTime);
        transform.position += new Vector3(randomDirectionX * movementSpeed * Time.deltaTime, randomDirectionY * movementSpeed 
            * Time.deltaTime, 0);
    }

    void OnTriggerEnter(Collider other)
    {
        // Debug.Log("HIT!"); 
        if (other.gameObject.GetComponent<Bullet>() || other.gameObject.GetComponent<Ship>())
        {
            //destroy both this rock and the other gameobject (which is a ship or bullet)
            Destroy(other.gameObject);
            Explode();
        }
    }

    void Explode()
    {
        mainRef.updateScore(1);
        mainRef.rocks.Remove(this);
        Destroy(this.gameObject);
    }
}
