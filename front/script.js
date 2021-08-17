
const btn = document.getElementById('predire')
const closing = document.getElementById('close')


btn.addEventListener('click', () => {
  var myForm = document.getElementById('titanicForm')
  var formData = new FormData(myForm)

  var request = new XMLHttpRequest();

  request.open("POST", "https://titanicdeadoralive.azurewebsites.net/passenger_dict/");

  request.onreadystatechange = function () {

    if (this.readyState === request.DONE && this.status === 200) {
      var survie = JSON.parse(this.responseText)
      console.log(survie.result);

      var img = document.createElement("img");
      if (survie.result === "No") {
        img.src = "front/Jack.jpg";
      } else if (survie.result === "Yes") {
        img.src = "front/Rose.jpg";
      }
      var modal = document.getElementById("resultat");
      modal.classList.remove('hidden')
      var photo = document.getElementById('photoResultat');
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

// document.addEventListener('keydown', logKey);

// function logKey(e) {
//   log.textContent += ` ${e.code}`;
// }
// closing.addEventListener('click', () => {

//   }
// EventTarget.addEventListener("keydown", event => {
//   console.log('test ok');
//   var photo = document.getElementById('photoResultat');
//   while (photo.hasChildNodes()) {
//     photo.removeChild(photo.firstChild);
//   }
// }
// )
