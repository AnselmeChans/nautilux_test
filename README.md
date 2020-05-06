

# *Plateforme d'intervention*

Mise en place d'une interface permettant de gérer des interventions


### Construit avec : 

* Django/Django Rest Framework pour le Back-End
* AngularJs - Framework web pour le Front-End(application web)
* SQlite3 (base de données)


### Installation

Il est nécessaire de bien suivre les étapes d'installation de l'application qui vont suivre : 

#### Activer votre environnement virtuel

```bash
source  tutorial-env/bin/activate

```

#### Installer les libraries nécéssaire au fonctionement de l'application

```bash
cd requirements
pip install -r base.txt
```

#### Effectuer les migrations de la base de données

```bash
python manage.py makemigrations
python manage.py migrate
```


#### Lancer l'application

```bash
python manage.py runserver
```

#### Accéder à l'application

Aller dans votre navigateur web et tapé addresse suivante : http://127.0.0.1:8000/


#### Sortir de son environement de travail 

```bash
deactivate
```

## Autheur

* **Hans CERIL** - [PurpleBooth](https://github.com/AnselmeChans/nautilux_test)


