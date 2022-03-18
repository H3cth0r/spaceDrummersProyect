using System.Collections;
using System.Collections.Generic;
using UnityEditor;
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.Networking;
using TMPro;
using System.Security.Cryptography; //Para MD5
using System.Text;



public class Login : MonoBehaviour
{
    public TMP_InputField usr;
    public TMP_InputField pwd;
    public Persistente persist;
    public string escena;

    string HashMD5(string txt)
    {
        MD5 md5 = new MD5CryptoServiceProvider();
        string key = "ABCDE";
        byte[] bytes = Encoding.UTF8.GetBytes(txt + key);
        byte[] hash = md5.ComputeHash(bytes);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < hash.Length; i++)
            sb.Append(hash[i].ToString("X2"));

        return sb.ToString();
    }

    // Start is called before the first frame update
    IEnumerator Upload(string url)
    {
        //WWWForm form = new WWWForm();
        //form.AddField("bundle", "json");
        //using (UnityWebRequest www = UnityWebRequest.Post("https://victorportilla.github.io/login.json", form))
        using (UnityWebRequest www = UnityWebRequest.Get(url))
        {
            //var request = new UnityWebRequest(url, "POST");
            byte[] bodyRaw = System.Text.Encoding.UTF8.GetBytes(url);
            www.uploadHandler = (UploadHandler)new UploadHandlerRaw(bodyRaw);
            www.downloadHandler = (DownloadHandler)new DownloadHandlerBuffer();
            www.SetRequestHeader("Content-Type", "application/json");
            yield return www.SendWebRequest();
            if (www.isNetworkError || www.isHttpError)
            {
                Debug.Log(www.error);
            }
            else
            {
                Debug.Log("Form upload complete!");
                Debug.Log(www.downloadHandler.text);
                persist.u = JsonUtility.FromJson<User>(www.downloadHandler.text.Replace('\'', '\"'));
                Debug.Log(persist.u.ToString());
                SceneManager.LoadScene(escena);
            }
        }
    }
    public IEnumerator PostMethod(string json)
    {
        string URL = "https://victorportilla.github.io/login.json";
        string jsonData = json;
        string method = "";
        using (UnityWebRequest req = UnityWebRequest.Put(URL + method, jsonData))
        {
            req.method = UnityWebRequest.kHttpVerbPOST;
            req.SetRequestHeader("Content-Type", "application/json");
            req.SetRequestHeader("Accept", "application/json");
            yield return req.SendWebRequest();
            if (!req.isNetworkError && req.responseCode != 404)
            {
                Debug.Log("JSON sent to server!");
            }
            else
            {
                Debug.Log("JSON not sent to server");
            }
        }
    }
    // Start is called before the first frame update
    void Start()
    {
        //TextAsset productList = Resources.Load<TextAsset>("Text/AssetBundleInfo");
        //string json = EditorJsonUtility.ToJson(productList);
        //Debug.Log(productList.ToString());
        //string json = "Hello Server!";
        //StartCoroutine(Upload(json));
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void LoginButtonClicked()
    {
        persist.u.userId = 1;
        persist.u.id = 1;
        persist.u.body = usr.text;
        persist.u.title = HashMD5(pwd.text);
        Debug.Log(persist.u.ToString());

        string url = "https://victorportilla.github.io/login.json?userId=a" + persist.u.userId;
        url += "&id=" + persist.u.id;
        url += "&body=" + persist.u.body;
        url += "&title=" + persist.u.title;

        StartCoroutine(Upload(url));

        
    }
}
