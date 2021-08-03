using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MainLogic : MonoBehaviour
{
    [SerializeField] Ship shipPrefab;

    private Ship ship;
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        //spawn ship on left click
        if (Input.GetMouseButtonDown(0) && ship == null)
        {
            ship = Instantiate(shipPrefab);
            
        }
    }
}
