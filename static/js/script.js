const navbarShowBtn= document.querySelector('.navbar-show-btn');

const navbarCollapseDiv = document.querySelector('.navbar-collapse');

const navbarHidebtn = document.querySelector('.navbar-hide-btn');

navbarShowBtn.addEventListener('click' , function(){
   navbarCollapseDiv.classList.add("navbar-show");
}); 

navbarHidebtn.addEventListener('click' , function(){
    navbarCollapseDiv.classList.remove('navbar-show')
});

let resizeTimer;
window.addEventListener('resize' , ()=>{
    document.body.classList.add('resize-animation-stopper');
    clearTimeout(resizeTimer);
    resizeTimer=setTimeout(()=>{
        document.body.classList.remove('resize-animation-stopper');
    },400);
});


// login

function handlelogin(){
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;

    if(username==="admin" && password==="admin"){
        localStorage.setItem('isLoggedIn','true');
        window.location.href="/templates/home.html";
        
        
    }
    else{
        alert("Invalid username or password")
    }
}

// check user is logged in or not

const isLoggedIn = localStorage.getItem('isLoggedIn');
    
// Update the button based on the login state
updateLoginButton(isLoggedIn);

function toggleLogin() {
  // If the user is not logged in, open the login page
  if (!isLoggedIn) {
    window.location.href = "login.html";
  } else {
    // If the user is logged in, simulate a logout by removing the login state from localStorage
    localStorage.removeItem('isLoggedIn');

    // Update the button based on the new login state
    updateLoginButton(false);
  }
}

function updateLoginButton(isLoggedIn) {
  const loginButton = document.getElementById('loginButton');
  const doc_panel = document.getElementById('doc-panel');
  const doc_nav = document.getElementById('doc-nav');

  if (isLoggedIn) {
    loginButton.textContent = 'Logout';
    loginButton.onclick = toggleLogin;
  } else {
    doc_panel.style.display='none';
    doc_nav.style.display='none';
    loginButton.textContent = 'Login';
    loginButton.onclick = function() {
      window.location.href = "login.html";
    };
  }
}

// smooth scrolling

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener("click", function(e){
    e.preventDefault();
    document.querySelector(this.getAttribute("href")).scrollIntoView({
      behavior : "smooth"
    });
  });
});

   function checkAnswers() {
    var answers = document.querySelectorAll('input[type="radio"]:checked');
    if (answers.length !== 15) {
        alert("Please answer all the questions.");

    }
    window.location.href = "result.html";
}
