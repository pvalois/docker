Usage : 

docker build . -t auditor
docker run d -rm -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker:/var/lib/docker:ro auditor 

Vous pouvez ensuite ouvrir un shell dans ce container et utiliser les outils python dans /root.
Ceux-ci peuvent lancer des commandes et inspecter les containers pour obtenir beaucoup d'infos. 

* get_containers_date.py

  Exécute la commande "date" sur tous les containers pour vérifier que tous es ok

* orphaned_overlays.py

  Liste les overlays presents dans /var/lib/docker/overlays2 et cherche les orphelins non rattachés à un container

