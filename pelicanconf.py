#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime, date, time, timedelta

AUTHOR = 'Gros Damien'
SITENAME = 'ePortfolio Gros Damien'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'public'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/mon-theme-pelican'
THEME_STATIC_DIR = 'themes/mon-theme-pelican/static'
CSS_FILE = 'style.css'

# SITUATION = 'Étudiant en BTS SIO option SLAM'
SITUATION = "Technicien applicatif intéropérabilité"

MENU = (
	('#presentation', 'Accueil'),
        ('#mes_competences', 'Mes compétences'),
        ('#realisations', 'Mes contribution / réalisations professionnelles'),
	('#a_propos', 'À Propos'),
	('#bas', 'Contact'),
        )

TITRE_COMPETENCES = 'Mes compétences'

NUM_COMPETENCE = ('competence1.1', 'competence1.2', 'competence1.3', 'competence1.4', 'competence1.5', 'competence1.6' )


COMPETENCES = (
    (
        'B1.1 : Gérer le patrimoine informatique',
        ('B1.1.1 Recenser et identifier les ressources numériques. (acquisition : 3/5)',
        'B1.1.2 Exploiter des référentiels, normes et standards adoptés par le prestataire informatique (acquisition : 3/5)')
    ),
    
    (
        'B1.2 : Répondre aux incidents et aux demandes d’assistance et d’évolution',
        ('B1.2.1 Collecter, suivre et orienter des demandes (acquisition : /5)',
        'B.1.2.2 Traiter des demandes concernant les services réseau et système, applicatifs',
        'B1.2.3 Traiter des demandes concernant les applications (acquisition : /5)')
    ),
    
    (
        ('B1.3 : Développer la présence en ligne de l’organisation'),
        ('B1.3.1 : Participer à la valorisation de l’image de l’organisation sur les médias numériques en tenant compte du cadre juridique et des enjeux économiques. (acquisition : /5)',
         'B1.3.3 : Participer à l’évolution d’un site Web exploitant les données de l’organisation. (acquisition : /5)')
    ),
    
    (
        ('B1.4 : Travailler en mode projet'),
        ('B1.4.1 Analyser les objectifs et les modalités d’organisation d’un projet (acquisition : /5)',
        'B1.4.2 Planifier les activités (acquis)',
        'B1.4.3 Évaluer les indicateurs de suivi d’un projet et analyser les écarts (acquisition : /5)',)
    ),

    (
        ('B1.5 : Mettre à disposition des utilisateurs un service informatique'),
        ('B1.5.1 Réaliser les tests d’intégration et d’acceptation d’un service (acquisition : /5)',
        'B1.5.2 Déployer un service (acquisition : /5)',
        'B1.5.3 Accompagner les utilisateurs dans la mise en place d’un service (acquisition : /5)')
    ),
        
    (
        ('B1.6 : Organiser son développement professionnel'),
        ('B1.6.1 Mettre en place son environnement d’apprentissage personnel (acquisition : /5)',
        'B.1.6.2 Mettre en œuvre des outils et stratégie de veille informationnelle',
        'B1.6.3 Gérer son identité professionnelle (acquisition : /5)',
        'B1.6.4 Développer son projet professionnel (acquisition : /5)')
    )
)
        
TITRE_REALISATION = 'Réalisations professionnelles'

naissance = date(2003, 5, 30)
aujourdhui = date.today()

# Calcul de l'âge en années (précis, tient compte du mois/jour)
age = aujourdhui.year - naissance.year - (
    (aujourdhui.month, aujourdhui.day) < (naissance.month, naissance.day)
)

POSTE = 'Technicien applicatif et intéropérabilité pour la société NEXUS/FRANCE à bellerive-sur-allier.'

SOCIETE = ''

CURSUS = 'Avant cela j\'ai obtenu un BAC STI2D option SIN qui nous a formé à du C++ (Arduino) et à quelques notions de PHP, qui m\'a par la suite orienté sur un BTS SIO option SLAM (Solution logiciel etapplication métier), qui m\a donc formé au au postes de developpeur métier avec dans le cursus la formation au développement Web (frameworks Symfony et Django / Front-End avec le framework Bootstrap. Mais également au développement d\'application multi-plateformes (JavaFX), d\'applications mobiles Android et sur l\'analyse et l\'administration des bases de données. Ce BTS, comportait une deuxieme spécialités orienté réseaux donc nosu avons également eu une formation commune.'

TEXT_A_PROPOS = (
        'Bonjour, je m\'appelle GROS Damien je suis née en 2003 j\'ai donc ' + str(age) +' ans et je suis actuellement' + POSTE+'.',
        CURSUS,
	    'Dans la vie je m\'intéresse à beaucoup de chose différente, je suis de nature plutôt curieuse mais avant tout j\'aime le volley et les jeux vidéos',
        'bienvenu à vous dans ce portfolio qui témoigne de ma progression dans ma vie étudiante ainsi que professionnel.'
         )
CONTACT = (
        'Mail : Dgros398@protonmail.com',
        'Tél : 06.52.33.18.03',
        'Courrier : 6 Rue de beauséjour,03200 Vichy',
        )

ENTREPRISE = (
        'Lycée général et technologique Albert Londres,',
        'Bd du 8 mai 1945, 03300 Cusset',
        )

# a modifier