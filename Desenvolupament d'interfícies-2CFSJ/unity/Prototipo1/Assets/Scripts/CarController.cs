using UnityEngine;

public class CarController : MonoBehaviour
{

    public float speed = 5.0f;
    
    void Start()
    {
        
    }

    void Update()
    {
        transform.Translate(Vector3.forward * speed * Time.deltaTime);
    }
}
