using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Pause : MonoBehaviour
{
    public GameObject canvasPause;
    public bool boolean;
    
    public void PauseFun()
    {
        canvasPause.SetActive(boolean);
    }
}
