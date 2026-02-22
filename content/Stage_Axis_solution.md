Title: Stage_Axis
Date: 2023-06-26 17:00
Modified: 2023-06-26 17:00 17:00
Category: Python
Tags: pelican, publishing
Slug: Axis_solution
Authors: Gros damien
Summary: Mission implémentation d’une solution de gestion des Formations sur l’application de l’entreprise, durant le stage de fin de première année du BTS SIO, dans l'entreprise Axis Solution
type: SLAM
style: contenu

### Stage de 1er année (Axis Solution)

#### Contexte 
La société Axis est certifiée Qualiopi. Cette certification vise à attester la qualité du processus de formation. Le fonctionnement interne était avec des tableaux de suivi Excel. Le but du développement était d'améliorer le fonctionnement, mais aussi le suivi de formation afin de ne pas oublier de document. De plus, il avait aussi pour but de générer des documents automatiques afin de faire gagner du temps en termes de fonctionnement.

Le développement devait être implémenté pour une version du logiciel de gestion de l'entreprise, Axilta. Pour cela à partir d'un clone du projet Axilta'2, je devais prévoir et implémenter un bouton "formation" dans le menu "vente" de l'application qui ouvrirait une fenêtre qui permettra de lister les formations avec comme informations :

- un libellé
- le Client
- le type de formation
- la date de la formation
- l'Etat (fini ou en cours)
- le répertoire de la formation
Et où il serait possible de filtrer la liste des formations par libellé date ou était.
l'Interface devait disposer également de boutons "ajoutés", "modifier", "supprimer". Le double-clic sur une formation exécuterait le même fonctionnement que le bouton "modifié". Et le bouton "supprimer" afficherai un pop-up de confirmation qui permettra la suppression de la ligne sélectionnée.

Axilta'2 :

![image](./themes/mon-theme-pelican/static/images/stage_axis/Axilta2_menu.PNG)

À partir de cette fenêtre de formation, on devait pouvoir accéder a **La fiche de formation** qui devait contenir :

- le Libellé 
- le Client
- La date de formation 
- Le type de formation
- Champ "Terminer" pour l'état de la formation

**Dans les paramètres de données de base**

**Formation type**
Une interface qui permettrait de lister, ajouter, modifier, supprimer les types de formation
Les types de formation étaient :
- Gestactiv'2
- Axilta'2

**Type de chronologie**
Une interface qui permettrait de lister, ajouter, modifier, supprimer un type de chronologie
Un chronologie devait être constituée de :

- Un libellé (Ex : Devis, Formation)
- d'un répertoire (Ex : 1-Devis, 3-Formation)
- d'un ordre d'affichage (Ex : Ordre, 3)

![image](./themes/mon-theme-pelican/static/images/stage_axis/ex_type_chrono.jpg)

Pour chaque type de formation, il devait être possible de renseigner 1 ou plusieurs documents composé de :

- un Libellé (255 caractères, champ obligatoire.)
- Une description
- un type de chronologie
- Un ordre d'affichage
- Un modèle Word
- Document global à la société ou par Interlocuteur (génération ou ajout du doc)
- de l'envoyer et reçu

Pour chaque formation, il devait être possible de sélectionner 1 ou plusieurs interlocuteurs du client (société) et l'interface devait permettre l'ajout de nouveaux. 
Interlocuteurs sur la fiche clients de la formation
Depuis la fiche formation, il devait être possible de générer les documents et de les sauvegarder dans le répertoire souhaité. Pour chaque document, il fallait pouvoir renseigner. 

- la date
- la date de reçu
- le chemin d'envoi (le doc envoyée)
- chemin reçu (le doc reçue)
- chemin email d'envoi (l'email d'envoi)
- chemin d'email reçu (l'email de reçu)
- la validation

Suite à l'analyse de l'application à l'aide de l'IDE de WinDev et des différentes tables de donnée de la base à l'aide du logiciel Microsoft SQL server management studio 18 et Azure Data Studio, il était nécessaire de créer 5 nouvelles Tables

- Formation
- Formation_type
- formation_doc
- Type_chronologie
- formation_doc_client

![image](./themes/mon-theme-pelican/static/images/stage_axis/Microsoft Sql Server Manager (création de table).PNG)

En relation avec des tables déjà existantes dans la base de données (Ex TABLE : DocumentWord / TABLE : client) qui serviront à la création d'une fenêtre de gestion de formations qui les listera et permettra la modification de ces dernières

En amont de la création de ces tables un diagramme CMD ou UML devait être créé expliquant les dépendances entre les
Tables existantes et les nouvelles 

![image](./themes/mon-theme-pelican/static/images/stage_axis/shema_dependances.PNG)

**Programation**  
Une fois, le schéma CMD Validé par le chef de projet et les Tables créent, je suis passé à l'implémentation de la fonctionnalité 
Toujours sur le logiciel WinDev, la programmation sur ce logiciel peut être en français ou en anglais. 
Pour le logiciel Axilta'2 le code était en français.  

Rajouter l'aspect de recherche (langage nouveau, site utilisé etx)
Ce travail à necessessité une prise en main du langage et logiciel de programmation WinDev en utilisant notamment la documentation officiel de **PC SOFT** (très détaillé et précise et intégralement en français)
![image](./themes/mon-theme-pelican/static/images/stage_axis/PCSOFT doc.PNG)

Il a ensuite été nécessaire de faire une veille active afin de pouvoir accomplir chaque tâche et fonctions de l'application. Pour cela, je me suis servi de :

- la Documentation officielle WinDev (windev.com)
- SQL.sh (SQL) 
- developpez.com, WDF (forum d'entraide de développement)

Cette mission à permis de mobiliser les compétences apprit en SQL avec l'ajout des tables et la manipulation des données de l'application.
Les compétences de recherches et de veilles ainsi qu'un développement de connaissance de la logique métier.

#### environnement technologique
- clone du logiciel Axilta'2
- IDE et langage windev
- Windows
- base de données MYSQL
- Windows azure.

#### Compétences mobilisés
- **B.1.6.2 Mettre en œuvre des outils et stratégie de veille informationnelle**
- Recherche approfondis de la doc ou de forum spécialisé développement pour trouver des solutions 
- **B1.4.1 Analyser les objectifs et les modalités d’organisation d’un projet**
- Projet avec une vision logistique clair avec chef de projet
- **B1.2.3 Traiter des demandes concernant les applications**
- Étude de code existant et modification ou utilisation pour faire de nouvelle fonctionnalité
