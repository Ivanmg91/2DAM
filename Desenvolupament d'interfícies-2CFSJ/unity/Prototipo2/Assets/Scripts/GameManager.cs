using UnityEngine;

public class GameManager : MonoBehaviour
{

    private int score = 0;
    private int lives = 3;
    
    void Start()
    {
        
    }

    void Update()
    {
        
    }

    public void AddLives(int value)
    {
        lives += value;

        if (lives <= 0)
        {
            Debug.Log("Game Over");
            lives = 0;
        }

        Debug.Log("Lives = " + lives);
    }
    
    public void AddScore(int value)
    {
        score += value;
        Debug.Log("Score = " + score);
    }
}
