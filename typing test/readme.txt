Zweck des Skriptes

Der Zweck des Skriptes ist es ein Programm zu schreiben welches ähnlich wie «monkeytype» funktioniert.
Der Benutzer kann somit seine Words per minute herausfinden.
Es soll den User in seiner schreib Geschwindigkeit und in seiner Genauigkeit fördern um Texte oder ähnliches schreiben.

------------------------------------------------------------------------------------------------------------------------
Ziel Beschreibung

1. Jedes Wort soll auf seine Richtigkeit überprüft werden.
2. Es soll ein Benutzerfreundliches GUI haben.
3. Die Berechnung der Wörter pro Minute und Genauigkeit soll funktionieren.
4. Ergebnisse der Berechnungen sollen in einer Datenbank gespeichert werden.
5. Die Ergebnisse sollen auch wieder ausgegeben werden.

------------------------------------------------------------------------------------------------------------------------
Anforderungen an das Skript

Die Anforderungen sind, dass, das Skript Überprüfungen der Eingabe durchführt.
Diese Überprüfung soll das Skript mittels RegEx machen, es soll somit erkennen, ob das geschriebene Wort korrekt oder inkorrekt ist.
Das GUI soll anschaulich und benutzerfreundlich gestaltet sein, so dass jeder Mensch auch nicht allzu bewanderte Menschen denn Umgang mit dem Skript verstehen.
Das Programm soll eine Berechnung durchführen, welche die Wörter pro Minute berechnet.
Dies kann man sich so vorstellen, dass wenn der Benutzer schneller tippt, steigen die Wörter pro Minute an.
Es soll auch die Genauigkeit des Benutzers berechnet werden, also desto weniger Fehler beim Schreiben geschehen desto besser ist die Genauigkeit.
Jegliche Ergebnisse der Berechnungen für die Wörter pro Minute und die Genauigkeit sollen in einer Datenbank abgespeichert werden, wenn der Benutzer das auch will.
Sobald es abgespeicherte Daten gibt, sollen diese auch angezeigt werden. Somit kann der Benutzer das beste Ergebnisse zum Beispiel sehen.

-----------------------------------------------------------------------------------------------------------------------
Anweisung

Die Bedienung des Programms ist denkbar einfach, da alles über die grafische Benutzeroberfläche (GUI) erfolgt.
Im Hauptmenü gibt es die Möglichkeit, den Schwierigkeitsgrad und die Satzlänge zu wählen.
Sobald man sich für das leichte oder das schwere Programm entschieden hat, muss der Benutzer nur noch den Test eingeben, um die Geschwindigkeit (in Sekunden), die WPM (Wörter pro Minute) und die CPM (Zeichen pro Minute) zu messen.
Die Daten können in einer MySQL-Datenbank gespeichert werden und der Highscore kann jederzeit abgerufen werden.
