
document.addEventListener("DOMContentLoaded", function () {
    
    // ==========================================
    // LOGIC 1: ĐIỀU KHIỂN HERO BANNER (VÒNG LẶP 4 SLIDE)
    // ==========================================
    const slides = document.querySelectorAll(".hero-slide");
    const dots = document.querySelectorAll(".custom-dot");
    let currentSlideIndex = 0;
    const totalSlides = slides.length; // Sẽ tự động lấy ra 4 slide

    function nextHeroSlide() {
        if (totalSlides === 0) return;

        // Xóa class active ở slide và chấm tròn hiện tại
        slides[currentSlideIndex].classList.remove("active");
        if (dots[currentSlideIndex]) dots[currentSlideIndex].classList.remove("active");

        // Tăng index lên 1, nếu vượt quá ảnh 4 (index 3) thì tự quay về ảnh 1 (index 0)
        currentSlideIndex = (currentSlideIndex + 1) % totalSlides;

        // Thêm class active cho slide và chấm tròn kế tiếp
        slides[currentSlideIndex].classList.add("active");
        if (dots[currentSlideIndex]) dots[currentSlideIndex].classList.add("active");
    }

    // Tự động chuyển Banner sau mỗi 4 giây (4000ms)
    setInterval(nextHeroSlide, 4000);


    // ==========================================
    // LOGIC 2: ĐIỀU KHIỂN KHỐI SÁCH MỚI (XOAY VÒNG ẢNH)
    // ==========================================
    const bookImages = [
        "https://unsplash.com", 
        "https://unsplash.com", 
        "https://unsplash.com", 
        "https://unsplash.com"  
    ];
    
    let currentBookIndex = 0;
    
    const mainBookImg = document.querySelector(".custom-book-center img");
    const leftBookImg = document.querySelector(".custom-book-slider-height .start-0");
    const rightBookImg = document.querySelector(".custom-book-slider-height .end-0");

    function rotateBooks() {
        if (!mainBookImg || !leftBookImg || !rightBookImg) return;

        currentBookIndex = (currentBookIndex + 1) % bookImages.length;
        
        let leftIndex = (currentBookIndex - 1 + bookImages.length) % bookImages.length;
        let rightIndex = (currentBookIndex + 1) % bookImages.length;

        mainBookImg.src = bookImages[currentBookIndex];
        leftBookImg.src = bookImages[leftIndex];
        rightBookImg.src = bookImages[rightIndex];
    }

    // Tự động hoán đổi sách sau mỗi 3 giây (3000ms)
    setInterval(rotateBooks, 3000);
});
document.addEventListener("DOMContentLoaded", function () {
    // 1. Mảng danh sách các bức ảnh bìa sách trong project của bạn
    const bookImages = [
        "/img/new-b-1.webp",
        "/img/new-b-2.webp",
        "/img/new-b-3.webp",
        "/img/new-b-4.webp",
        "/img/new-b-5.webp",
        "/img/new-b-6.webp"
    ];

    const track = document.getElementById("booksTrack");
    if (!track) return;

    // Nhân đôi mảng gốc để dải trượt liên tục nối liền không điểm dừng
    const initialList = [...bookImages, ...bookImages];

    // 2. Tự động tạo cấu trúc thẻ ảnh HTML ban đầu
    initialList.forEach((src, index) => {
        const img = document.createElement("img");
        img.src = src;
        img.className = "book-item";
        img.alt = `Book ${index + 1}`;
        track.appendChild(img);
    });

    let isTransitioning = false;

    // 3. Thuật toán quét tọa độ hình học thực tế để tìm chính xác cuốn nằm giữa khung nhìn
    function formatCenterBook() {
        const currentBooks = track.querySelectorAll(".book-item");
        currentBooks.forEach(book => book.classList.remove("center-book"));
        
        const wrapper = track.parentElement;
        const wrapperCenter = wrapper.getBoundingClientRect().left + (wrapper.offsetWidth / 2);

        let closestBook = null;
        let minDistance = Infinity;

        currentBooks.forEach(book => {
            const bookRect = book.getBoundingClientRect();
            const bookCenter = bookRect.left + (bookRect.width / 2);
            const distance = Math.abs(wrapperCenter - bookCenter);

            if (distance < minDistance) {
                minDistance = distance;
                closestBook = book;
            }
        });

        // Kích hoạt class phóng to đè lớp cho cuốn trúng tâm hình học
        if (closestBook) {
            closestBook.classList.add("center-book");
        }
    }

    // 4. Hàm điều khiển trượt tịnh tiến liền kề vô tận
    function moveNext() {
        if (isTransitioning) return;
        isTransitioning = true;

        // Xóa class phóng to trước khi trượt để dải sách phẳng phẳng di chuyển mượt
        const currentBooks = track.querySelectorAll(".book-item");
        currentBooks.forEach(book => book.classList.remove("center-book"));

        // Thực hiện kéo dải sách trượt sang bên trái một bước trượt bằng chiều rộng ảnh sườn phẳng
        track.style.transition = "transform 0.5s ease-in-out";
        track.style.transform = "translateX(-42px)"; 

        // Chờ hiệu ứng trượt 0.5 giây hoàn tất
        setTimeout(() => {
            // Tắt animation chuyển động để tráo đổi DOM ngầm (0 giây)
            track.style.transition = "none"; 
            track.style.transform = "translateX(0)"; // Trả thanh ray về tọa độ gốc

            // Bốc phần tử ảnh đầu tiên bên trái chèn nối đuôi vào sau điểm cuối để tạo vòng lặp vô tận
            const firstBook = track.querySelector(".book-item");
            track.appendChild(firstBook);

            // ĐÁP ỨNG YÊU CẦU: Trượt xong, dừng lại phẳng lỳ ➔ Chờ đúng 1 giây (1000ms) rồi mới phóng ảnh ra
            setTimeout(() => {
                formatCenterBook(); 
                isTransitioning = false;
            }, 1000);

        }, 500); 
    }

    // Khởi tạo trạng thái phóng to cuốn ở giữa ban đầu khi vừa mở trang
    setTimeout(formatCenterBook, 200);

    // Kích hoạt vòng lặp tự động chạy vô hạn (4 giây một chu kỳ)
    setInterval(moveNext, 4000);
});

document.addEventListener("DOMContentLoaded", function () {
    // 1. Lấy đường dẫn (URL) hiện tại của trình duyệt (ví dụ: /tin-tuc hoặc /gioi-thieu)
    const currentPath = window.location.pathname;

    // 2. Tìm tất cả các thẻ liên kết menu trong thanh Navbar đỉnh
    const navLinks = document.querySelectorAll(".navbar-top-custom .navbar-nav .nav-link");

    // Lờ đi việc kiểm tra nếu không tìm thấy link nào
    if (navLinks.length === 0) return;

    // Trước hết, xóa tạm thời class active mặc định đang cắm cứng ở HTML để JS tự xử lý
    navLinks.forEach(link => link.classList.remove("active"));

    let isMatched = false;

    // 3. Duyệt qua từng link để đối chiếu đường dẫn
    navLinks.forEach(link => {
        const linkPath = link.getAttribute("href");

        // Nếu đường dẫn của link khớp với URL hiện tại trên trình duyệt
        if (linkPath && currentPath.endsWith(linkPath) && linkPath !== "#" && linkPath !== "/") {
            link.classList.add("active");
            isMatched = true;
        }
    });

    // 4. Trường hợp đặc biệt: Nếu là trang chủ hoặc không khớp mục nào, tự động active nút đầu tiên
    if (!isMatched && navLinks.length > 0) {
        navLinks[0].classList.add("active");
    }
});

