# flippo - Dobjatok fel egy érmét online!
Tegyük fel, hogy valakivel beszélgetsz **online**, és valamiről nem tudtok megegyezni, ezért feldobnátok egy pénzérmét.
A lehetőségeid:
 - Egyikőtök feldob egy érmét és megírja az eredményt: a kijelölt azt füllent, amit akar.
 - A **flippo** segítségével a kijelölt létrehoz egy sorsolást, majd a létrehozott linket megosztja.

Az eredmény akkor és csak akkor válik láthatóvá, ha két különböző böngészőből meglátogatták a linket. Ha ezután egy harmadik helyről is meglátogatják a linket, akkor az illető egy hibaüzenetet kap: "This coin has already been flipped!".
Ez a két feltétel megakadályozza azt, hogy a kijelölt fél lássa a sorsolás eredményét, mielőtt megosztja, és ezután megossza a másikkal, tehát nem lehet trükközni, ugyanis mindkét fél tudja, ha a másik trükközni próbál.

A böngészőket **cookie**-k segítségével azonosítom. A [Flask](http://flask.pocoo.org/) könyvtárat használtam, mert viszonylag kevés kóddal sokat lehet vele elérni. A Redis adatbázist viszonylagos egyszerűsége miatt választottam.

### Követelmények a telepítéshez
 - Python 2 vagy Python 3: https://www.python.org/. 
 - Redis adatbázis, de **csak** ha az van tárolónak választva: https://redis.io.

### Telepítés és futtatás
 1. Töltsd le a repository-t, pl: `git clone https://github.com/madasigon/flippo`
 2. Menj be a reporitory mappájába, pl: `cd <ahova_letöltötted>/flippo`
 3. Szükség esetén konfiguráld.
 3. Telepítsd a szükséges Python modulokat: `python -m pip install -r requirements.txt`
 5. Futtasd: `python run.py`
 6. Látogasd meg a kezdőoldalt: http://localhost:5000/

### Konfiguráció
A sorsolások(Flip-ek) eltárolására két opctió van, az egyik, hogy egy Python változóban tároljuk(PythonFlip, ez elveszik a program leállása után!), illetve a Redis adatbázis használata(RedisFlip). A választásra a **models.py** fájlban a "Flip" változó értékadásánál van lehetőség(utolsó sor).
Ha a **Redis opció** van kiválasztva, akkor a **flippo.py** megfelelő sorát át kell írni a használt Redis adatbázis URL-jére.

#### Fejlesztési lehetőségek
 - Bejelentkezési lehetőség (pl. Google felhasználóval), ezáltal a sorsolások követhetőségének javítása. Ezesetben akárhány ember részt vehet egy sorsolásban és senki sem állíthatja azt, hogy ő valamiért nem látja az eredényt.
 - Kinézet, felhasználói felület javítása. A projekt egyelőre csak az alapvető funkcionalitás demonstrációja.
