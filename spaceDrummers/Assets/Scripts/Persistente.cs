using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Persistente : MonoBehaviour
{
    public User u;
    void Awake()
    {
        u = new User();
        DontDestroyOnLoad(this.gameObject);
    }
}
