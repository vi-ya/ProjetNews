// Select HTML element with scroll-top ID
let buttonTop = document.querySelector("#scroll-top");

// when the user clicks on the button, the page returns to the top.
buttonTop.addEventListener("click", () => {
   // Back to top of page when button is clicked
   window.scrollTo({
      // Target the top of the page.
      top: 0,  
      // fluid scrolling effect.
      behavior: "smooth"
   });
});

// Show button only when user has scrolled down.
document.addEventListener("scroll", () => {
//  Measures the vertical distance from the top of the page.   
//    Used by most modern browsers // in some older browsers.
let scrollButton = document.documentElement.scrollTop || document.body.scrollTop;
   // If the user has scrolled more than 50 pixels, the button becomes visible.
   if (scrollButton > 150 ) buttonTop.style.display = "block";
   else buttonTop.style.display = "none";
});