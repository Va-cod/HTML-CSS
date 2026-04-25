// Wait until the DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {

    // 1. Show welcome message when the page loads
    alert("Welcome to my portfolio! 👋");

    // 3. Button to show/hide projects
    const projectsList = document.querySelector("#projects ul");

    const toggleBtn = document.createElement("button");
    toggleBtn.textContent = "Show/Hide projects";
    toggleBtn.style.display = "block";
    toggleBtn.style.marginBottom = "10px";

    projectsList.parentElement.insertBefore(toggleBtn, projectsList);

    toggleBtn.addEventListener("click", () => {
        if (projectsList.style.display === "none") {
            projectsList.style.display = "block";
        } else {
            projectsList.style.display = "none";
        }
    });

});