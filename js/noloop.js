const myImage = document.getElementById("my-image");

myImage.addEventListener("load", function() {
  myImage.setAttribute("loop", "1");
  myImage.addEventListener("click", function() {
    myImage.removeAttribute("loop");
  });
});