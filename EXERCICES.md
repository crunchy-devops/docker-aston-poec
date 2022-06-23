## EXERCICE 1
dans une commande docker run
* vous devez etre en interactif et avec un tty pour le display
* le container etre nommée **myalpes** 
* dans cette commande creer un volume /MountPoint
* passer la commande /bin/ash   
Ensuite a l'interieur du container  
* creer un fichier test.py
* et inserez le texte "WARNING: ret pointer is null"
---
* a partir de ce container créer une image nommée  myalpine:v12.

**Commandes à utiliser**:  docker run et docker commit 

## EXERCICE 2
Créer un fichier Dockerfile qui utilise l’image myalpine:v1, définir un volume /MountPoint dans ce dockerfile.  Créer une image avec ce dockerfile nommée test:v1.  
Lancer un container en tâche de fond en utilisant cette image avec un mapping de volume  
 -v /tmp/test:/MountPoint et la commande tail -f /dev/null    
Commandes à utiliser: docker build et docker run 

## EXERCICE 3
Enlever les metadata de l’image  test:v1. Vérifier avec docker history  
Commandes à utiliser: docker export , docker import  


## EXERCICE 4
Aller dans Docker Hub et voir comment lancer un container NGINX. Créer ou copier une page html de votre choix et faire le bind de volume pour afficher cette page html dans NGINX.   
Mapper le port du localhost(VM) en 22500 et le port 80 du container.   
Commandes à utiliser: docker pull, docker run   
