## Gestion des paramètres avec JavaScript
Habituellement, les paramètres sont gérés côté SERVEUR, avec PHP.

Ici, on va faire le même type de traitement, en javascript.
1. Copier le contenu des fichiers [form.html](form.html) et [cible.html](cible.html) dans un éditeur de texte, par exemple Notepad++.
2. Ouvrir ces deux fichiers dans un navigateur.
3. Ouvrir la console javascript dans les outils de développement F12
4. Tester `cible.html?valeur1=abc&valeur2=xyz`

#### Exercice
Modifier le formulaire et le fichier cible de telle sorte que :
* l'utilisateur puisse saisir deux valeurs dans le formulaire
* puis cliquer sur le bouton
* et obtenir une page dans laquelle :
  * un clic sur le titre "PREMIER" affiche la première valeur passée en paramètre
  * un clic sur le titre "SECOND" affiche la deuxième valeur passée en paramètre
