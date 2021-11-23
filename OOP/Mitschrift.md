<div style="width:500px">

# Datenkapselung

Software-Objekte (als Programmiereinheiten) werden so knzipiert, dass Details über den inneren Aufbau verborgen werden und Änderungen von Objekzuständen nur über dafür vorgesehene Methoden erfolgen können. Das Verbernen des inneren Aufbaus wird realisiert, indem man keinen direkten Zugriff auf die Attribute zur Verwaltung der internen Daten ermöglicht. Man nennt diese Vorgehensweise auch: _*Datenkapselung*_. 

---
## Zugriffsrechte/Zugriffsmethoden  
Um interne Daten kapseln zu können werden Zugriffsrechte festgelegt. Der Entwickler einer Klasse hat die Möglichkeit, Attribute und Methoden einer Klasse als öffentlich oder privat zu deklarieren. Lesende und schreibende Zugriffe auf Attribute bzw. Methoden eines Objektes sind nur möglich, wenn diese öffentlich sind. Private Attribute und Methoden können dagegen nur bei der Implementierung der betreffenden Klasse benutzt werden. 

Im Klassendiagramm werden die Rechte auf die Attribute und Methoden mit Hilfe der Symbole `+` und `-` (öffentlich und privat) festgelegt. Verfolgt man die Strategie, alle Attribute als privat zu deklarieren, so besteht keine Möglichkeit, lesend oder schreibend Werte zu ändern. 
Um dennoch solche Zugriffe zuzulassen, werden spezielle öffentliche Zugriffsmethoden (.set / .get ) bereitgestellt. Das Klassendiagramm wird daher um solche Methoden erweitert.

</div>