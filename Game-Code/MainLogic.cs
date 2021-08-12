using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class MainLogic : MonoBehaviour
{
    [SerializeField] Ship shipPrefab;
    [SerializeField] Rock rockPrefab;

    [SerializeField] Text scoreText;
    [SerializeField] Text livesText;
    int score; 
    const int STARTING_SCORE = 0;
    int lives;
    const int STARTING_LIVES = 3;

    public List<Rock> rocks = new List<Rock>();
    int rockCount = 4;
    int maxRocks = 8;
    int radiusOfRockSpawns = 5;

    private Ship ship;
    // Start is called before the first frame update
    void Start()
    {
        score = STARTING_SCORE;
        lives = STARTING_LIVES;
    }

    // Update is called once per frame
    void Update()
    {
        //spawn ship on left click
        if (Input.GetMouseButtonDown(0) && ship == null)
        {
            ship = Instantiate(shipPrefab);
            updateLives(-1);
        }
        if (rocks.Count == 0 && ship != null)
        {
            SpawnRocks(rockCount);
            
            if (rockCount < maxRocks)
                rockCount++;
        }
        if (lives <= 0 && ship == null)
        {
            newGame();
        }
    }

    void newGame()
    {
        // clear and destroy the rock list and rocks, lives = starting, score = starting, reset rockCount
        foreach (Rock rock in rocks)
        {
            Destroy(rock.gameObject);
        }
        rocks.Clear();
        lives = STARTING_LIVES;
        score = STARTING_SCORE;
        rockCount = 4;
    }

    void SpawnRocks(int amount)
    {
        for (int i = 0; i < amount; i++)
        {
            SpawnRockInCircle(ship.transform.position, radiusOfRockSpawns);
        }
    }

    void SpawnRockInCircle(Vector3 center, int radius)
    {
        float randomAngle = Random.Range(-360, 360);
        Vector3 rockPosition;
        rockPosition.x = center.x + radius * Mathf.Cos(randomAngle * Mathf.Deg2Rad);
        rockPosition.y = center.y + radius * Mathf.Sin(randomAngle * Mathf.Deg2Rad);
        rockPosition.z = center.z;

        Rock rock = Instantiate(rockPrefab);
        rock.transform.position = rockPosition;

        rock.MainRef = this;
        rocks.Add(rock);
    }

    public void updateScore(int deltaScore)
    {
        score += deltaScore;
        scoreText.text = "Score: " + score;

        // every 10 rocks/score we destroy, we gain an extra life
        if (score % 10 == 0 && score != 0)
        {
            updateLives(1);
        }
    }

    public void updateLives(int deltaLives)
    {
        lives += deltaLives;
        livesText.text = "Lives: " + lives;
    }
}
