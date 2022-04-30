![SpaceDrummers](https://github.com/H3cth0r/spaceDrummersProyect/blob/main/vectors/portada/portada.png)

## Collaborators
<ul>
    <li> Héctor Miranda García A01658845</li>
    <li> Misael Chavez Ramos A01659759</li>
    <li> German Wong del Toro A01655080</li>
    <li> Victor Hugo Portilla Ortiz A01659198</li>
</ul>

## General Project Information
This project aims to make a videogame, a running server and a webpage for said game. 

## General Project Structure

```
spaceDrummersProyect
    ├───animations
    ├───dataBase
    ├───django_server
    │   └───sd_server
    │       ├───sd_server
    │       │   └───__pycache__
    │       ├───static
    │       │   ├───profile_photos
    │       │   │   └───the_data
    │       │   ├───resources
    │       │   ├───scripts
    │       │   │   └───anime-master
    │       │   │       └───anime-master
    │       │   │           ├───.github
    │       │   │           │   └───ISSUE_TEMPLATE
    │       │   │           ├───documentation
    │       │   │           │   ├───assets
    │       │   │           │   │   ├───css
    │       │   │           │   │   ├───fonts
    │       │   │           │   │   ├───img
    │       │   │           │   │   │   └───icons
    │       │   │           │   │   └───js
    │       │   │           │   │       ├───anime
    │       │   │           │   │       └───vendors
    │       │   │           │   └───examples
    │       │   │           ├───lib
    │       │   │           └───src
    │       │   ├───styles
    │       │   │   └───helvetica_font
    │       │   └───videogame_file
    │       ├───templates
    │       │   └───registration
    │       └───videojuego
    │           ├───migrations
    │           │   └───__pycache__
    │           └───__pycache__
    ├───single_scripts
    │   └───txt_tabs
    ├───staticAPIs
    ├───unity
    ├───vectors
    │   ├───alien_1
    │   ├───alien_2
    │   ├───alien_3
    │   ├───alien_4
    │   ├───alien_5
    │   ├───background
    │   ├───config
    │   ├───drumstick
    │   ├───in_level_pack_selection
    │   ├───level_pack_selection
    │   ├───login_assets
    │   ├───main_menu
    │   ├───pause_menu
    │   ├───portada
    │   └───space_ship
    └───website_sd
        ├───resources
        ├───scripts
        │   └───anime-master
        │       └───anime-master
        │           ├───.github
        │           │   └───ISSUE_TEMPLATE
        │           ├───documentation
        │           │   ├───assets
        │           │   │   ├───css
        │           │   │   ├───fonts
        │           │   │   ├───img
        │           │   │   │   └───icons
        │           │   │   └───js
        │           │   │       ├───anime
        │           │   │       └───vendors
        │           │   └───examples
        │           ├───lib
        │           └───src
        └───styles
            └───helvetica_font
```


- **website_sd(Space Drummers website)** <br> Here we store every file required to view and run the official SpaceDrummers project website. On the main folder you will find the html files where the resources, scripts and style are being applied.
  - **resources**: Here we store images and icons that are applyed on the site.
  - **scripts**: Here are a series of js scripts necessary for some animatiosn and data processing.
  - **styles**: On this foldew we store all the css and font files used for the styling of our website.
- **django_server**: Here are located all the correspongin django files and exes for running our server.
- **vectors**: Here are located the design object located on the website and unity game.
- **staticAPISs**: This are the examples of APIs that will give functionality to the game.
- **dataBse**: We saved all files relationated with the database architecture.


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
