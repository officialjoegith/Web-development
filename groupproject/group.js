/*var abs = document.getElementById("present").value;
var pas = document.getElementById("absent").value;*/

/*let gi = document.querySelector(".gi");
function register(){
    gi.style.display="block";
    }
    let button = document.getElementById("butt");
    let present= document.getElementById("present");

button.addEventListener("click", validation);
function validation(){

    let present= present.value;

} 
let click = getElementById('.present');
click.addEventListener("click", check)
function check(){
    
}

/*localStorage.setItem("ab", abs);
var abu = sessionStorage.getItem(about);
console.log();
localStorage.setItem("gi", JSON.stringify({present}));
location.replace('page2.html');*/


// Get the modal 
let butt_on = document.getElementById('infor');
let user = document.getElementById('info');
let use = document.getElementById('infr');
butt_on.addEventListener('click', check);
let admin = 'admin';
function check(){
    let info = user.value
    let infr = use.value
    if(infr == admin){
        alert('You are correct');
    } 
    else{
        alert("you are wrong")
    }
}
var modal = document.getElementById
('id01');

// When the user clicks anywhere


window.onclick = function(event) {
if (event.target == modal) {
 modal.style.display = "none";
}
}