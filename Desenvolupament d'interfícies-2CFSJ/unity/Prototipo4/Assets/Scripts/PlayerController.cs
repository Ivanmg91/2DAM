using System;
using System.Collections;
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    private Rigidbody playerRb;
    public float speed = 5.0f;
    private GameObject focalPoint;
    
    public bool hasPowerup;
    private float powerUpStrength = 15.0f;

    public GameObject powerupIndicator;
    
    public PowerUpType currentPowerUp = PowerUpType.None;
    public GameObject rocketPrefab;
    private GameObject tmpRocket;
    private Coroutine powerupCountdown;
    
    public float hangTime;
    public float smashSpeed;
    public float explosionForce;
    public float explosionRadius;
    bool smashing = false;
    float floorY;
    
    void Start()
    {
        playerRb = GetComponent<Rigidbody>();
        focalPoint = GameObject.Find("Focal Point");
    }

    void Update()
    {
        float forwardInput = Input.GetAxis("Vertical");
        playerRb.AddForce(focalPoint.transform.forward * forwardInput * speed);
        powerupIndicator.transform.position = transform.position + new Vector3(0, -0.5f, 0);

        if (currentPowerUp == PowerUpType.Rockets && Input.GetKeyDown(KeyCode.F))
        {
            LaunchRockets();
        }

        if (currentPowerUp == PowerUpType.Smash && Input.GetKeyDown(KeyCode.Space) && !smashing)
        {
            Debug.Log("Smash powerup activated");
            smashing = true;
            StartCoroutine(Smash());
        }
    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Powerup"))
        {
            hasPowerup = true;
            currentPowerUp = other.gameObject.GetComponent<PowerUp>().powerUpType;
            powerupIndicator.gameObject.SetActive(true);
            Destroy(other.gameObject);
            if(powerupCountdown != null)
            {
                StopCoroutine(powerupCountdown);
            }
            powerupCountdown = StartCoroutine(PowerupCountdownRoutine());
        }
    }
    
    IEnumerator PowerupCountdownRoutine()
    {
        yield return new WaitForSeconds(7);
        hasPowerup = false;
        currentPowerUp = PowerUpType.None;
        powerupIndicator.gameObject.SetActive(false);
    }
    
    IEnumerator Smash()
    {
        Debug.Log("Smash coroutine started");
        var enemies = FindObjectsByType<Enemy>(FindObjectsSortMode.None);
        floorY = transform.position.y;
        float jumpTime = Time.time + hangTime;

        // Player jumps up
        while (Time.time < jumpTime)
        {
            playerRb.linearVelocity = new Vector3(playerRb.linearVelocity.x, smashSpeed, playerRb.linearVelocity.z);
            Debug.Log("Jumping up: " + playerRb.linearVelocity);
            yield return null;
        }

        // Player falls down
        while (transform.position.y > floorY)
        {
            playerRb.linearVelocity = new Vector3(playerRb.linearVelocity.x, -smashSpeed * 2, playerRb.linearVelocity.z);
            Debug.Log("Falling down: " + playerRb.linearVelocity);
            yield return null;
        }

        // Apply explosion force to enemies
        for (int i = 0; i < enemies.Length; i++)
        {
            if (enemies[i] != null)
            {
                enemies[i].GetComponent<Rigidbody>().AddExplosionForce(explosionForce, transform.position, explosionRadius, 0.0f, ForceMode.Impulse);
                Debug.Log("Explosion force applied to enemy: " + enemies[i].name);
            }
        }
        smashing = false;
        Debug.Log("Smash coroutine ended");
    }

    private void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.CompareTag("Enemy") && currentPowerUp == PowerUpType.Pushback)
        {
            Rigidbody enemyRigidbody = collision.gameObject.GetComponent<Rigidbody>();
            Vector3 awayFromPlayer = (collision.gameObject.transform.position - transform.position);
            enemyRigidbody.AddForce(awayFromPlayer * powerUpStrength, ForceMode.Impulse);
            
            Debug.Log("Player collided with: " + collision.gameObject.name + " with powerup set to " + currentPowerUp.ToString());
        }
    }
    
    void LaunchRockets()
    {
        foreach(var enemy in FindObjectsByType<Enemy>(FindObjectsSortMode.None))
        {
            tmpRocket = Instantiate(rocketPrefab, transform.position + Vector3.up, Quaternion.identity);
            tmpRocket.GetComponent<RocketBehaviour>().Fire(enemy.transform);
        }
    }
}