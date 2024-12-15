# Ecole-Alarme

Dans le cadre de mon cours d<internet des objets et de IA, le premier exercise que nous avons effectuer etais de faire un petit systeme d'alarme.

Dans ce cours de programmation embarquer, il falait initier les OUTPUT et INPUT d'un raspberry PI pour controller des DEL et un buzzer, en plus de devoir avoir des input pour surveiller l'environment(deux bouton et un detecteur de mouvement.

Initialement, j'ai effectuer un code plus primaire, mais je me suis donner comme defi de le faire en mode classes/objet pour mon developpement. 

Voici donc le resultat de mes efforts pour ce projet.

Exercice : Gestion d'un Système de Sécurité avec Raspberry Pi

Objectif

Créer un système de sécurité interactif utilisant les GPIO du Raspberry Pi, intégrant des boutons (en pull-up et pull-down), des LEDs, un détecteur de mouvement, et un buzzer. Le programme doit être écrit en Python et inclure une logique simple de gestion des événements.

Schéma du système

LED rouge : Connectée à un GPIO configuré en sortie.
LED verte : Connectée à un GPIO configuré en sortie.
Buzzer : Connecté à un GPIO configuré en sortie.
Bouton 1 (Mode Armement) : Configuré en entrée avec une résistance pull-up.
Bouton 2 (Désarmement) : Configuré en entrée avec une résistance pull-down.
Détecteur de mouvement PIR : Configuré en entrée pour détecter une présence.
Logique à implémenter

Mode par défaut
Le système est désarmé au démarrage.
La LED verte est allumée pour indiquer que le système est inactif.
La LED rouge et le buzzer sont éteints.
Armement
Lorsque le Bouton 1 est pressé, le système passe en mode "armé".
La LED rouge s'allume, et la LED verte s'éteint.
Le détecteur de mouvement est activé pour surveiller la zone.
Détection de mouvement (si armé)
Si le détecteur de mouvement PIR détecte une présence, le buzzer émet un son (alarme).
La LED rouge clignote pour signaler une alarme active.
Désarmement
Lorsque le Bouton 2 est pressé, le système revient en mode "désarmé".
Le buzzer s'arrête immédiatement.
La LED rouge s'éteint et la LED verte se rallume.
Spécifications des GPIO

GPIO en sortie
LED rouge (choisir un GPIO, par exemple GPIO 18).
LED verte (choisir un GPIO, par exemple GPIO 23).
Buzzer (choisir un GPIO, par exemple GPIO 24).
GPIO en entrée
Bouton 1 avec pull-up (choisir un GPIO, par exemple GPIO 17).
Bouton 2 avec pull-down (choisir un GPIO, par exemple GPIO 27).
Détecteur de mouvement PIR (choisir un GPIO, par exemple GPIO 22).
Contraintes de programmation

Utiliser des interruptions (GPIO.add_event_detect) pour gérer les boutons-poussoirs.
Implémenter une boucle principale qui surveille l'état du détecteur de mouvement.
Gérer l'état (armé/désarmé) à l'aide d'une variable globale ou un état logique.
Implémenter un clignotement pour la LED rouge pendant une alarme (en utilisant time.sleep() pour simuler le clignotement).
Exemple de comportement attendu

Démarrage
LED verte allumée (système désarmé).
Appui sur Bouton 1
LED rouge s'allume, LED verte s'éteint (système armé).
Détection de mouvement (PIR)
LED rouge clignote, buzzer émet un son.
Appui sur Bouton 2
LED rouge et buzzer s'éteignent, LED verte s'allume (système désarmé).

Carl Bougie
