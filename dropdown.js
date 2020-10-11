document.addEventListener("DOMContentLoaded", function () {
    let dropdowns = document.getElementsByClassName("dropdown");

    for (let index = 0; index < dropdowns.length; index++) {
        let dropdown = dropdowns[index];

        let click = dropdown.querySelector('.click_to_open');
        let dropdownContent = dropdown.querySelector('.dropdown_content');

        click.onclick = function () {
            let isOpen = dropdownContent.getAttribute("data-open");
            if (isOpen == "false" || isOpen === null || isOpen === undefined) {
                dropdownContent.style.display = "block";
                dropdownContent.setAttribute("data-open", true);
            } else {
                dropdownContent.style.display = "none";
                dropdownContent.setAttribute("data-open", false);
            }
        }
    }
})