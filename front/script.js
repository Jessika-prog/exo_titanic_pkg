
const btn = document.getElementById('predire')
const closing = document.getElementById('close')


btn.addEventListener('click', () => {
  // Récupération des données du formulaire
  var myForm = document.getElementById('titanicForm')
  var formData = new FormData(myForm)

  var request = new XMLHttpRequest();
// envoie des données à l'api
  request.open("POST", "https://titanicdeadoralive.azurewebsites.net/passenger_dict/");

  request.onreadystatechange = function () {
// attente de réponse de l'api puis choix de l'action en fonction de la réponse
    if (this.readyState === request.DONE && this.status === 200) {
      var survie = JSON.parse(this.responseText)
      console.log(survie.result);

      var img = document.createElement("img");
      var answer = document.createElement("p");
      if (survie.result === "No") {
        answer.innerHTML = "Vous n'auriez pas survécu 😔"
        img.src = "front/Jack.jpg";
      } else if (survie.result === "Yes") {
        answer.innerHTML = "Vous auriez survécu 🎉"
        img.src = "front/Rose.jpg";
      }
      var modal = document.getElementById("resultat");
      modal.classList.remove('hidden')
      var photo = document.getElementById('photoResultat');
      photo.appendChild(answer);
      photo.appendChild(img);
    }
  }
  request.send(formData);
})


closing.addEventListener('click', () => {
  var photo = document.getElementById('photoResultat');
  while (photo.hasChildNodes()) {
    photo.removeChild(photo.firstChild);
  }
})
