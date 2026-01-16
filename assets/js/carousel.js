// assets/js/carousel.js

document.addEventListener('DOMContentLoaded', () => {
  const carousels = document.querySelectorAll('.card-carousel-container');
  if (!carousels.length) return;

  carousels.forEach(carousel => {
    const track = carousel.querySelector('.card-carousel-track');
    const slides = Array.from(track.children);
    const nextBtn = carousel.querySelector('.card-carousel-button.next');
    const prevBtn = carousel.querySelector('.card-carousel-button.prev');

    if (!track || !nextBtn || !prevBtn) return;

    // Calculate width of one item + gap
    const getScrollAmount = () => {
      const item = track.querySelector('.carousel-item');
      return item ? item.offsetWidth + 20 : 300; // 20px is the gap defined in CSS
    };

    const updateButtons = () => {
      const tolerance = 5; // Buffer for float calculations
      // Disable Prev if at start
      prevBtn.disabled = track.scrollLeft <= tolerance;
      // Disable Next if at end
      nextBtn.disabled = track.scrollLeft + track.clientWidth >= track.scrollWidth - tolerance;
    };

    nextBtn.addEventListener('click', () => {
      track.scrollBy({ left: getScrollAmount(), behavior: 'smooth' });
    });

    prevBtn.addEventListener('click', () => {
      track.scrollBy({ left: -getScrollAmount(), behavior: 'smooth' });
    });

    // Update buttons on scroll (handles manual scroll/swipe)
    track.addEventListener('scroll', updateButtons);
    window.addEventListener('resize', updateButtons);

    // Initial check
    updateButtons();
  });
});
