function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for(let i = 0; i <ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) == ' ') {
        c = c.substring(1);
      }
      if (c.indexOf(name) == 0) {
        return c.substring(name.length, c.length);
      }
    }
    return "";
  }




const sideMenu = document.querySelector("aside");
const themeToggler = document.querySelector(".theme-toggler");




// controlling night mode cookie

var night_mode = getCookie("night_mode");
if(night_mode == "1"){
    document.body.classList.toggle('dark-theme-variables');  
    themeToggler.querySelector('span:nth-child(1)').classList.toggle('active')
    themeToggler.querySelector('span:nth-child(2)').classList.toggle('active')
}
//night-light mode and set cookie
themeToggler.addEventListener('click', () => {
    if(night_mode == "0"){
        document.body.classList.toggle('dark-theme-variables');  
        themeToggler.querySelector('span:nth-child(1)').classList.toggle('active')
        themeToggler.querySelector('span:nth-child(2)').classList.toggle('active')
        document.cookie = "night_mode=1"
    }else{
        document.body.classList.toggle('dark-theme-variables');  
        themeToggler.querySelector('span:nth-child(1)').classList.toggle('active')
        themeToggler.querySelector('span:nth-child(2)').classList.toggle('active')
        document.cookie = "night_mode=0"
    }
})

