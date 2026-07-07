from django.contrib.auth.models import User
from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File

from PIL import Image

# ==========================
# THỂ LOẠI SÁCH
# ==========================
class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="category/")
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# # ==========================
# # SÁCH
# # ==========================
# class Book(models.Model):
#
#     name = models.CharField(max_length=255)
#
#     author = models.CharField(max_length=200)
#
#     publisher = models.CharField(max_length=200)
#
#     specification = models.TextField()
#
#     image = models.ImageField(upload_to="books/")
#
#     category = models.ForeignKey(
#         Category,
#         on_delete=models.CASCADE
#     )
#
#     quantity = models.PositiveIntegerField(default=1)
#
#     price = models.DecimalField(
#         max_digits=10,
#         decimal_places=2
#     )
#
#     status = models.BooleanField(default=True)
#
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.name
class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    specification = models.TextField()
    image = models.ImageField(upload_to="books/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # THÊM TRƯỜNG LƯU MÃ QR CODE
    qr_code = models.ImageField(upload_to="qr_codes/", blank=True, null=True)

    def __str__(self):
        return self.name

    # GHI ĐÈ HÀM SAVE ĐỂ TỰ ĐỘNG TẠO QRkhi ADMIN THÊM SÁCH
    def save(self, *args, **kwargs):
        # Lưu trước để lấy ID cuốn sách nếu là sách mới tinh
        is_new = self.pk is None
        super().save(*args, **kwargs)

        if is_new or not self.qr_code:
            # Tạo đường dẫn tuyệt đối dẫn thẳng tới trang chi tiết cuốn sách này
            # Khi chạy thực tế trên máy bạn, domain cục bộ là http://127.0.0.1:8000
            # qr_data = f"http://127.0.0{self.id}/"
            # Sửa lại dòng qr_data trong hàm save() của lớp Book trong models.py:
            qr_data = f"http://localhost:8000/book/{self.id}/"
            # Khởi tạo công cụ vẽ mã QR
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(qr_data)
            qr.make(fit=True)

            # Vẽ ảnh QR bằng thư viện Pillow
            img = qr.make_image(fill_color="black", back_color="white")

            # Tiến hành ép kiểu ảnh vào bộ nhớ đệm và lưu vào trường qr_code của Django
            buffer = BytesIO()
            img.save(buffer, format="PNG")
            filename = f"book_{self.id}_qr.png"

            self.qr_code.save(filename, File(buffer), save=False)
            super().save(*args, **kwargs)  # Lưu lại lần cuối cùng để cập nhật tệp QR

# ==========================
# GIỚI THIỆU
# ==========================
class About(models.Model):

    title = models.CharField(
        max_length=255,
        unique=True
    )

    text = models.TextField()

    image = models.ImageField(
        upload_to="about/"
    )

    def __str__(self):
        return self.title

class UserProfile(models.Model):
        GENDER = (
            ("Nam", "Nam"),
            ("Nữ", "Nữ"),
        )

        user = models.OneToOneField(
            User,
            on_delete=models.CASCADE
        )

        avatar = models.ImageField(
            upload_to="avatar/",
            default="avatar/default.png"
        )

        student_id = models.CharField(
            max_length=20,
            blank=True
        )

        faculty = models.CharField(
            max_length=100,
            blank=True
        )

        class_name = models.CharField(
            max_length=50,
            blank=True
        )

        phone = models.CharField(
            max_length=15,
            blank=True
        )

        address = models.TextField(
            blank=True
        )

        gender = models.CharField(
            max_length=10,
            choices=GENDER,
            default="Nam"
        )

        birthday = models.DateField(
            null=True,
            blank=True
        )

        def __str__(self):
            return self.user.username


# ==========================
# QUẢN LÝ MƯỢN / TRẢ SÁCH (Nền móng Giai đoạn 4)
# ==========================
class BorrowTicket(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Chờ duyệt mượn'),
        ('borrowing', 'Đang mượn'),
        ('returned', 'Đã trả'),
        ('overdue', 'Quá hạn'),
        ('canceled', 'Đã hủy'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="borrow_tickets")
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_deadline = models.DateField() # Ngày hẹn trả
    actual_return_date = models.DateField(null=True, blank=True) # Ngày trả thực tế
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.book.name} ({self.get_status_display()})"



# ==========================
# GIỎ HÀNG VÀ MUA SÁCH (Giai đoạn 5)
# ==========================
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cart")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Giỏ hàng của {self.user.username}"

    # Hàm tính tổng tiền tất cả sách trong giỏ
    def get_total_price(self):
        return sum(item.get_subtotal() for item in self.items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.book.name} trong giỏ"

    # Hàm tính tổng tiền của riêng mục này
    def get_subtotal(self):
        return self.book.price * self.quantity





# class Question(models.Model):
#
#     LEVEL = (
#         ("easy", "Easy"),
#         ("medium", "Medium"),
#         ("hard", "Hard"),
#     )
#
#     QUESTION_TYPE = (
#         ("choice", "Trắc nghiệm"),
#         ("drag", "Kéo thả"),
#         ("sort", "Sắp xếp Block Code"),
#     )
#
#     title = models.CharField(
#         max_length=300,
#         verbose_name="Tên câu hỏi"
#     )
#
#     code = models.TextField(
#         verbose_name="Code C++"
#     )
#
#     level = models.CharField(
#         max_length=20,
#         choices=LEVEL,
#         default="easy"
#     )
#
#     question_type = models.CharField(
#         max_length=20,
#         choices=QUESTION_TYPE,
#         default="choice"
#     )
#
#     option_a = models.CharField(max_length=300)
#
#     option_b = models.CharField(max_length=300)
#
#     option_c = models.CharField(max_length=300)
#
#     option_d = models.CharField(max_length=300)
#
#     correct = models.CharField(
#         max_length=1,
#         choices=(
#             ("A", "A"),
#             ("B", "B"),
#             ("C", "C"),
#             ("D", "D"),
#         )
#     )
#
#     score = models.IntegerField(default=10)
#
#     class Meta:
#         ordering = ["level", "id"]
#
#     def __str__(self):
#         return f"[{self.level.upper()}] {self.title}"


class GameQuestion(models.Model):
    LEVEL_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    TYPE_CHOICES = [
        ('multiple_choice', 'Trắc nghiệm (4 đáp án)'),
        ('drag_drop_blank', 'Kéo thả điền khuyết (Medium)'),
        ('sort_code', 'Sắp xếp dòng code (Hard)'),
    ]

    title = models.CharField(max_length=255, verbose_name="Tiêu đề / Yêu cầu câu hỏi")
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES, default='easy')
    question_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='multiple_choice')

    # --- DÙNG CHO TRẮC NGHIỆM & ĐIỀN KHUYẾT (Hiển thị đoạn code mẫu) ---
    code = models.TextField(blank=True, null=True, verbose_name="Đoạn mã hiển thị (Nếu có)")

    # --- DÙNG CHO TRẮC NGHIỆM (EASY & MEDIUM 2 CÂU ĐẦU) ---
    option_a = models.CharField(max_length=255, blank=True, null=True)
    option_b = models.CharField(max_length=255, blank=True, null=True)
    option_c = models.CharField(max_length=255, blank=True, null=True)
    option_d = models.CharField(max_length=255, blank=True, null=True)
    correct_option = models.CharField(max_length=1, blank=True, null=True, verbose_name="Đáp án đúng (A/B/C/D)")

    # --- DÙNG CHO MEDIUM (KÉO THẢ ĐIỀN KHUYẾT) ---
    # Gợi ý nhập box đáp án vô số từ Admin: "đáp_án_1, đáp_án_2, đáp_án_nhiễu_1, đáp_án_nhiễu_2"
    pool_answers = models.TextField(blank=True, null=True,
                                    verbose_name="Box chứa vô số đáp án (Cách nhau bởi dấu phẩy)")
    # Đáp án đúng theo thứ tự các ô trống: "int, cout, return"
    blank_answers = models.CharField(max_length=255, blank=True, null=True,
                                     verbose_name="Các đáp án đúng theo thứ tự ô trống (Cách nhau bởi dấu phẩy)")

    # --- DÙNG CHO HARD (SẮP XẾP DÒNG CODE) ---
    # Nhập các dòng code lộn xộn để hiện bên trái: "Line lộn xộn 1 || Line lộn xộn 2 || Line lộn xộn 3"
    shuffled_lines = models.TextField(blank=True, null=True,
                                      verbose_name="Các dòng code lộn xộn bên trái (Cách nhau bởi '||')")
    # Thứ tự đúng của các dòng code (Dựa theo text chính xác): "Dòng 1 || Dòng 2 || Dòng 3"
    correct_lines_order = models.TextField(blank=True, null=True,
                                           verbose_name="Thứ tự các dòng code đúng hoàn chỉnh (Cách nhau bởi '||')")

    def __str__(self):
        return f"[{self.get_level_display()}] - {self.title[:30]}"

class Score(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    score = models.IntegerField(default=0)

    total_correct = models.IntegerField(default=0)

    total_question = models.IntegerField(default=0)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.score}"


# Bổ sung vào cuối file models.py của bạn:

class Voucher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vouchers")
    code = models.CharField(max_length=50, unique=True)
    discount_percent = models.IntegerField(default=10)
    # Chỉ áp dụng Voucher cho một danh mục cụ thể (Ví dụ: Sách Lập Trình)
    applicable_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    is_used = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} - Giảm {self.discount_percent}% ({self.applicable_category.name if self.applicable_category else 'Tất cả'})"


# =======================================================
#               GAME 2: C++ POINTER RACING GT3
# =======================================================

class PointerGameQuestion(models.Model):
    LEVEL_CHOICES = [
        (1, 'Chặng 1: Tokyo Cyber Highway (Easy)'),
        (2, 'Chặng 2: Neo Monaco GP (Medium)'),
        (3, 'Chặng 3: Hell Gate Nürburgring (Hard)'),
    ]

    title = models.CharField(max_length=255, verbose_name="Tình huống / Chướng ngại vật")
    level = models.IntegerField(choices=LEVEL_CHOICES, default=1, verbose_name="Thuộc Chặng Level")
    code_context = models.TextField(blank=True, null=True, verbose_name="Đoạn mã con trỏ mẫu (Nếu có)")

    # 6 Lựa chọn đáp án đại diện cho các hành động của con trỏ C++
    option_1 = models.CharField(max_length=150, verbose_name="Đáp án 1")
    option_2 = models.CharField(max_length=150, verbose_name="Đáp án 2")
    option_3 = models.CharField(max_length=150, verbose_name="Đáp án 3")
    option_4 = models.CharField(max_length=150, verbose_name="Đáp án 4")
    option_5 = models.CharField(max_length=150, verbose_name="Đáp án 5")
    option_6 = models.CharField(max_length=150, verbose_name="Đáp án 6")

    correct_option = models.IntegerField(
        choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')],
        verbose_name="Đáp án đúng (Từ 1 đến 6)"
    )

    def __str__(self):
        return f"Stage {self.level} - {self.title[:30]}"


class PointerGameScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed_at = models.DateTimeField(auto_now_add=True)
    has_won = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - Đua xe Con trỏ"