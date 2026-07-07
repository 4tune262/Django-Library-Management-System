// /*=========================
//         TIMER
// =========================*/
//
// let time = 60;
//
// const timer = document.getElementById("timer");
//
// if(timer){
//
//     const countdown = setInterval(function(){
//
//         time--;
//
//         timer.innerHTML = time;
//
//         if(time<=10){
//
//             timer.classList.add("timer-danger");
//
//         }
//
//         if(time<=0){
//
//             clearInterval(countdown);
//
//             alert("Hết thời gian!");
//
//             document.querySelector("form").submit();
//
//         }
//
//     },1000);
//
// }
//
// /*=========================
//         SCORE EFFECT
// =========================*/
//
// const score = document.getElementById("scoreText");
//
// if(score){
//
//     score.classList.add("score-add");
//
// }
//
// /*=========================
//         CHARACTER
// =========================*/
//
// const form=document.querySelector("form");
//
// if(form){
//
// form.addEventListener("submit",function(){
//
// const anime=document.getElementById("anime");
//
// anime.classList.add("correct");
//
// });
//
// }
//
// /*=========================
//         PARTICLE
// =========================*/
//
// setInterval(function(){
//
// const p=document.createElement("div");
//
// p.className="particle";
//
// p.style.left=Math.random()*100+"vw";
//
// p.style.animationDuration=
//
// 3+Math.random()*4+"s";
//
// document.body.appendChild(p);
//
// setTimeout(()=>{
//
// p.remove();
//
// },7000);
//
// },250);
//
// /*=========================
//         BUTTON EFFECT
// =========================*/
//
// document
//
// .querySelectorAll(".answer-btn")
//
// .forEach(function(btn){
//
// btn.onclick=function(){
//
// document
//
// .querySelectorAll(".answer-btn")
//
// .forEach(i=>{
//
// i.classList.remove("answer-correct");
//
// });
//
// this.classList.add("answer-correct");
//
// }
//
// });
//
// /*=========================
//         PROGRESS
// =========================*/
//
// const bar=document.getElementById("progressBar");
//
// if(bar){
//
// let width=0;
//
// const run=setInterval(function(){
//
// width++;
//
// bar.style.width=width+"%";
//
// if(width>=33){
//
// clearInterval(run);
//
// }
//
// },12);
//
// }
//
// /*=========================
//         RIPPLE
// =========================*/
//
// document
//
// .querySelectorAll(".btn-play")
//
// .forEach(btn=>{
//
// btn.addEventListener("mouseenter",()=>{
//
// btn.style.transform="scale(1.05)";
//
// });
//
// btn.addEventListener("mouseleave",()=>{
//
// btn.style.transform="scale(1)";
//
// });
//
// });
//
// /*=========================
//         FLOAT CHARACTER
// =========================*/
//
// const anime=document.getElementById("anime");
//
// if(anime){
//
// setInterval(()=>{
//
// anime.style.transform=
//
// "translateY("+
//
// (Math.sin(Date.now()/400)*8)
//
// +"px)";
//
// },20);
//
// }
/*======================================================
        C++ CODING ARENA - GAME.JS (CHỈNH SỬA CHUẨN LUỒNG)
=======================================================*/

/*=========================
        TIMER LOGIC
=========================*/
let time = 60;
const timerElement = document.getElementById("timer");

if (timerElement) {
    const countdown = setInterval(function() {
        time--;
        timerElement.innerHTML = time;

        // Nếu còn dưới 10 giây, đổi màu sang đỏ nhấp nháy (Class css của bạn)
        if (time <= 10) {
            timerElement.classList.add("timer-danger");
        }

        // Hết giờ: tự động tạo câu trả lời trống và submit để chuyển câu, tránh đứng game
        if (time <= 0) {
            clearInterval(countdown);
            alert("Hết thời gian làm bài của câu hỏi này!");

            const gameForm = document.querySelector("form");
            if (gameForm) {
                let hiddenTimeoutInput = document.createElement("input");
                hiddenTimeoutInput.type = "hidden";
                hiddenTimeoutInput.name = "answer";
                hiddenTimeoutInput.value = "TIMEOUT";
                gameForm.appendChild(hiddenTimeoutInput);
                gameForm.submit();
            }
        }
    }, 1000);
}

/*=========================
        SCORE EFFECT
=========================*/
const score = document.getElementById("scoreText");
if (score) {
    // Hiệu ứng scale nhẹ khi điểm số xuất hiện
    score.classList.add("score-add");
}

/*=========================
    SUBMIT ANIMATION (CHARACTER)
=========================*/
const form = document.querySelector("form");
if (form) {
    form.addEventListener("submit", function() {
        const anime = document.getElementById("anime");
        if (anime) {
            // Kích hoạt hiệu ứng lắc (correctShake) khi bấm gửi
            anime.classList.add("correct");
        }
    });
}

/*=========================
    BACKGROUND PARTICLES EFFECT
=========================*/
setInterval(function() {
    const p = document.createElement("div");
    p.className = "particle";
    p.style.left = Math.random() * 100 + "vw";
    p.style.animationDuration = 3 + Math.random() * 4 + "s";
    document.body.appendChild(p);

    setTimeout(() => {
        p.remove();
    }, 7000);
}, 250);

/*=========================
    ANSWER BUTTON SELECTION EFFECT
=========================*/
document.querySelectorAll(".answer-btn").forEach(function(btn) {
    btn.onclick = function() {
        // 1. Xóa class active của toàn bộ các nút đáp án khác
        document.querySelectorAll(".answer-btn").forEach(i => {
            i.classList.remove("answer-correct");
            // Đảm bảo nút radio bên trong không bị check nhầm
            const radio = i.querySelector("input[type='radio']");
            if (radio) radio.checked = false;
        });

        // 2. Kích hoạt trạng thái sáng xanh neon cho nút được click
        this.classList.add("answer-correct");

        // 3. Tích chọn thực tế vào thẻ input radio ẩn bên trong để gửi lên server Django
        const currentRadio = this.querySelector("input[type='radio']");
        if (currentRadio) {
            currentRadio.checked = true;
        }
    }
});

/*=========================
    PROGRESS BAR ANIMATION
=========================*/
// LƯU Ý: Phần trăm đã do Django gán động trong template play.html.
// Đoạn code dưới đây giúp thanh bar tăng mượt (Transition) từ 0% lên mốc % đó khi vừa tải trang.
const bar = document.getElementById("progressBar");
if (bar) {
    // Lấy giá trị phần trăm thực tế từ style mà Django đã render ra (ví dụ: 66%)
    let targetWidth = bar.style.width;

    // Đặt tạm về 0% rồi cho nó tăng dần lên mục tiêu để tạo hiệu ứng chuyển động mượt mà
    bar.style.width = "0%";
    setTimeout(() => {
        bar.style.width = targetWidth;
    }, 100);
}

/*=========================
        PLAY BUTTON HOVER
=========================*/
document.querySelectorAll(".btn-play").forEach(btn => {
    btn.addEventListener("mouseenter", () => {
        btn.style.transform = "scale(1.05)";
    });
    btn.addEventListener("mouseleave", () => {
        btn.style.transform = "scale(1)";
    });
});

/*=========================
    FLOAT CHARACTER (SINE WAVE)
=========================*/
const animeChar = document.getElementById("anime");
if (animeChar) {
    setInterval(() => {
        // Giữ hiệu ứng nhân vật C++ Sensei bay lên xuống nhịp nhàng dựa trên hàm Sin thời gian
        animeChar.style.transform = "translateY(" + (Math.sin(Date.now() / 400) * 8) + "px)";
    }, 20);
}