# Space Drummers

## Collaborators
<ul>
    <li> Héctor Miranda García A01658845</li>
    <li> Misael Chavez Ramos A01659759</li>
    <li> German Wong del Toro A01655080</li>
    <li> Victor Hugo Portilla Ortiz A01659198</li>
</ul>

## Explanation
This pro





## Classes

### Send and Used on Unity

- **Login**
  * Attributes
      - userName:TMP_input_field:
      - hashPwd:TMP_input_field 
  * Methods
      - MD5_hash(stsring):string
      - Upload(string):IEnumerator
      - LoginButton(Clicked):void



- **Session**
  * Attributes
      - startTime:string
      - endTime:string
      - currentLevel:int <========
  * Methods
      - gets()
      - sets()

- **Attempt(per level gamed)**
  * Attributes
      - levelId:Int
      - Score:Int
      - Succed:Bool
      - timeWhenScored:String
      - KOS:Int
      - failedShotos:Int
      - totalShots:Int
  * Methods
      - gets()
      - sets()
- **User**
  * Attributes
      - userId:int
      - userName:string
      - userId:int
      - currentSession:Session
  * Methods
      - gets()
      - sets()
### Send and used on server

- **InitialSession(response from server)**
  * Attributes
      - currentLevel:int 
      - accessGranted:bool
      - userId:int
      - userName:string
  * Methods
     eq