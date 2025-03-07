using System;
using UnityEditor.Build.Content;
using UnityEngine;

public class DetectCollisions : MonoBehaviour
{

    private GameManager gameManager;
    void Start()
    {
        gameManager = GameObject.Find("GameManager").GetComponent<GameManager>();
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    private void OnTriggerEnter(Collider other)
    {
//Check if the other tag was the Player, if it was remove a life
        if (other.CompareTag("Player"))
        {
            gameManager.AddLives(-1);
            Destroy(gameObject);
        }
//Check if the other tag was an Animal, if so add points to the score
        else if (other.CompareTag("Animal"))
        {
            other.GetComponent<AnimalHunger>().FeedAnimal(1);
        }
    }
}
