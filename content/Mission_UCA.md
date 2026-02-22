Title: Mission_UCA
Date: 2024-03-10 15:00
Modified: 2024-03-10 15:00
Category: Python
Tags: pelican, publishing
Slug: stage_uca
Authors: Gros damien
Summary: Mission implémentation de raccourci dans le menu de l’ENT de L’UCA, durant le stage de deuxième année dans l'Université de L'UCA (université Clermont Auvergne) site d'Aubière.
type: SLAM
style: contenu

### Stage de 2er année à Université Clermont Auvergne (UCA)

#### L'organisme d'accueil

Dans le cadre de notre formation de BTS SIO, nous avions un stage de 6 semaines en entreprise durant la période du 8 janvier 2024 au vendredi 16 février 2024 (inclus). J'ai effectué mon stage dans l'Université Clermont Auvergne (UCA), dans le département de la DSI. l'équipe de la DSI était composée d'une dizaine de personnes. Le département s'occupe de différence application en lien avec l'ENT et les outils de l'université. (ENT, cour en ligne, noodle, ressource des cours, app de gestion d'accès dans certains bâtiments, etc.)

#### Contexte 

J'ai été affecté au menu d'accueil de l'ENT. Le design du site internet de l'université ayant fait l'objet d'une refonte graphique, il a été jugé interréssant de modifier l'ENT pour coller à la nouvelle charte graphique de l'UCA l'ENT a donc fait l'objet d'une refonte intégrale que ce soit du design et du fonctionnement (nom de domaine, etc.) lors de mon stage ce nouveau menu était en phase de test et ouvert une certaine population. (utilisateur avec comme rôle "personnel")

![image](./themes/mon-theme-pelican/static/images/stage_uca/maquette_web.png)
![image](./themes/mon-theme-pelican/static/images/stage_uca/current_dashboard.png)

**l'application**
l'ENT est une application web sous PHP 5 et symfony7
Elle implémente du JS et exécute des requêtes Ajax à la base de données ainsi que Bootstrap et du SCSS pour tout ce qui est CSS est responsivité.
Pour les classes Modèles, elle implémente des classes ORM avec l'utilisation de doctrine.

**organisation de l'équipe**
Chaque personne s'occupe d'un type d'application en principal. (Ex : administratif, etc.) Tout le monde a au moins 1 jour de télétravail, ils utilisent donc teams

Ma mission consistait principalement à l'implémentation de widget raccourci dans le nouveau menu de l'application avec plusieurs tickets gérer sur notion.org.

![image](./themes/mon-theme-pelican/static/images/stage_uca/notions.png)
![image](./themes/mon-theme-pelican/static/images/stage_uca/notions2.png)

J'ai eu plusieurs tickets correspondant aux tâches suivantes :
- implémentation widget_shortcut :
Ajout d'un widget de raccourcis avec la possibilité de sélectionner 6 shortcuts à l'aide d'un bouton (+) qui ouvre le modal ou l'on sélectionne parmi tous les menus possibles de l'ENT et ou il est possible de les réorganiser
![image](./themes/mon-theme-pelican/static/images/stage_uca/shortcut/menu_customization.png)
![image](./themes/mon-theme-pelican/static/images/stage_uca/shortcut/customization-shortcuts_modal.png)
Cette mission a demandé l'apprentissage et l'utilisation de Bootstrap pour le rendu du template twig, de JS pour la réorganisation des menus dans le widget à partir du modal et de doctrine pour la récupération et la construction des objets menus.

- Modification Widget_email :
Modification du widget email déjà présent qui affichait les mails non lus pour permettre à l'utilisateur de pouvoir choisir entre "afficher tous les emails non lus" ou "afficher les emails non lus du jour" ainsi que l'affichage ou non du titre des derniers messages non lu
    
![image](./themes/mon-theme-pelican/static/images/stage_uca/email/menu_widget_email.png)
    
La messagerie et la récupération des messages de l'ENT s'appuient sur l'API Zimbra (messagerie et calendrier) montré ci-dessous. Il a donc été nécessaire d'apprendre le fonctionnement de l'API en recherchant à tatillon, car la documentation est pratiquement inexistante.
    
![image](./themes/mon-theme-pelican/static/images/stage_uca/email/apizimbra.png)

Pour cela une API de test zimbra a été mise en place.

![image](./themes/mon-theme-pelican/static/images/stage_uca/email/apizimbra_test.png)

- Traduction de l'application en anglais
Traduction de l'application en anglais par le biais de la fonctionnalité translation native à symfony.
Cette mission était à l'origine le 2e ticket assigné cependant, il a été mis en pause, car n'étant pas la priorité sur les autres missions et étant bloquer à un stade particulier par manque de connaissances de ma part et une contrainte technique lié a l'application (nom de domaine et routes), mon maître de stage étant assez occupé la mission prenais plus de temps que ce qu'il était nécessaire.

![image](./themes/mon-theme-pelican/static/images/stage_uca/translation/menu-en.png)
![image](./themes/mon-theme-pelican/static/images/stage_uca/translation/email.twig-translation.png) 


**Programation**  

#### environnement technologique

- pc sous Linux (Ubuntu)*
- Teams et Rocket (communication au sein de l'entreprise)
- Notion (la gestion des tickets assignés et le journal de bord)
- API Zimbra (gestion de la messagerie et calendrier)
- PHP version 5
- Symphony version 7
- JS et Ajax
- Classe ORM Doctrine

#### Compétences mobilisés

- **B1.2.3 Traiter des demandes concernant les applications**
- traitement des demandes d'evolution d'une application web pour suivre le changement de charte graphique et de fonctionnement.
- **B1.4.1 Analyser les objectifs et les modalités d’organisation d’un projet**
- Prise en main du projet en vue d'atteindre l'objectif fixé (ajouter des widgets et les adapter sur le nouveau menu), tout en suivant l'organisation déjà établis par les membres de l'équipe et de l'organisation (utilisation des outils, respect de la normalisation, etc.)
- **B1.4.2 Planifier les activités**
- planification de mon développement pour respecter la date de mise en production des différents éléments et features de la page en vue de l'élargissement de la population de test
