# Iter - Stat

## zweck

berechen folgender leisungsindikatoren einer iteration:

* summer der efforts für jeden status
* unfertig vs fertig auf ebene efforts
* maximale anzahl durchlaufener sprints der issues

die angaben werden für die berechnung der iterations kapazität genutzt.  

## inputs

die inputs werden in jira erstellt (csv exports):

* gehe zum report **sprint report**
* wähle für *comleted* und *issues not completed* die *issue navigator* ansicht
* exportiere die ansichten zu csv mit mindestens den spalten
  * status
  * original estimate
  * sprint

die inputs werden ohne weitere bearbeitung und unter beliebigen namen (extension .csv muss vorhanden sein) im top-level directory abgelegt.  

## reaultate

ausgabe der resultate:

* im terminal
* im directory *results* befinden sich die ausgabedateien

## ausführung

direkt aus dem terminal oder via ide-run.  
