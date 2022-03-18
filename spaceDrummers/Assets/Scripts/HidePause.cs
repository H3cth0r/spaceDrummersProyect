using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class HidePause : MonoBehaviour
{
    public GameObject canvasPause;
    // Start is called before the first frame update
    void Start()
    {
        canvasPause.SetActive(false);
    }
}
