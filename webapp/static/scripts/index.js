// Extract loading element
const loadingBackground = document.getElementById("loading-background");

// Extract submit button
const getButton = document.getElementById("button");

getButton.addEventListener("click", function () {
  loadingBackground.style.display = "flex";
});
