Title: gestion de ticket
Date: 2023-05-08 17:00
Modified: 2023-05-08 17:00
Category: Python
Tags: pelican, publishing
Slug: AMAphp_1a
Authors: Gros damien
Summary: Mission gestion d'incidents sur l'application AMAphp dans son itération 1a (contexte AMAP).
type: SLAM
style: contenu

### Gestion de ticket d'une application web de gestion de panier et de paysans AMAphp

#### Contexte
![mon image](./themes/mon-theme-pelican/static/images/AMAphp/acceuil_AMAphp.png)

Réalisation d'un projet de gestion de ticket dans le contexte du projet AMAP avec l'application web AMAphp sous la version 1a.
Pour cette mission plusieurs rapports d’erreur dans l'application, on était fait, nous avions à choisir un de ces rapports d’erreurs à traiter (ce choix était irréversible.).
![mon image](./themes/mon-theme-pelican/static/images/AMAphp/ticket_incident.png)

Nous avions ensuite créé un ticket sur la forge logicielle framagit qui visait à répondre à la problématique de ce rapport d'erreur. 


Le ticket produit sur framagit devait contenir 

- Une description des incidents (la description et l'effet de l'incident)
- une analyse des causes du problème qui conclue une analyse des corrections possibles
- une analyse des Dépendances Fonctionnelles avec un schéma relationnel (si la correction envisagée demandait une modification des variables de la base de données).
- Les actions réalisées en fonction des corrections trouvées
- Les incidents et modifications des actions par rapport aux corrections envisagées.

![mon image](./themes/mon-theme-pelican/static/images/AMAphp/ticket_framagit.png)

Suite à la création de ce ticket, on devait implémenter le code de la solution envisagée dans le ticket framagit, puis pousser la modification sur la forge logicielle sur une branche distincte à la résolution du ticket.

#### Environnement technologique

Ces différents tickets devaient être créé à partir de

- Gitlab-CE et expliquer avec précision l'incident rencontré et l'analyse de résolution du problème avant de commencer le code
- Sur une branche du dépôt spécifique au ticket résolu

Utilisation de :

- PHP
- IDE NetBeans
- Frameword Symfony
- GNU/Linux Debian

#### Compétences mobilisé

Cette mission a demandé la mobilisation des compétences suivantes :

- **B1.1.2 Exploiter des référentiels, normes et standards adoptés par le prestataire informatique**
- (Acquis par l'apprentissage et l'utilisation du framework symfony).
- **B1.2.3 Traiter des demandes concernant les applications**
- (encore en cours d'acquisition, mais un commencement de l'acquisition par le traitement des rapports d'incident utilisateurs).
- **B1.6.2 Mettre en œuvre des outils et stratégies de veille informationnelle**
- 