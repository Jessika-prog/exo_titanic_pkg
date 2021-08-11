
const btn = document.getElementById('test')


btn.addEventListener('click', (event)=> {
  var myForm = document.getElementById('titanicForm')
  var formData = new FormData(myForm)

  event.preventDefault()

  var request = new XMLHttpRequest();

  request.open("POST","http://127.0.0.1:8000/passenger_dict/");

  request.onreadystatechange = function () {
    if (this.readyState === request.DONE && this.status === 200) {
      var survie = JSON.parse(this.responseText)
      console.log(survie.result);
      if (survie.result === "No") {
        var newDiv = document.createElement('div')
        var newChild = document.createTextNode('You will not survive!!')
        newDiv.appendChild(newChild)

        document.body.insertBefore(newDiv, myForm)
      }else if(survie.result === "Yes") {
        var newDiv = document.createElement('div')
        var newChild = document.createTextNode('You will survive!!')
        newDiv.appendChild(newChild)

        document.body.insertBefore(newDiv, myForm)
      }
    }}
  request.send(formData);
})
