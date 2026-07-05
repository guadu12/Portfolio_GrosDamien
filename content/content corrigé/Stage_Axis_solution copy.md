Title: Stage_Axis
Date: 2023-06-26 17:00
Modified: 2023-06-26 17:00 17:00
Category: Python
Tags: pelican, publishing
Slug: Axis_solution_copy
Authors: Gros damien
Summary: Mission implémentation d’une solution de gestion des Formations sur l’application de l’entreprise, durant le stage de fin de première année du BTS SIO, dans l'entreprise Axis Solution
type: SLAM
style: contenu

# Stage de 1re année (Axis Solution)

### Contexte 

La société Axis est certifiée Qualiopi. Cette certification vise à attester la qualité du processus de formation. Le fonctionnement interne s'appuyait sur des tableaux de suivi Excel. Le but du développement était d'améliorer ce fonctionnement, mais aussi le suivi des formations afin de ne pas oublier de documents. De plus, il avait également pour objectif de générer des documents automatiques afin de gagner du temps en termes de gestion.

Le développement devait être implémenté pour une version du logiciel de gestion de l'entreprise, **Axilta'2**. À partir d'un clone du projet Axilta'2, je devais prévoir et implémenter un bouton "Formation" dans le menu "Vente" de l'application, qui ouvrirait une fenêtre permettant de lister les formations avec les informations suivantes :

- un libellé
- le client
- le type de formation
- la date de la formation
- l'état (fini ou en cours)
- le répertoire de la formation

Il devait également être possible de filtrer la liste des formations par libellé, date ou état.  
L'interface devait disposer de boutons "Ajouter", "Modifier", "Supprimer". Le double-clic sur une formation devait exécuter la même fonction que le bouton "Modifier". Le bouton "Supprimer" afficherait un pop-up de confirmation pour permettre la suppression de la ligne sélectionnée.

**Axilta'2 :**

![image](./themes/mon-theme-pelican/static/images/stage_axis/Axilta2_menu.PNG)

Depuis cette fenêtre de formation, il devait être possible d'accéder à **La fiche de formation** qui devait contenir :

- le libellé 
- le client
- la date de formation 
- le type de formation
- un champ "Terminer" pour l'état de la formation

**Dans les paramètres de données de base**

**Formation type**  
Une interface qui permettrait de lister, ajouter, modifier, supprimer les types de formation.  
Les types de formation étaient :
- **Gestactiv'2**
- **Axilta'2**

**Type de chronologie**  
Une interface permettant de lister, ajouter, modifier, supprimer un type de chronologie.  
Une chronologie devait être constituée de :

- un libellé (Ex : Devis, Formation)
- un répertoire (Ex : 1-Devis, 3-Formation)
- un ordre d'affichage (Ex : Ordre, 3)

![image](./themes/mon-theme-pelican/static/images/stage_axis/ex_type_chrono.jpg)

Pour chaque type de formation, il devait être possible de renseigner un ou plusieurs documents, composés de :

- un libellé (255 caractères, champ obligatoire)
- une description
- un type de chronologie
- un ordre d'affichage
- un modèle Word
- un document global à la société ou spécifique à un interlocuteur (génération ou ajout du document)
- possibilité d'envoi et de réception

Pour chaque formation, il devait être possible de sélectionner un ou plusieurs interlocuteurs du client (société) et l'interface devait permettre l'ajout de nouveaux interlocuteurs.  
Depuis la fiche formation, il devait être possible de générer les documents et de les sauvegarder dans le répertoire souhaité. Pour chaque document, il fallait pouvoir renseigner :

- la date
- la date de réception
- le chemin d'envoi (document envoyé)
- le chemin de réception (document reçu)
- le chemin de l'email d'envoi
- le chemin de l'email de réception
- la validation

Suite à l'analyse de l'application à l'aide de l'IDE **WinDev** et des différentes tables de la base de données à l'aide des logiciels **Microsoft SQL Server Management Studio 18** et **Azure Data Studio**, il a été nécessaire de créer cinq nouvelles tables :

- **Formation**
- **Formation_type**
- **Formation_doc**
- **Type_chronologie**
- **Formation_doc_client**

![image](./themes/mon-theme-pelican/static/images/stage_axis/Microsoft%20Sql%20Server%20Manager%20(cr%C3%A9ation%20de%20table).PNG)

Ces nouvelles tables étaient en relation avec des tables déjà existantes dans la base de données (Ex : **TABLE : DocumentWord / TABLE : Client**), qui servaient à la création d'une fenêtre de gestion des formations, permettant de les lister et de les modifier.

En amont de la création de ces tables, un diagramme **CMD** ou **UML** devait être créé pour expliquer les dépendances entre les tables existantes et les nouvelles.

![image](./themes/mon-theme-pelican/static/images/stage_axis/shema_dependances.PNG)

### Programmation  

Une fois le schéma CMD validé par le chef de projet et les tables créées, je suis passé à l'implémentation de la fonctionnalité.  
Toujours sur le logiciel **WinDev**, la programmation sur ce logiciel peut être faite en français ou en anglais.  
Pour le logiciel **Axilta'2**, le code était en français.

Ce travail a nécessité une prise en main du langage et du logiciel de programmation **WinDev**, en utilisant notamment la documentation officielle de **PC SOFT** (très détaillée, précise et intégralement en français).

![image](./themes/mon-theme-pelican/static/images/stage_axis/PCSOFT%20doc.PNG)

Il a ensuite été nécessaire de faire une veille active afin d'accomplir chaque tâche et fonction de l'application. Pour cela, je me suis appuyé sur :

- la documentation officielle **WinDev** (windev.com)
- **SQL.sh** (SQL)
- **developpez.com**, **WDF** (forum d'entraide de développement)

Cette mission m'a permis de mobiliser les compétences acquises en SQL avec l'ajout des tables et la manipulation des données de l'application.  
J'ai également développé des compétences en recherche et en veille, ainsi qu'une meilleure compréhension de la logique métier.

### Environnement technologique

- Clone du logiciel **Axilta'2**
- IDE et langage **WinDev**
- **Windows**
- Base de données **MySQL**
- **Azure** (Windows)

### Compétences mobilisées

- **B1.6.2 Mettre en œuvre des outils et stratégies de veille informationnelle**  
  Recherche approfondie dans la documentation et sur des forums spécialisés en développement pour trouver des solutions.

- **B1.4.1 Analyser les objectifs et les modalités d’organisation d’un projet**  
  Projet avec une vision logistique claire encadré par un chef de projet.

- **B1.2.3 Traiter des demandes concernant les applications**  
  Étude du code existant et modification ou utilisation pour la création de nouvelles fonctionnalités.
