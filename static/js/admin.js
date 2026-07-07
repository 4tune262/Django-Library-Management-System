const menuToggle = document.getElementById("menuToggle");
const sidebar = document.getElementById("sidebar");
const overlay = document.getElementById("overlay");

const mainContent = document.querySelector(".main-content");
const navbar = document.querySelector(".top-navbar");

if (menuToggle && sidebar && overlay) {

    menuToggle.addEventListener("click", () => {

        // Mobile & Tablet
        if (window.innerWidth < 992) {

            sidebar.classList.toggle("show");
            overlay.classList.toggle("show");

        }
        // Desktop
        else {

            sidebar.classList.toggle("collapsed");
            mainContent.classList.toggle("expanded");
            navbar.classList.toggle("expanded");

        }

    });

    // Đóng bằng overlay
    overlay.addEventListener("click", () => {

        sidebar.classList.remove("show");
        overlay.classList.remove("show");

    });

    // Click menu trên mobile
    document.querySelectorAll(".sidebar-menu a").forEach(item => {

        item.addEventListener("click", () => {

            if (window.innerWidth < 992) {

                sidebar.classList.remove("show");
                overlay.classList.remove("show");

            }

        });

    });

    // Resize
    window.addEventListener("resize", () => {

        if (window.innerWidth < 992) {

            sidebar.classList.remove("collapsed");
            mainContent.classList.remove("expanded");
            navbar.classList.remove("expanded");

        } else {

            sidebar.classList.remove("show");
            overlay.classList.remove("show");

        }

    });

}

/* ===== SUBMENU ===== */

document.querySelectorAll(".menu-toggle").forEach(menu => {

    menu.addEventListener("click", function (e) {

        e.preventDefault();

        this.parentElement.classList.toggle("active");

    });

});
const currentPath = window.location.pathname;

document.querySelectorAll(".sidebar-menu a").forEach(link => {

    const href = link.getAttribute("href");

    let isActive = false;

    if (href === "/admin") {

        isActive =
            currentPath === "/admin" ||
            currentPath === "/admin/index";

    } else {

        isActive =
            currentPath === href ||
            currentPath.startsWith(href + "/");

    }

    if (isActive) {

        link.parentElement.classList.add("active");

        const parentSubmenu = link.closest(".has-submenu");

        if (parentSubmenu) {
            parentSubmenu.classList.add("active");
        }
    }

});


// ============================
// CATEGORY VALIDATOR
// ============================
document.querySelectorAll('form[data-validate="category"]').forEach(form => {

    console.log("CATEGORY FORM FOUND");

    const nameInput = form.querySelector(".category-name");
    const imageInput = form.querySelector(".category-image");

    const nameError = form.querySelector(".name-error");
    const imageError = form.querySelector(".image-error");

    const nameRegex = /^[\p{L}\p{N}\s]+$/u;
    const imageRegex = /\.(jpg|jpeg|png|webp|gif)$/i;

    form.addEventListener("submit", function (e) {

        let ok = true;

        const name = nameInput?.value.trim();
        const image = imageInput?.value.trim();

        // DEBUG
        console.log("SUBMIT:", name, image);

        // NAME CHECK
        if (!nameRegex.test(name)) {
            nameError.textContent = "Tên không được chứa ký tự đặc biệt";
            ok = false;
        } else {
            nameError.textContent = "";
        }

        // IMAGE CHECK
        if (!imageRegex.test(image)) {
            imageError.textContent = "Sai định dạng ảnh";
            ok = false;
        } else {
            imageError.textContent = "";
        }

        if (!ok) {
            e.preventDefault();
            console.log("BLOCKED FORM");
        }
    });

});
document.querySelectorAll('form[data-validate="book"]').forEach(form => {

    const name = form.querySelector(".book-name");
    const spec = form.querySelector(".book-specification");
    const image = form.querySelector(".book-image");
    const price = form.querySelector(".book-price");

    const errName = form.querySelector(".book-name-error");
    const errSpec = form.querySelector(".book-specification-error");
    const errImage = form.querySelector(".book-image-error");
    const errPrice = form.querySelector(".book-price-error");

    const textRegex = /^[\p{L}\p{N}\s]+$/u;
    const imageRegex = /\.(jpg|jpeg|png|webp|gif)$/i;
    const priceRegex = /^[0-9]+$/;

    form.addEventListener("submit", e => {

        let ok = true;

        // NAME
        if (!textRegex.test(name.value.trim())) {
            errName.textContent = "Tên không hợp lệ";
            ok = false;
        } else errName.textContent = "";

        // SPEC
        if (!textRegex.test(spec.value.trim())) {
            errSpec.textContent = "Mô tả không hợp lệ";
            ok = false;
        } else errSpec.textContent = "";

        // IMAGE
        if (!imageRegex.test(image.value.trim())) {
            errImage.textContent = "Ảnh phải .jpg .png .webp .jpeg";
            ok = false;
        } else errImage.textContent = "";

        // PRICE
        if (!priceRegex.test(price.value.trim())) {
            errPrice.textContent = "Giá chỉ được nhập số";
            ok = false;
        } else errPrice.textContent = "";

        if (!ok) e.preventDefault();
    });

});
// chọn category => tự submit
document.querySelectorAll('.category-checkbox')
    .forEach(item => {

        item.addEventListener('change', function () {

            document.getElementById('filterForm').submit();

        });

    });

// chuyển trang
document.querySelectorAll('.page-number')
    .forEach(item => {

        item.addEventListener('click', function (e) {

            e.preventDefault();

            const page = this.dataset.page;

            const form = document.getElementById('filterForm');

            let pageInput =
                form.querySelector('input[name="page"]');

            if (!pageInput) {

                pageInput =
                    document.createElement('input');

                pageInput.type = 'hidden';
                pageInput.name = 'page';

                form.appendChild(pageInput);

            }

            pageInput.value = page;

            form.submit();

        });

    });