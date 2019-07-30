# utility

<b> Utility. </b>

<br>

Hier wird das Utility Template bereitgestellt, welches insbesondere für moderne und zeitgemäße Themen wie Mode, Fashion oder Lifestyle geeignet ist.

Bei der Verwendung von Utility, startet ihr ein neues Projekt mit folgenden Funktionalitäten:
<ul>
<li> Login und SignUp zur Plattform mit Benutzernamen und Passwort </li>
<li> Administration Interface, welches genutzt werden kann, um neue Blogbeiträge, Events oder Newsletter zu erstellen </li>
<li> Formulare direkt auf der Plattform zum Erstellen von Blogbeiträgen und Events für registrierte Nutzer </li>
<li> Regisitrierung zum Newsletter für alle User </li>
</ul>

<br>
<b> Wie Utility zu verwenden ist: </b>

Bitte stelle sicher, dass folgende Programme installiert sind:
<ul>
<li> Python 3 </li>
<li> Sqlite </li>
</ul>

<br>
<b>Gehe folgendermaßen vor, um Utility zu starten:</b>
<ul>
<li> Navigiere dich mithilfe in der Konsole in den Ordner, in welchem du das Projekt Utility anlegen möchtest </li>
<li> Starte deine virtuelle Umgebung und installiere dort Django und Pip </li>
<li> Clone das Utility GitHub Repository nun mit Hilfe von git clone und des GitHub Links </li>
<li> Installiere mit pip install -r requirements.txt alle benötigten Komponenten für Utility </li>
<li> Lege in dem Vezeichnis, in welchem auch die Datei settings.py liegt, eine local_settings.py an </li>
<li> Wenn du über den Newsletter E-Mails verschicken möchtest, trage in die local_settings.py den EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT und EMAIL_USE_TLS für deinen Newsletter ein
<li> Führe anschließend mit python manage.py makemigrations und migrate eine Migration der App durch </li>
<li> Erstelle mit createsuperuser einen user, welcher im Folgenden die Admin Funktionen erhält </li>
</ul>

<br>

Nun kannst du deinen Server starten und dich von Utility überzeugen. Das Projekt kann gerne nach individuellen Wünschen und Bedürfnissen individualisiert und angepasst werden.
