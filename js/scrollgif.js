const gif = document.querySelector('.gif');

function playGif() {
  const rect = gif.getBoundingClientRect();
  if (rect.top >= 0 && rect.bottom <= window.innerHeight) {
    gif.src = gif.src;
    window.removeEventListener('scroll', playGif);
  }
}

window.addEventListener('scroll', playGif);
