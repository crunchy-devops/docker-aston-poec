## EXERCICE 1
Creez un repo github nommé **docker-exe1**  
il doit etre public, avec un fichier README.md , un fichier  .gitignore valable pour le langage Python, une License MIT  
Faites un git clone dans votre directory project local   
mettre en place dans goland la connexion ssh vers votre VM   
attention a ne pas oublier le mapping sur le deployment path sur /home/ubuntu/docker-exe1  
Mettre les commandes de l'exercice suivant dans le fichier README.md  

Dans une commande docker run
* vous devez etre en interactif et avec un tty pour le display
* le container doit etre nommé **myalpes** 
* dans cette commande creer un volume /MountPoint
* image doit etre alpine
* passer la commande /bin/ash   
Ensuite a l'interieur du container  
* creer un fichier test.py
* et inserez le texte "WARNING: ret pointer is null"
---
* a partir de ce container créer une image nommée  myalpine:v12.
* Supprimer les metadata de cette image avec docker export et docker import 
* Verifier aavec docker history 
* mettez cette image dans docker hub sous votre compte docker hub

## EXERCICE 2
Creez un repo github nommé **docker-exe2**  
il doit etre public, avec un fichier README.md , un fichier  .gitignore valable pour le langage Python, une License MIT  
Faites un git clone dans votre directory project local   
mettre en place dans goland la connexion ssh vers votre VM   
attention a ne pas oublier le mapping sur le deployment path sur /home/ubuntu/docker-exe2  
Mettre les commandes de l'exercice suivant dans le fichier README.md

Creez un Dockerfile file dans votre projet sous Goland , qui contient  
comme image de base fabric8/tomcat-9 de tomcat 9  
copier le fichier webapp.war dans la directory  de tomcat /opt/tomcat/webapps  
faire un build d'image avec ce Dockerfile, l'image est nommée tomcat:v1  
Faire des recherches ( docker history, docker inspect) pour trouver le port utilisé par tomcat dans cette image
Faire un docker run pour creer un container a partir de l'image tomcat:v1, en background, avec le mapping de port   
20200: et le port de tomcat dans le container que vous avez trouvé  
Ouvrir votre navigateur et affiche la page d'accueil de l'application , copiez et collez le texte de cette page dans le fichier result.txt  
En utilisant portainer , allez a l'interieur du container et creer un utilisateur tomcat nommé logwire et passord: docker  
mettez cette image dans docker hub sous votre compte docker hub  


## EXERCICE 3
Creez une branche nommée **exercice3** dans votre repo github nommé **docker-exe2**  
Dans cette branche, creez un fichier docker-compose.yml a partir du fichier docker-compose.yml dans votre projet  
docker-aston-poec. 
Ce docker-compose.yml va demarre votre container tomcat 9 






