using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class ChangeScene : MonoBehaviour
{
    public string Escena;
    // Start is called before the first frame update
    public void ChangeSceneFun()
    {
        Debug.Log("Movi�ndose a " + Escena);
        SceneManager.LoadScene(Escena);
    }
    
}
