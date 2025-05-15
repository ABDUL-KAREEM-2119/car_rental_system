document.addEventListener("DOMContentLoaded", function () {
  const modal = document.getElementById("carModal");
  const addButton = document.querySelector(".add-car-btn");
  const closeButton = document.querySelector(".close");
  const form = document.getElementById("carForm");

  if (addButton) {
    addButton.addEventListener("click", openAddCarModal);
  }

  if (closeButton) {
    closeButton.addEventListener("click", closeModal);
  }

  if (form) {
    form.addEventListener("submit", handleFormSubmit);
  }

  // Close modal when clicking outside
  window.addEventListener("click", function (event) {
    if (event.target === modal) {
      closeModal();
    }
  });
});

function openAddCarModal() {
  const modal = document.getElementById("carModal");
  modal.style.display = "block";
}

function closeModal() {
  const modal = document.getElementById("carModal");
  modal.style.display = "none";
}

function handleFormSubmit(event) {
  event.preventDefault();
  // Add your form submission logic here
  // You can use fetch or form submission
}
