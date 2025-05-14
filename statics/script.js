document.addEventListener("DOMContentLoaded", () => {
  const dropdowns = document.querySelectorAll(".nav-item.dropdown");

  dropdowns.forEach((dropdown) => {
    const dropdownMenu = dropdown.querySelector(".dropdown-menu");
    let isInside = false;

    dropdown.addEventListener("mouseenter", () => {
      dropdown.classList.add("show");
      dropdownMenu.classList.add("show");
    });

    dropdown.addEventListener("mouseleave", () => {
      setTimeout(() => {
        if (!isInside) {
          dropdown.classList.remove("show");
          dropdownMenu.classList.remove("show");
        }
      }, 150);
    });

    dropdownMenu.addEventListener("mouseenter", () => {
      isInside = true;
      dropdown.classList.add("show");
      dropdownMenu.classList.add("show");
    });

    dropdownMenu.addEventListener("mouseleave", () => {
      isInside = false;
      dropdown.classList.remove("show");
      dropdownMenu.classList.remove("show");
    });

    // Close dropdown on click outside
    document.addEventListener("click", (event) => {
      if (!dropdown.contains(event.target)) {
        dropdown.classList.remove("show");
        dropdownMenu.classList.remove("show");
      }
    });
  });
});

let position = 0;

function moveSlider(direction) {
  const slider = document.querySelector('.slider');
  const cardWidth = document.querySelector('.card').offsetWidth + 20; // card width + margin
  const totalCards = document.querySelectorAll('.card').length;
  const visibleCards = 4;

  position += direction;

  // Clamp the position to stay within the valid range
  const maxPosition = totalCards - visibleCards;
  if (position < 0) position = 0;
  if (position > maxPosition) position = maxPosition;

  // Apply the translate to shift the slider
  slider.style.transform = `translateX(-${position * cardWidth}px)`;
}



