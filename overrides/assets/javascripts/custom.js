// Navigate to home when clicking the header title (same destination as the logo link)
document.addEventListener("DOMContentLoaded", () => {
  const title = document.querySelector(".md-header__title");
  const home = document.querySelector("a.md-header__button.md-logo");

  if (!title || !home) return;

  title.style.cursor = "pointer";
  title.addEventListener("click", () => {
    window.location.href = home.getAttribute("href");
  });
});