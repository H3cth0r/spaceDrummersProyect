using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[System.Serializable]
public class User
{
    public int userId;
    public int id;
    public string title;
    public string body;

    public override string ToString()
    {
        string res = "userID: " + userId;
        res += " id: " + id;
        res += " title: " + title;
        res += " body: " + body;
        return res;
    }
}
