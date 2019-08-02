# utility

<b> Utility. </b>

<br>

Hier wird das Utility Template bereitgestellt, welches insbesondere für moderne und zeitgemäße Themen wie Mode, Fashion oder Lifestyle geeignet ist.

Bei der Verwendung von Utility startet ihr ein neues Projekt mit folgenden Funktionalitäten:
<ul>
<li> Login und SignUp zur Plattform mit Benutzernamen und Passwort </li>
<li> Administration Interface, welches genutzt werden kann, um neue Blogbeiträge, Events oder Newsletter zu erstellen </li>
<li> Formulare direkt auf der Plattform zum Erstellen von Blogbeiträgen und Events für registrierte Nutzer </li>
<li> Registrierung zum Newsletter für alle User </li>
</ul>

<br>
<b> Wie Utility zu verwenden ist: </b>

Bitte stelle sicher, dass folgende Programme installiert sind:
<ul>
  <li> Python 3 </li>
</ul>

<br>
<b>Gehe folgendermaßen vor, um Utility zu starten:</b>
<ul>
  <li> Navigiere dich in der Konsole in den Ordner, in welchem du das Projekt Utility anlegen möchtest </li>
  <li> Installiere mit Python <i> -m venv myvenv</i> eine virtuelle Umgebung </li>
  <li> Starte deine virtuelle Umgebung und installiere in dieser mit Phython Pip mit <i>-m pip install --upgrade pip</i></li>
  <li> Clone das Utility GitHub Repository nun mit Hilfe von <i>git clone [URL zum Repository]</i></li>
  <li> Navigiere dich in den Ordner <i>utility</i> und installiere mit <i> pip install -r requirements.txt </i> alle benötigten Komponenten für Utility </li>
  <li> Lege in dem Vezeichnis, in welchem auch die Datei settings.py liegt, eine <i>local_settings.py</i> an </li>
  <li> Wenn du über den Newsletter E-Mails verschicken möchtest, trage in die local_settings.py den <i>EMAIL_HOST, EMAIL_HOST_USER,      EMAIL_HOST_PASSWORD, EMAIL_PORT</i> und <i>EMAIL_USE_TLS</i> für deinen Newsletter ein, andernfalls kann die local_settings.py Datei leer bleiben
  <li> Führe anschließend mit <i>python manage.py makemigrations</i> und <i>python manage.py migrate</i> eine Migration der App durch </li>
  <li> Erstelle mit <i> python manage.py createsuperuser </i> einen Superuser, welcher im Folgenden die Admin Funktionen erhält </li>
</ul>

<br>

Nun kannst du deinen Server starten und dich von Utility überzeugen. Das Projekt kann gerne nach individuellen Wünschen und Bedürfnissen individualisiert und angepasst werden.
