function Couleur() 
{
  let red = Number(document.getElementById("R").value);
  let hexR = red.toString(16);
  console.log(hexR);
  let green = Number(document.getElementById("V").value);
  let hexV = green.toString(16);
  console.log(hexV);
  let blue = Number(document.getElementById("B").value);
  let hexB = blue.toString(16);
  console.log(hexB);
  let couleur = '#' + hexR + hexV + hexB;
  console.log(couleur);
  document.body.style.backgroundColor = couleur;
}
