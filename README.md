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

## General Project Structure
- **website_sd(Space Drummers website)** <br> Here we store every filed required to view and run the official SpaceDrummers project website. On the main folder you will find the html files where the resources, scripts and style are being styled.
  - **resources**: Here we store images and icons that are applyed on the site.
  - **scripts**: Here are a series of js scripts necessary for some animatiosn and data processing.
  - **styles**: On this foldew we store all the css and font files used for the styling of our website.



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
      - userInfo:User
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
      - sendDataToServer()
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

- **Settings**
   * Attributes
       - volumeLevel:int
       - controlConfig:Control
   * Methods
       - changeVolume(int):bool
       - resetControls():bool
       - changeControlConfig()bool
- **Control**
   * Attributes
       - controlOne:char
       - controlTwo:char
       - controlThree:char
       - controlFour:char
   * Methods
       - defaultControls():bool
       - gets():char
       - sets(char):bool
### Send and used on server

- **InitialSession(response from server)**
  * Attributes
      - currentLevel:int 
      - accessGranted:bool
      - userId:int
      - userName:string
  * Methods
      - Gets()
      - Sets()
