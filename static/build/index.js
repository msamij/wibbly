(()=>{var n=document.querySelector(".header__profile-menu"),t=document.querySelector(".popup-signup-menu"),e=document.querySelector(".overlay");n.addEventListener("click",function(i){(i.target.closest(".btn-signup")||i.target.closest(".btn-login"))&&(t.style.opacity="1",t.style.visibility="visible",e.style.visibility="visible",e.style.opacity="1")});e.addEventListener("click",function(i){t.style.opacity="0",t.style.visibility="hidden",e.style.visibility="hidden",e.style.opacity="0"});})();
