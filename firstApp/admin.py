# from django.contrib import admin
# from django.utils.html import format_html
#
# from .models import Book, Category, About, BorrowTicket
# from .models import UserProfile
# from .models import GameQuestion,Score
# # ==========================
# # CATEGORY
# # ==========================
#
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#
#     list_display = (
#         "id",
#         "image_preview",
#         "name",
#         "status",
#     )
#
#     search_fields = (
#         "name",
#     )
#
#     list_filter = (
#         "status",
#     )
#
#     ordering = (
#         "id",
#     )
#
#     def image_preview(self, obj):
#         if obj.image:
#             return format_html(
#                 '<img src="{}" width="60" height="60" style="border-radius:8px;" />',
#                 obj.image.url
#             )
#         return "-"
#
#     image_preview.short_description = "Image"
#
#
# # ==========================
# # BOOK
# # ==========================
#
# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#
#     list_display = (
#         "id",
#         "image_preview",
#         "name",
#         "author",
#         "publisher",
#         "category",
#         "quantity",
#         "price",
#         "qr_preview",  # Thêm cột xem trước QR ngoài danh sách
#         "status",
#     )
#
#     search_fields = (
#         "name",
#         "author",
#         "publisher",
#     )
#
#     list_filter = (
#         "category",
#         "status",
#     )
#
#     ordering = (
#         "id",
#     )
#
#     list_per_page = 10
#
#     def image_preview(self, obj):
#         if obj.image:
#             return format_html(
#                 '<img src="{}" width="60" height="80" style="border-radius:8px;" />',
#                 obj.image.url
#             )
#         return "-"
#
#     image_preview.short_description = "Cover"
#  # Hàm hiển thị ảnh QR nhỏ trong trang quản trị
#     def qr_preview(self, obj):
#         if obj.qr_code:
#             return format_html(
#                 '<img src="{}" width="50" height="50" style="border: 1px solid #ccc;" />',
#                 obj.qr_code.url
#             )
#         return "-"
#     qr_preview.short_description = "Mã QR Sách"
#
# # ==========================
# # ABOUT
# # ==========================
#
# @admin.register(About)
# class AboutAdmin(admin.ModelAdmin):
#
#     list_display = (
#         "id",
#         "image_preview",
#         "title",
#     )
#
#     search_fields = (
#         "title",
#     )
#
#     def image_preview(self, obj):
#         if obj.image:
#             return format_html(
#                 '<img src="{}" width="80" />',
#                 obj.image.url
#             )
#         return "-"
#
#     image_preview.short_description = "Image"
#
#
# @admin.register(UserProfile)
# class UserProfileAdmin(admin.ModelAdmin):
#
#     list_display = (
#         "user",
#         "student_id",
#         "faculty",
#         "phone",
#     )
# @admin.register(BorrowTicket)
# class BorrowTicketAdmin(admin.ModelAdmin):
#     list_display = ("id", "user", "book", "borrow_date", "return_deadline", "status")
#     list_filter = ("status", "borrow_date")
#     search_fields = ("user__username", "book__name")
#     ordering = ("-id",)
#
#
# # ==========================
# # GAME QUESTION
# # ==========================
#
# @admin.register(GameQuestion)
# class QuestionAdmin(admin.ModelAdmin):
#
#     list_display = (
#         "id",
#         "title",
#         "level",
#         "question_type",
#         "correct",
#         "score",
#     )
#
#     list_filter = (
#         "level",
#         "question_type",
#     )
#
#     search_fields = (
#         "title",
#     )
#
#     ordering = (
#         "level",
#         "id",
#     )
#
#     fieldsets = (
#
#         ("Thông tin câu hỏi", {
#
#             "fields": (
#
#                 "title",
#
#                 "code",
#
#                 "level",
#
#                 "question_type",
#
#             )
#
#         }),
#
#         ("Đáp án", {
#
#             "fields": (
#
#                 "option_a",
#
#                 "option_b",
#
#                 "option_c",
#
#                 "option_d",
#
#                 "correct",
#
#                 "score",
#
#             )
#
#         }),
#
#     )
#
#
# # ==========================
# # GAME SCORE
# # ==========================
#
# @admin.register(Score)
# class ScoreAdmin(admin.ModelAdmin):
#
#     list_display = (
#
#         "id",
#
#         "user",
#
#         "score",
#
#         "total_correct",
#
#         "total_question",
#
#         "created",
#
#     )
#
#     ordering = (
#
#         "-created",
#
#     )
#
#     search_fields = (
#
#         "user__username",
#
#     )
#
#
from django.contrib import admin
from django.utils.html import format_html

from .models import Book, Category, About, BorrowTicket, UserProfile, GameQuestion, Score, Voucher

# ==========================
# CATEGORY
# ==========================
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "image_preview",
        "name",
        "status",
    )
    search_fields = ("name",)
    list_filter = ("status",)
    ordering = ("id",)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" style="border-radius:8px; object-fit: cover;" />',
                obj.image.url
            )
        return "-"
    image_preview.short_description = "Image"


# ==========================
# BOOK
# ==========================
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "image_preview",
        "name",
        "author",
        "publisher",
        "category",
        "quantity",
        "price",
        "qr_preview",
        "status",
    )
    search_fields = ("name", "author", "publisher")
    list_filter = ("category", "status")
    ordering = ("id",)
    list_per_page = 10

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="80" style="border-radius:8px; object-fit: cover;" />',
                obj.image.url
            )
        return "-"
    image_preview.short_description = "Cover"

    def qr_preview(self, obj):
        if obj.qr_code:
            return format_html(
                '<img src="{}" width="50" height="50" style="border: 1px solid #ccc; border-radius:4px;" />',
                obj.qr_code.url
            )
        return "-"
    qr_preview.short_description = "Mã QR Sách"


# ==========================
# ABOUT
# ==========================
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("id", "image_preview", "title")
    search_fields = ("title",)

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="80" style="border-radius:4px;" />',
                obj.image.url
            )
        return "-"
    image_preview.short_description = "Image"


# ==========================
# USER PROFILE
# ==========================
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "student_id", "faculty", "phone", "gender", "class_name")
    search_fields = ("user__username", "student_id", "phone")
    list_filter = ("faculty", "gender")


# ==========================
# BORROW TICKET
# ==========================
@admin.register(BorrowTicket)
class BorrowTicketAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "book", "borrow_date", "return_deadline", "actual_return_date", "status")
    list_filter = ("status", "borrow_date")
    search_fields = ("user__username", "book__name")
    ordering = ("-id",)


# ==========================
# VOUCHER (Bổ sung quản lý lịch sử phát hành)
# ==========================
@admin.register(Voucher)
class VoucherAdmin(admin.ModelAdmin):
    list_display = ("code", "user", "discount_percent", "applicable_category", "is_used", "created_at")
    list_filter = ("is_used", "applicable_category")
    search_fields = ("code", "user__username")
    ordering = ("-created_at",)


# ==========================
# GAME QUESTION (Sửa đổi chính xác theo model mới)
# ==========================
@admin.register(GameQuestion)
class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "level",
        "question_type",
    )
    list_filter = ("level", "question_type")
    search_fields = ("title", "code")
    ordering = ("level", "id")

    # Chia các phân vùng nhập liệu khoa học, rõ ràng giúp bạn dễ phân loại khi soạn đề câu hỏi
    fieldsets = (
        ("Thông tin cơ bản", {
            "fields": ("title", "level", "question_type", "code")
        }),
        ("Cấu hình Trắc nghiệm (Easy & 2 câu đầu Medium)", {
            "fields": ("option_a", "option_b", "option_c", "option_d", "correct_option"),
            "description": "Chỉ nhập dữ liệu phần này nếu chọn Loại câu hỏi là 'Trắc nghiệm'."
        }),
        ("Cấu hình Kéo thả điền khuyết (Medium)", {
            "fields": ("pool_answers", "blank_answers"),
            "description": "Nhập các từ ngăn cách bằng dấu phẩy. Ví dụ: 'int, cout, return'."
        }),
        ("Cấu hình Sắp xếp dòng code (Hard)", {
            "fields": ("shuffled_lines", "correct_lines_order"),
            "description": "Nhập các khối lệnh dòng code phân tách nhau bằng ký tự '||'."
        }),
    )


# ==========================
# GAME SCORE
# ==========================
@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "score",
        "total_correct",
        "total_question",
        "created",
    )
    ordering = ("-created",)
    search_fields = ("user__username",)


# Thêm các Model mới vào danh sách import ở đầu file nếu chưa có
from .models import PointerGameQuestion, PointerGameScore


# =======================================================
#          GAME 2: POINTER RACING GT3 ADMIN
# =======================================================

@admin.register(PointerGameQuestion)
class PointerGameQuestionAdmin(admin.ModelAdmin):
    # Hiển thị danh sách câu hỏi ngoài trang tổng quan
    list_display = (
        "id",
        "level",
        "title",
        "correct_option",
    )

    # Bộ lọc nhanh theo Chặng (Level) bên cột phải
    list_filter = ("level",)

    # Thanh tìm kiếm theo tiêu đề tình huống hoặc đoạn mã
    search_fields = ("title", "code_context")

    # Sắp xếp mặc định theo thứ tự ID chặng tăng dần
    ordering = ("level", "id")

    # Phân nhóm khu vực nhập liệu trực quan khi thêm câu hỏi
    fieldsets = (
        ("Thông tin Chặng đua", {
            "fields": ("level", "title", "code_context")
        }),
        ("Hệ thống 06 Lệnh điều khiển (Đáp án)", {
            "fields": (
                "option_1",
                "option_2",
                "option_3",
                "option_4",
                "option_5",
                "option_6",
            ),
            "description": "Nhập các câu lệnh hoặc thao tác con trỏ C++. Hệ thống sẽ tự động gán nhãn từ [01] đến [06] ngoài giao diện game."
        }),
        ("Cơ chế Vượt chướng ngại vật", {
            "fields": ("correct_option",),
            "description": "Chọn số thứ tự của đáp án đúng (Từ 1 đến 6) để kích hoạt lệnh Drift/Phóng xe vượt rào chắn."
        }),
    )


@admin.register(PointerGameScore)
class PointerGameScoreAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "has_won", "completed_at")
    list_filter = ("has_won", "completed_at")
    search_fields = ("user__username",)
    ordering = ("-completed_at",)