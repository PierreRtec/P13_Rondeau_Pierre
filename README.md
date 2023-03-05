## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure
- Docker (Docker Desktop si vous êtes sous Windows)

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/PierreRtec/P13_Rondeau_Pierre.git`

#### Créer l'environnement virtuel

- `cd './P13_Rondeau_Pierre/'`
- Installer les dépendances `pipenv install`
- Activer l'environnement `pipenv shell`

#### Exécuter le site localement

- ouvrir un terminal depuis la racine du projet (au même niveau que le Dockerfile)
- construire l'image Docker "p13_oc_lettings_site" `docker build -t p13_oc_lettings_site .`
- lancer Docker en local `docker run -p 8000:8000 -e WEB_CONCURRENCY=1 -e PORT=8000 p13_oc_lettings_site`
- Ctrl+click : `http://localhost:8000`
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd ./P13_Rondeau_Pierre/`
- `isort .`
- `flake8 .`
- `black .`

#### Tests unitaires

##### Tests oc_lettings_site :

- `cd ./P13_Rondeau_Pierre/`

- `py -m oc_lettings_site.manage test oc_lettings_site.oc_lettings_site.tests_oc_lettings_site.test_oc_lettings_site_views`

##### Tests lettings app :

- `py -m oc_lettings_site.manage test oc_lettings_site.lettings.tests_lettings.test_lettings_views`

##### Tests profiles app :

- `py -m oc_lettings_site.manage test oc_lettings_site.profiles.tests_profiles.test_profiles_views`

#### Base de données

- `cd ./P13_Rondeau_Pierre/oc_lettings_site/`
- check avec "ls" ou "dir" si la base de données 'oc-lettings-site.sqlite3' est bien présente 
- Jouer la commande `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `PRAGMA table_info(profiles_profile);`
- Lancer une requête sur la table des profils, `SELECT user_id, favorite_city FROM profiles_profile WHERE favorite_city LIKE 'B%';`
- `.quit` pour quitter OU Ctrl+C

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

---


### CircleCI

Nous avons un fichier de configuration YML pour configurer la pipeline CircleCI. Voici une brève documentation pour chacun des éléments du fichier `config.yml` :

- '**version: 2.1**' : Indique la version de la configuration de CircleCI utilisée.

- '**jobs**' : Définit une liste de travaux à exécuter.

- '**build**' : Définit le nom du build. Ce build utilise une image Docker "circleci/python:3.9-buster-node-browsers-legacy" et exécute plusieurs étapes.

- '**steps**' : Définit une liste d'étapes pour exécuter le travail de construction (build).

- '**checkout**' : Clone le dépôt Git actuel pour accéder au code source.

- '**setup_remote_docker**' : Installe et configure Docker pour exécuter des images Docker.

- '**run**' : Permet d'exécuter une commande avec un nom donné.

- '**Install dependencies and Linting**' : Installe les dépendances Python nécessaires pour exécuter l'application et effectue des vérifications de code avec -> isort, flake8 et black.

- '**Testing**' : Exécute des tests unitaires avec le code de l'application.

- '**Heroku API Key and App creation**' : Installe l'interface en ligne de commande Heroku, crée une clé d'API Heroku, ajoute les buildpacks requis et crée une nouvelle application Heroku.

- '**Docker Auth, Build and Push to Heroku**' : Connecte Docker à l'API Heroku, construit et pousse une image Docker de l'application sur Heroku, puis lance l'application.

Pour améliorer cette configuration, nous pourrions envisager l'utilisation d'orbs CircleCI pour simplifier la 
configuration et la gestion de "secrets". Nous pourrions également ajouter des méthodes de confidentialité supplémentaires 
pour notre application Django en utilisant des solutions telles que "Hashicorp Vault" pour stocker et gérer les secrets 
de l'application. Il faudrait donc envisager une nouvelle version de l'application encore plus sécurisée. Mais nous pourrions
également envisager l'utilisation de workers en parallèle. Ce qui permettrait d'obtenir de meilleures performances de déploiement et de livraison continue.
