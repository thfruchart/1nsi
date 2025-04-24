function Couleur() 
{
  
  let rouge = Number(document.getElementById("rouge").value);
  let hexaRouge = rouge.toString(16);
  console.log(hexaRouge);
  
  let vert = Number(document.getElementById("vert").value);
  let hexaVert = vert.toString(16);
  console.log(hexaVert);
  
  let bleu = Number(document.getElementById("bleu").value);
  let hexaBleu = bleu.toString(16);
  console.log(hexaBleu);
  
  
  let couleur = '#'+hexaRouge+hexaVert+hexaBleu;
  console.log(couleur);
  document.body.style.backgroundColor = couleur;
}
