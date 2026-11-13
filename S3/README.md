# Types construits

## PARCOURS : types construits
* Parcours sans indice
  * [chaîne de caractère](https://pratique.forge.apps.education.fr/balayage/2-chaine/46-exclamations/)
  * [maximum d'une liste](https://pratique.forge.apps.education.fr/balayage/1-lecture_tab/06-maxi/)
  * [moyenne d'une liste](https://pratique.forge.apps.education.fr/balayage/1-lecture_tab/10-moyenne/)
 
## Type muables dans une fonction
- [une fonction peut modifier une valeur d'une liste](https://pythontutor.com/visualize.html#code=def%20f%28x%29%20%3A%20%0A%20%20%20%20L%5B0%5D%20%3D%20x%0A%20%20%20%20return%20L%0A%0AL%20%3D%20%5B10,20,30%5D%0A%0Aprint%28%20f%28100%29%20%29%0Aprint%28%20L%20%29&curInstr=8&mode=display&origin=opt-frontend.js&py=311)
- [une fonction ne peut pas RE-définir une liste](https://pythontutor.com/visualize.html#code=def%20f%28x%29%20%3A%20%0A%20%20%20%20L%20%3D%20%5Bx,%20x%2B1,%20x%2B2%5D%0A%20%20%20%20return%20L%0A%0AL%20%3D%20%5B10,20,30%5D%0A%0Aprint%28%20f%28100%29%20%29%0Aprint%28L%29&curInstr=8&mode=display&origin=opt-frontend.js&py=311)

### Des exercices pour s'entraîner sur pratique.forge.apps.education.fr
* [listes](https://pratique.forge.apps.education.fr/balayage/1-lecture_tab/)
  * [Soleil couchant](https://pratique.forge.apps.education.fr/balayage/1-lecture_tab/15-soleil_couchant/)
  * [Premier minimum local](https://pratique.forge.apps.education.fr/balayage/1-lecture_tab/16-premier_minimum/)
* [dictionnaires](https://pratique.forge.apps.education.fr/balayage/4-dico/32-dict_extremes/)
  * [CORRECTION : dictionnaire des valeurs extrêmes](32-dict_extremes-exo.py)
  * [CORRECTION : dictionnaire d'occurrences](45-dico_occurrences-exo.py)

### QCM
* [Entraînement : `list`](https://genumsi.inria.fr/qcm.php?h=bb1228ec37442a326e9c5682b62fe8a6)
* [Entraînement : `dict`](https://genumsi.inria.fr/qcm.php?h=cbb959459c8a953f46ea79e0c939647e)
* [EVAL LIST-TUPLE-DICT](https://genumsi.inria.fr/qcm.php?h=e79034e09e84584ff2d87685cb6039c1)
