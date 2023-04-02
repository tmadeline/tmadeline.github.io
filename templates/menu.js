const menuButton = document.getElementById('header-mobile__menu-toggle');
const menu = document.getElementById('header-mobile__menu');

// Function to toggle the menu
function toggleMenu() {
  menu.classList.toggle('show');
  // Check if menu is open
  if (menu.classList.contains('show')) {
    // Replace menu icon with animation
    menuButton.innerHTML = '<img src="hamxin.gif" alt="Menu">';
    // Wait for animation to finish and replace with icon
    setTimeout(function() {
      menuButton.innerHTML = '<img src="hamburger.png" alt="Menu">';
    }, 1000);
  } else {
    // Replace menu icon with animation
    menuButton.innerHTML = '<img src="hamxout.gif" alt="Menu">';
    // Wait for animation to finish and replace with icon
    setTimeout(function() {
      menuButton.innerHTML = '<img src="hamburger.png" alt="Menu">';
    }, 1000);
  }
}

// Add event listener to menu button
menuButton.addEventListener('click', toggleMenu);
