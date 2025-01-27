using UnityEngine;

public class PlayerController : MonoBehaviour
{

    // Variables
    private float speed = 5.0f;
    private float turnSpeed = 45.0f;
    private float horizontalInput;
    private float forwardInput;
    
    public string inputID;
    public KeyCode switchKey;
    
    // Camaras
    public Camera mainCamera;
    public Camera firstPersonCamera;
    public void ShowMainCameraView()
    {
        mainCamera.enabled = true;
        firstPersonCamera.enabled = false;
    }
    
    public void ShowFirstPersonCameraView()
    {
        mainCamera.enabled = false;
        firstPersonCamera.enabled = true;
    }
    
    // Start is called once before the first execution of Update after the MonoBehaviour is created
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        horizontalInput = Input.GetAxis("Horizontal" + inputID);
        forwardInput = Input.GetAxis("Vertical" + inputID);
        
        // Move vehicle forward
        transform.Translate(Vector3.forward * Time.deltaTime * speed * forwardInput);
        // Rotates the car based on horizontal input
        transform.Rotate(Vector3.up, turnSpeed * horizontalInput * Time.deltaTime);
        
        // Q ACELERE
        if (forwardInput != 0) {
            speed += 0.2f;
        } else {
            speed = 5.0f;
        }
        
        // Cambiar de camara al pulsar el espacio
        if (Input.GetKeyDown(switchKey)) {
            if (mainCamera.enabled) {
                ShowFirstPersonCameraView();
            } else {
                ShowMainCameraView();
            }
        }
    }
}
