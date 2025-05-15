// Function to handle car rental form submission
function handleRentalForm(event) {
  event.preventDefault();
  const form = event.target;
  const formData = new FormData(form);

  fetch(form.action, {
    method: "POST",
    body: formData,
    headers: {
      "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
    },
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        alert("Car rented successfully!");
        window.location.href = "/cars/";
      } else {
        alert(data.error || "An error occurred. Please try again.");
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      alert("An error occurred. Please try again.");
    });
}

// Function to handle contact form submission
function handleContactForm(event) {
  event.preventDefault();
  const form = event.target;
  const formData = new FormData(form);

  fetch(form.action, {
    method: "POST",
    body: formData,
    headers: {
      "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
    },
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        alert("Your message has been sent successfully!");
        // Clear all form inputs
        form.reset();
        // Just to make sure, also clear all inputs and textarea explicitly
        form.querySelectorAll("input, textarea").forEach((input) => {
          input.value = "";
        });
      } else {
        alert(data.error || "An error occurred. Please try again.");
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      alert("An error occurred. Please try again.");
    });
}

// Function to handle login form submission
function handleLoginForm(event) {
  event.preventDefault();
  const form = event.target;
  const formData = new FormData(form);

  fetch(form.action, {
    method: "POST",
    body: formData,
    headers: {
      "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
    },
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        window.location.href = "/";
      } else {
        alert(data.error || "Invalid username or password.");
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      alert("An error occurred. Please try again.");
    });
}

// Function to handle signup form submission
function handleSignupForm(event) {
  event.preventDefault();
  const form = event.target;
  const formData = new FormData(form);

  fetch(form.action, {
    method: "POST",
    body: formData,
    headers: {
      "X-CSRFToken": document.querySelector("[name=csrfmiddlewaretoken]").value,
    },
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.success) {
        alert("Account created successfully! Please login.");
        window.location.href = "/login/";
      } else {
        alert(data.error || "An error occurred. Please try again.");
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      alert("An error occurred. Please try again.");
    });
}

// Add event listeners when the DOM is loaded
document.addEventListener("DOMContentLoaded", function () {
  // Add form submission handlers
  const rentalForm = document.querySelector("#rentalForm");
  if (rentalForm) {
    rentalForm.addEventListener("submit", handleRentalForm);
  }

  const contactForm = document.querySelector("#contactForm");
  if (contactForm) {
    contactForm.addEventListener("submit", handleContactForm);
  }

  const loginForm = document.querySelector("#loginForm");
  if (loginForm) {
    loginForm.addEventListener("submit", handleLoginForm);
  }

  const signupForm = document.querySelector("#signupForm");
  if (signupForm) {
    signupForm.addEventListener("submit", handleSignupForm);
  }
});
