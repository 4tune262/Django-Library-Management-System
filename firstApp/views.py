# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render
#
# from firstApp.models import About, Book, Category, Voucher
#
# from django.shortcuts import redirect
# from .forms import RegisterForm
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib import messages
# from .forms import ProfileForm
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import get_object_or_404
# from .models import BorrowTicket
# # Đảm bảo ở đầu file views.py có dòng import đầy đủ này:
# from datetime import date, timedelta
# from django.contrib.auth.decorators import login_required
# from .models import Cart, CartItem, Book
# from django.db.models import Q
# from django.http import JsonResponse
# from django.core.paginator import Paginator
# from .models import Question
# from .models import Score
# from django.utils import timezone
# from random import choice
# # Create your views here.
# def index(request):
#
#     new_books = Book.objects.filter(status=True).order_by("-created_at")[:10]
#
#     return render(request, "index.html", {
#         "new_books": new_books
#     })
# def about(request):
#     acc_about = About.objects.all()
#     dic = {
#         'title': 'About',
#         'content': 'About',
#         'acc_about': acc_about
#     }
#     return render(request, "about.html",dic)
#
# from firstApp.models import Book, Category
#
# # def books(request):
# #
# #     books = Book.objects.filter(status=True)
# #
# #     categories = Category.objects.filter(status=True)
# #
# #     selected = request.GET.getlist("category")
# #     keyword = request.GET.get("q")
# #
# #     if keyword:
# #
# #             books=books.filter(
# #                 Q(name__icontains=keyword) |
# #                 Q(author__icontains=keyword) |
# #                 Q(publisher__icontains=keyword) |
# #                 Q(category__name__icontains=keyword)
# #             )
# #
# #
# #     if selected:
# #         books = books.filter(category__id__in=selected)
# #
# #     return render(
# #         request,
# #         "books.html",
# #         {
# #             "title": "Books",
# #             "books": books,
# #             "categories": categories,
# #             "selected": list(map(int, selected))
# #         }
# #     )
#
# def books(request):
#
#     books = Book.objects.filter(status=True)
#
#     categories = Category.objects.filter(status=True)
#
#     selected = request.GET.getlist("category")
#     keyword = request.GET.get("q", "").strip()
#     sort = request.GET.get("sort")
#     if keyword == "None":
#         keyword = ""
#     if keyword:
#         books = books.filter(
#             Q(name__icontains=keyword) |
#             Q(author__icontains=keyword) |
#             Q(publisher__icontains=keyword)
#         )
#
#     if selected:
#         books = books.filter(category__id__in=selected)
#     # ================= SORT =================
#
#     if sort == "price_asc":
#         books = books.order_by("price")
#
#     elif sort == "price_desc":
#         books = books.order_by("-price")
#
#     elif sort == "name_asc":
#         books = books.order_by("name")
#
#     elif sort == "name_desc":
#         books = books.order_by("-name")
#
#     elif sort == "newest":
#         books = books.order_by("-created_at")
#     else:
#         books = books.order_by("-created_at")
#     # ---------------- Pagination ----------------
#     paginator = Paginator(books, 9)   # 9 sách / trang
#
#     page_number = request.GET.get("page")
#
#     page_obj = paginator.get_page(page_number)
#
#     return render(
#         request,
#         "books.html",
#         {
#             "title": "Books",
#             "books": page_obj,
#             "page_obj": page_obj,
#             "categories": categories,
#             "selected": list(map(int, selected)),
#             "keyword": keyword,
#             "sort": sort,
#         }
#     )
# def register(request):
#
#     if request.method == "POST":
#
#         form = RegisterForm(request.POST)
#
#         if form.is_valid():
#
#             user = form.save()
#             from .models import UserProfile
#             UserProfile.objects.create(
#                 user=user
#             )
#
#             login(request, user)
#
#             return redirect("/")
#
#     else:
#
#         form = RegisterForm()
#
#     return render(request,
#                   "account/register.html",
#                   {
#                       "title": "Đăng ký",
#                       "form": form
#                   })
# def user_login(request):
#
#     if request.user.is_authenticated:
#         return redirect("home")
#
#     if request.method == "POST":
#
#         username = request.POST["username"]
#
#         password = request.POST["password"]
#
#         user = authenticate(
#             username=username,
#             password=password
#         )
#
#         if user:
#
#             login(request, user)
#
#             messages.success(request, "Đăng nhập thành công.")
#
#             return redirect("home")
#
#         else:
#
#             messages.error(request, "Sai tài khoản hoặc mật khẩu.")
#
#     return render(request,
#                   "account/login.html",
#                   {
#                       "title":"Đăng nhập"
#                   })
#
# @login_required
# def user_logout(request):
#
#     logout(request)
#
#     messages.success(request, "Đã đăng xuất.")
#
#     return redirect("home")
#
#
#
# @login_required
# def profile(request):
#
#     profile = request.user.userprofile
#
#     if request.method == "POST":
#
#         form = ProfileForm(
#             request.POST,
#             request.FILES,
#             instance=profile
#         )
#
#         if form.is_valid():
#
#             form.save()
#
#             messages.success(
#                 request,
#                 "Cập nhật thành công."
#             )
#
#             return redirect("profile")
#
#     else:
#
#         form = ProfileForm(
#             instance=profile
#         )
#
#     return render(
#         request,
#         "account/profile.html",
#         {
#             "title": "Hồ sơ",
#             "form": form,
#             "profile": profile
#         }
#     )
# # def book_detail(request, id):
# #
# #     book = get_object_or_404(
# #         Book,
# #         id=id,
# #         status=True
# #     )
# #
# #     related_books = Book.objects.filter(
# #         category=book.category,
# #         status=True
# #     ).exclude(id=book.id)[:4]
# #
# #     return render(
# #         request,
# #         "book_detail.html",
# #         {
# #             "title": book.name,
# #             "book": book,
# #             "related_books": related_books
# #         }
# #     )
#
#
# @login_required(login_url='login')
# def student_dashboard(request):
#     # Lấy tất cả phiếu mượn của sinh viên hiện tại
#     user_tickets = BorrowTicket.objects.filter(user=request.user)
#
#     # Tính toán các chỉ số thống kê
#     total_borrowing = user_tickets.filter(status='borrowing').count()
#     total_returned = user_tickets.filter(status='returned').count()
#     total_pending = user_tickets.filter(status='pending').count()
#
#     # Kiểm tra sách quá hạn (Trạng thái đang mượn và quá ngày hẹn trả)
#     total_overdue = user_tickets.filter(status='borrowing', return_deadline__lt=date.today()).count()
#
#     # Lấy danh sách sách đang mượn thực tế để hiển thị lên bảng của Dashboard
#     current_borrowing_books = user_tickets.filter(status__in=['borrowing', 'overdue']).order_by('return_deadline')
#
#     context = {
#         "title": "Dashboard Cá Nhân",
#         "total_borrowing": total_borrowing,
#         "total_returned": total_returned,
#         "total_pending": total_pending,
#         "total_overdue": total_overdue,
#         "current_books": current_borrowing_books,
#     }
#     return render(request, "admin_page/dashboard.html", context)
#
#
# # XEM CHI TIẾT SÁCH
# def book_detail(request, id):
#     book = get_object_or_404(Book, id=id, status=True)
#
#     # Lấy ra các sách cùng thể loại nhưng loại trừ cuốn hiện tại
#     related_books = Book.objects.filter(
#         category=book.category,
#         status=True
#     ).exclude(id=book.id)[:4]
#
#     # Kiểm tra xem sinh viên hiện tại đã gửi yêu cầu hoặc đang mượn cuốn này chưa
#     has_borrowed = False
#     if request.user.is_authenticated:
#         has_borrowed = BorrowTicket.objects.filter(
#             user=request.user,
#             book=book,
#             status__in=['pending', 'borrowing', 'overdue']
#         ).exists()
#
#     return render(
#         request,
#         "book_detail.html",
#         {
#             "title": book.name,
#             "book": book,
#             "related_books": related_books,
#             "has_borrowed": has_borrowed
#         }
#     )
#
#
# # XỬ LÝ BẤM NÚT MƯỢN SÁCH
# @login_required(login_url='login')
# def borrow_book(request, id):
#     if request.method == "POST":
#         book = get_object_or_404(Book, id=id, status=True)
#
#         # 1. Kiểm tra nếu sách trong kho đã hết
#         if book.quantity <= 0:
#             messages.error(request, "Cuốn sách này hiện tại đã hết trong kho lưu trữ!")
#             return redirect('book_detail', id=id)
#
#         # 2. Kiểm tra nếu sinh viên đã mượn hoặc đang chờ duyệt cuốn này rồi
#         already_requested = BorrowTicket.objects.filter(
#             user=request.user,
#             book=book,
#             status__in=['pending', 'borrowing', 'overdue']
#         ).exists()
#
#         if already_requested:
#             messages.warning(request, "Bạn đã gửi yêu cầu mượn hoặc đang giữ cuốn sách này rồi!")
#             return redirect('book_detail', id=id)
#
#         # 3. Tạo phiếu mượn tự động (Hạn trả mặc định là 14 ngày sau)
#         deadline = date.today() + timedelta(days=14)
#
#         BorrowTicket.objects.create(
#             user=request.user,
#             book=book,
#             return_deadline=deadline,
#             status='pending'
#         )
#
#         messages.success(request, "Gửi yêu cầu mượn sách thành công! Vui lòng chờ thủ thư phê duyệt.")
#         return redirect('dashboard')
#
#     return redirect('books')
#
#
# # 1. THÊM SÁCH VÀO GIỎ HÀNG
# @login_required(login_url='login')
# def add_to_cart(request, book_id):
#     book = get_object_or_404(Book, id=book_id, status=True)
#
#     # Lấy hoặc tự động tạo giỏ hàng cho user hiện tại
#     cart, created = Cart.objects.get_or_create(user=request.user)
#
#     # Kiểm tra xem sách đã tồn tại trong giỏ chưa
#     cart_item, item_created = CartItem.objects.get_or_create(cart=cart, book=book)
#
#     if not item_created:
#         cart_item.quantity += 1
#         cart_item.save()
#
#     messages.success(request, f"Đã thêm '{book.name}' vào giỏ hàng thành công!")
#     return redirect('view_cart')
#
#
# # 2. XEM CHI TIẾT GIỎ HÀNG
# @login_required(login_url='login')
# def view_cart(request):
#     cart, created = Cart.objects.get_or_create(user=request.user)
#     return render(
#         request,
#         "cart/view_cart.html",
#         {
#             "title": "Giỏ hàng của bạn",
#             "cart": cart
#         }
#     )
#
#
# # 3. XÓA MỤC KHỎI GIỎ HÀNG
# @login_required(login_url='login')
# def remove_from_cart(request, item_id):
#     cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
#     book_name = cart_item.book.name
#     cart_item.delete()
#     messages.success(request, f"Đã xóa '{book_name}' khỏi giỏ hàng.")
#     return redirect('view_cart')
#
#
# @login_required(login_url='login')
# def update_cart_quantity(request, item_id):
#     if request.method == "POST":
#         cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
#         action = request.POST.get('action')  # Nhận hành động tăng hoặc giảm
#
#         if action == 'increase':
#             # Kiểm tra xem có vượt quá số lượng sách hiện có trong kho không
#             if cart_item.quantity < cart_item.book.quantity:
#                 cart_item.quantity += 1
#                 cart_item.save()
#             else:
#                 messages.warning(request, f"Trong kho chỉ còn tối đa {cart_item.book.quantity} quyển!")
#
#         elif action == 'decrease':
#             cart_item.quantity -= 1
#             if cart_item.quantity <= 0:
#                 cart_item.delete()  # Nếu giảm về 0 thì xóa luôn sách khỏi giỏ
#                 messages.success(request, f"Đã xóa '{cart_item.book.name}' khỏi giỏ hàng.")
#                 return redirect('view_cart')
#             else:
#                 cart_item.save()
#
#     return redirect('view_cart')
# def search_books(request):
#
#     keyword = request.GET.get("q", "").strip()
#
#     books = Book.objects.filter(
#         status=True
#     )
#
#     if keyword:
#         books = books.filter(
#             Q(name__icontains=keyword) |
#             Q(author__icontains=keyword) |
#             Q(publisher__icontains=keyword)
#         )
#
#     books = books[:6]
#
#     data = []
#
#     for book in books:
#
#         data.append({
#             "id": book.id,
#             "name": book.name,
#             "author": book.author,
#             "image": book.image.url if book.image else "",
#             "quantity": book.quantity,
#             "price": str(book.price)
#         })
#
#     return JsonResponse(data, safe=False)
#
#
#
#
#
#
#
# # @login_required
# # def game_home(request):
# #
# #     score=Score.objects.filter(
# #
# #         user=request.user
# #
# #     )
# #
# #     total=sum(i.score for i in score)
# #     request.session.pop("game_state", None)
# #
# #     score = Score.objects.filter(user=request.user)
# #     total = sum(i.score for i in score)
# #     return render(
# #
# #         request,
# #
# #         "game/home.html",
# #
# #         {
# #
# #             "total":total
# #
# #         }
# #
# #     )
# #
# #
# # @login_required
# # def play_game(request, level):
# #
# #     # =========================
# #     # KHỞI TẠO SESSION GAME
# #     # =========================
# #     if "game_state" not in request.session:
# #         request.session["game_state"] = {
# #             "level": level,
# #             "index": 0,
# #             "correct": 0,
# #             "total": 0
# #         }
# #
# #     state = request.session["game_state"]
# #
# #     questions = list(Question.objects.filter(level=level).order_by("id"))
# #     state = request.session.get("game_state")
# #     if not isinstance(state, dict):
# #         state = {
# #             "level": level,
# #             "index": 0,
# #             "correct": 0,
# #             "total": 0
# #         }
# #         request.session["game_state"] = state
# #     if not state:
# #         state = {
# #             "level": level,
# #             "index": 0,
# #             "correct": 0,
# #             "total": 0
# #         }
# #         request.session["game_state"] = state
# #     if not questions:
# #         messages.warning(request, "Level này chưa có câu hỏi.")
# #         return redirect("game_home")
# #
# #     # Nếu hết 3 câu → kết thúc level
# #     if state["index"] >= len(questions):
# #         return redirect("game_result")
# #
# #     question = questions[state["index"]]
# #
# #     if request.method == "POST":
# #
# #         answer = request.POST.get("answer")
# #         if not answer:
# #             messages.warning(request, "Bạn chưa chọn đáp án!")
# #             return redirect("play_game", level=level)
# #         is_correct = (answer == question.correct)
# #
# #         # cập nhật session
# #         state["total"] += 1
# #         if is_correct:
# #             state["correct"] += 1
# #
# #         state["index"] += 1
# #
# #         request.session["game_state"] = state
# #         request.session.modified = True
# #
# #         return redirect("play_game", level=level)
# #
# #     return render(request, "game/play.html", {
# #         "question": question,
# #         "level": level,
# #         "index": state["index"] + 1,
# #         "total_q": len(questions)
# #     })
# #
# #
# # @login_required
# # def game_result(request):
# #
# #     state = request.session.get("game_state")
# #
# #     if not state:
# #         return redirect("game_home")
# #
# #     correct = state["correct"]
# #
# #     # reset session sau khi kết thúc
# #     request.session["game_state"] = None
# #
# #     voucher = None
# #
# #     # =========================
# #     # PHÁT VOUCHER
# #     # =========================
# #     if correct >= 8:
# #
# #         from .models import Voucher
# #         from .utils import generate_voucher_code
# #
# #         voucher = Voucher.objects.create(
# #             user=request.user,
# #             code=generate_voucher_code(),
# #             discount_percent=10
# #         )
# #
# #     return render(request, "game/result.html", {
# #         "correct": correct,
# #         "voucher": voucher
# #     })
# import random
# import string
#
#
#
# @login_required(login_url='login')
# def game_home(request):
#     # Xóa trạng thái game cũ nếu có khi quay lại trang chủ game
#     if "game_state" in request.session:
#         del request.session["game_state"]
#
#     # Tính tổng điểm tích lũy của user từ trước đến nay
#     scores = Score.objects.filter(user=request.user)
#     total = sum(s.score for s in scores)
#
#     return render(request, "game/home.html", {"total": total})
#
#
# @login_required(login_url='login')
# def play_game(request, level):
#     level = level.lower()
#
#     # 1. Khởi tạo phiên chơi game mới nếu chưa có hoặc đổi level đột ngột
#     if "game_state" not in request.session or request.session["game_state"]["level"] != level:
#         # Lọc danh sách câu hỏi theo cấu hình yêu cầu
#         all_questions = list(Question.objects.filter(level=level))
#
#         # Phân loại câu hỏi theo yêu cầu của bạn
#         if level == "easy":
#             selected_qs = [q for q in all_questions if q.question_type == "choice"][:3]
#         elif level == "medium":
#             choices = [q for q in all_questions if q.question_type == "choice"][:2]
#             drags = [q for q in all_questions if q.question_type == "drag"][:2]
#             selected_qs = choices + drags
#         elif level == "hard":
#             selected_qs = [q for q in all_questions if q.question_type == "sort"][:3]
#         else:
#             selected_qs = all_questions[:3]
#
#         if not selected_qs:
#             messages.warning(request, f"Hệ thống chưa cấu hình đủ câu hỏi cho nhóm {level.upper()}!")
#             return redirect("game_home")
#
#         request.session["game_state"] = {
#             "level": level,
#             "q_ids": [q.id for q in selected_qs],
#             "current_index": 0,
#             "score_earned": 0,
#             "correct_count": 0,
#         }
#
#     state = request.session["game_state"]
#     q_ids = state["q_ids"]
#     current_idx = state["current_index"]
#
#     # Nếu đã làm hết số câu hỏi của Level này
#     if current_idx >= len(q_ids):
#         if level == "easy":
#             return redirect("play_game", level="medium")
#         elif level == "medium":
#             return redirect("play_game", level="hard")
#         else:
#             return redirect("game_result")
#
#     # Lấy đối tượng câu hỏi hiện tại
#     question = get_object_or_404(Question, id=q_ids[current_idx])
#
#     if request.method == "POST":
#         user_answer = request.POST.get("answer", "").strip()
#
#         # So sánh đáp án (Chấp nhận cả chữ thường/hoa)
#         if user_answer.upper() == question.correct.upper():
#             state["score_earned"] += 10
#             state["correct_count"] += 1
#             messages.success(request, "Chính xác! +10 điểm.")
#         else:
#             messages.error(request, f"Sai rồi! Đáp án đúng là {question.correct}")
#
#         # Chuyển sang câu tiếp theo
#         state["current_index"] += 1
#         request.session["game_state"] = state
#         request.session.modified = True
#
#         # Điều hướng tiếp tục vòng lặp
#         return redirect("play_game", level=level)
#
#     return render(request, "game/play.html", {
#         "question": question,
#         "level": level,
#         "index": current_idx + 1,
#         "total_q": len(q_ids),
#         "score_earned": state["score_earned"]
#     })
#
#
# @login_required(login_url='login')
# def game_result(request):
#     state = request.session.get("game_state")
#     if not state:
#         return redirect("game_home")
#
#     score_earned = state["score_earned"]
#     correct_count = state["correct_count"]
#     total_q = len(state["q_ids"])
#
#     # Lưu kết quả chơi vào bảng Score trong Database
#     Score.objects.create(
#         user=request.user,
#         score=score_earned,
#         total_correct=correct_count,
#         total_question=total_q
#     )
#
#     # Clear session game sau khi lưu xong
#     del request.session["game_state"]
#
#     # Xử lý cấp mã Voucher nếu đạt yêu cầu (ví dụ trả lời đúng từ 70% số câu trở lên)
#     voucher = None
#     if correct_count >= 2:  # Thay đổi số lượng tùy ý bạn
#         # Tìm hoặc tạo category "Sách Lập Trình" để gán điều kiện cho Voucher
#         prog_cat, _ = Category.objects.get_or_create(name="Sách Lập Trình")
#
#         code_gen = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
#         voucher = Voucher.objects.create(
#             user=request.user,
#             code=f"CPP-{code_gen}",
#             discount_percent=10,
#             applicable_category=prog_cat
#         )
#
#     return render(request, "game/result.html", {
#         "score_earned": score_earned,
#         "correct_count": correct_count,
#         "voucher": voucher
#     })


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.http import JsonResponse
from django.core.paginator import Paginator
from datetime import date, timedelta
import random
import string

from firstApp.forms import ProfileForm, RegisterForm
from firstApp.models import About, Book, Category, Voucher, BorrowTicket, Cart, CartItem, Score, PointerGameQuestion, \
    PointerGameScore
from django.shortcuts import render, redirect, get_object_or_404
from .models import GameQuestion

def index(request):
    new_books = Book.objects.filter(status=True).order_by("-created_at")[:10]
    return render(request, "index.html", {"new_books": new_books})


def about(request):
    acc_about = About.objects.all()
    dic = {
        'title': 'About',
        'content': 'About',
        'acc_about': acc_about
    }
    return render(request, "about.html", dic)


def books(request):
    books = Book.objects.filter(status=True)
    categories = Category.objects.filter(status=True)
    selected = request.GET.getlist("category")
    keyword = request.GET.get("q", "").strip()
    sort = request.GET.get("sort")

    if keyword == "None":
        keyword = ""
    if keyword:
        books = books.filter(
            Q(name__icontains=keyword) |
            Q(author__icontains=keyword) |
            Q(publisher__icontains=keyword)
        )

    if selected:
        books = books.filter(category__id__in=selected)

    if sort == "price_asc":
        books = books.order_by("price")
    elif sort == "price_desc":
        books = books.order_by("-price")
    elif sort == "name_asc":
        books = books.order_by("name")
    elif sort == "name_desc":
        books = books.order_by("-name")
    elif sort == "newest":
        books = books.order_by("-created_at")
    else:
        books = books.order_by("-created_at")

    paginator = Paginator(books, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "books.html",
        {
            "title": "Books",
            "books": page_obj,
            "page_obj": page_obj,
            "categories": categories,
            "selected": list(map(int, selected)),
            "keyword": keyword,
            "sort": sort,
        }
    )


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            from .models import UserProfile
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect("/")
    else:
        form = RegisterForm()
    return render(request, "account/register.html", {"title": "Đăng ký", "form": form})


def user_login(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Đăng nhập thành công.")
            return redirect("home")
        else:
            messages.error(request, "Sai tài khoản hoặc mật khẩu.")
    return render(request, "account/login.html", {"title": "Đăng nhập"})


@login_required
def user_logout(request):
    logout(request)
    messages.success(request, "Đã đăng xuất.")
    return redirect("home")


@login_required
def profile(request):
    profile = request.user.userprofile
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Cập nhật thành công.")
            return redirect("profile")
    else:
        form = ProfileForm(instance=profile)
    return render(request, "account/profile.html", {"title": "Hồ sơ", "form": form, "profile": profile})


@login_required(login_url='login')
def student_dashboard(request):
    user_tickets = BorrowTicket.objects.filter(user=request.user)
    total_borrowing = user_tickets.filter(status='borrowing').count()
    total_returned = user_tickets.filter(status='returned').count()
    total_pending = user_tickets.filter(status='pending').count()
    total_overdue = user_tickets.filter(status='borrowing', return_deadline__lt=date.today()).count()
    current_borrowing_books = user_tickets.filter(status__in=['borrowing', 'overdue']).order_by('return_deadline')

    context = {
        "title": "Dashboard Cá Nhân",
        "total_borrowing": total_borrowing,
        "total_returned": total_returned,
        "total_pending": total_pending,
        "total_overdue": total_overdue,
        "current_books": current_borrowing_books,
    }
    return render(request, "admin_page/dashboard.html", context)


def book_detail(request, id):
    book = get_object_or_404(Book, id=id, status=True)
    related_books = Book.objects.filter(category=book.category, status=True).exclude(id=book.id)[:4]
    has_borrowed = False
    if request.user.is_authenticated:
        has_borrowed = BorrowTicket.objects.filter(
            user=request.user, book=book, status__in=['pending', 'borrowing', 'overdue']
        ).exists()
    return render(request, "book_detail.html",
                  {"title": book.name, "book": book, "related_books": related_books, "has_borrowed": has_borrowed})


@login_required(login_url='login')
def borrow_book(request, id):
    if request.method == "POST":
        book = get_object_or_404(Book, id=id, status=True)
        if book.quantity <= 0:
            messages.error(request, "Cuốn sách này hiện tại đã hết trong kho lưu trữ!")
            return redirect('book_detail', id=id)
        already_requested = BorrowTicket.objects.filter(
            user=request.user, book=book, status__in=['pending', 'borrowing', 'overdue']
        ).exists()
        if already_requested:
            messages.warning(request, "Bạn đã gửi yêu cầu mượn hoặc đang giữ cuốn sách này rồi!")
            return redirect('book_detail', id=id)
        deadline = date.today() + timedelta(days=14)
        BorrowTicket.objects.create(user=request.user, book=book, return_deadline=deadline, status='pending')
        messages.success(request, "Gửi yêu cầu mượn sách thành công! Vui lòng chờ thủ thư phê duyệt.")
        return redirect('dashboard')
    return redirect('books')


@login_required(login_url='login')
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id, status=True)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, book=book)
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
    messages.success(request, f"Đã thêm '{book.name}' vào giỏ hàng thành công!")
    return redirect('view_cart')


# @login_required(login_url='login')
# def view_cart(request):
#     cart, created = Cart.objects.get_or_create(user=request.user)
#     return render(request, "cart/view_cart.html", {"title": "Giỏ hàng của bạn", "cart": cart})
@login_required(login_url='login')
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)

    # 1. Tiền gốc từ hàm trong model của bạn
    total_price = cart.get_total_price()

    # 2. Quét tìm Voucher khả dụng chưa sử dụng của user hiện tại
    active_voucher = Voucher.objects.filter(user=request.user, is_used=False).first()

    discount_amount = 0
    applied_voucher_code = None
    discount_percent = 0

    if active_voucher and total_price > 0:
        discount_percent = active_voucher.discount_percent
        # Áp dụng giảm giá trực tiếp lên tổng giá trị toàn bộ giỏ hàng
        discount_amount = (total_price * discount_percent) / 100
        applied_voucher_code = active_voucher.code

    # 3. Tính số tiền cuối cùng sau giảm giá
    final_price = total_price - discount_amount
    if final_price < 0:
        final_price = 0

    context = {
        "title": "Giỏ hàng của bạn",
        "cart": cart,
        "total_price": total_price,
        "discount_amount": discount_amount,
        "final_price": final_price,
        "applied_voucher_code": applied_voucher_code,
        "discount_percent": discount_percent
    }
    return render(request, "cart/view_cart.html", context)

@login_required(login_url='login')
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    book_name = cart_item.book.name
    cart_item.delete()
    messages.success(request, f"Đã xóa '{book_name}' khỏi giỏ hàng.")
    return redirect('view_cart')


@login_required(login_url='login')
def update_cart_quantity(request, item_id):
    if request.method == "POST":
        cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
        action = request.POST.get('action')
        if action == 'increase':
            if cart_item.quantity < cart_item.book.quantity:
                cart_item.quantity += 1
                cart_item.save()
            else:
                messages.warning(request, f"Trong kho chỉ còn tối đa {cart_item.book.quantity} quyển!")
        elif action == 'decrease':
            cart_item.quantity -= 1
            if cart_item.quantity <= 0:
                cart_item.delete()
                messages.success(request, f"Đã xóa '{cart_item.book.name}' khỏi giỏ hàng.")
                return redirect('view_cart')
            else:
                cart_item.save()
    return redirect('view_cart')


def search_books(request):
    keyword = request.GET.get("q", "").strip()
    books = Book.objects.filter(status=True)
    if keyword:
        books = books.filter(
            Q(name__icontains=keyword) | Q(author__icontains=keyword) | Q(publisher__icontains=keyword))
    books = books[:6]
    data = []
    for book in books:
        data.append({
            "id": book.id,
            "name": book.name,
            "author": book.author,
            "image": book.image.url if book.image else "",
            "quantity": book.quantity,
            "price": str(book.price)
        })
    return JsonResponse(data, safe=False)


# =======================================================
#             HỆ THỐNG ĐIỀU HƯỚNG C++ ARENA GAME
# =======================================================

@login_required(login_url='login')
def game_home(request):
    # Dọn dẹp các session game cũ khi quay lại sảnh chính
    if "game_state" in request.session:
        del request.session["game_state"]
    if "game_state_global" in request.session:
        del request.session["game_state_global"]

    scores = Score.objects.filter(user=request.user)
    total = sum(s.score for s in scores)
    return render(request, "game/home.html", {"total": total})


@login_required(login_url='login')
def play_game(request, level):
    level = level.lower()

    # 1. Khởi tạo trạng thái tích lũy toàn cục xuyên suốt cả 3 màn chơi
    if "game_state_global" not in request.session:
        request.session["game_state_global"] = {
            "total_score_earned": 0,
            "total_correct_count": 0,
            "total_q_count": 0
        }

    # 2. Khởi tạo danh sách câu hỏi cho riêng Level hiện tại nếu chưa có
    if "game_state" not in request.session or request.session["game_state"]["level"] != level:
        all_questions = GameQuestion.objects.filter(level=level).order_by('id')

        if level == "easy":
            # Lấy 3 câu trắc nghiệm đầu tiên cho màn Easy
            selected_qs = list(all_questions.filter(question_type="multiple_choice")[:3])
        elif level == "medium":
            # Màn Medium: 2 câu đầu trắc nghiệm, 2 câu sau kéo thả điền khuyết
            choices = list(all_questions.filter(question_type="multiple_choice")[:2])
            drags = list(all_questions.filter(question_type="drag_drop_blank")[:2])
            selected_qs = choices + drags
        elif level == "hard":
            # Lấy 3 câu sắp xếp dòng cho màn Hard
            selected_qs = list(all_questions.filter(question_type="sort_code")[:3])
        else:
            selected_qs = list(all_questions[:3])

        if not selected_qs:
            messages.warning(request, f"Hệ thống chưa cấu hình đủ câu hỏi cho nhóm {level.upper()}!")
            return redirect("game_home")

        request.session["game_state"] = {
            "level": level,
            "q_ids": [q.id for q in selected_qs],
            "current_index": 0,
        }
        # Cộng dồn số câu hỏi của chặng này vào tổng số câu toàn chặng
        request.session["game_state_global"]["total_q_count"] += len(selected_qs)
        request.session.modified = True

    state = request.session["game_state"]
    global_state = request.session["game_state_global"]
    q_ids = state["q_ids"]
    current_idx = state["current_index"]

    # Kiểm tra an toàn: Nếu chỉ số vượt quá số lượng câu hỏi của màn hiện tại
    if current_idx >= len(q_ids):
        if level == "easy":
            return redirect("play_game", level="medium")
        elif level == "medium":
            return redirect("play_game", level="hard")
        else:
            return redirect("game_result")

    # Lấy đối tượng câu hỏi hiện tại dựa trên model GameQuestion
    question = get_object_or_404(GameQuestion, id=q_ids[current_idx])

    # 3. Xử lý khi người chơi ấn Nộp đáp án (POST)
    if request.method == "POST":
        is_correct = False
        user_ans = request.POST.get('answer', '').strip().upper()  # Dành cho trắc nghiệm
        custom_ans = request.POST.get('custom_answer', '').strip()  # Dành cho kéo thả / sắp xếp

        # --- CHẤM ĐIỂM TYPE 1: TRẮC NGHIỆM ---
        if question.question_type == 'multiple_choice':
            if user_ans == (question.correct_option or '').upper():
                is_correct = True
            correct_display = question.correct_option

        # --- CHẤM ĐIỂM TYPE 2: KÉO THẢ ĐIỀN KHUYẾT (MEDIUM) ---
        elif question.question_type == 'drag_drop_blank':
            if custom_ans and question.blank_answers:
                # Loại bỏ khoảng trắng thừa để so sánh chính xác chuỗi ngăn cách bởi dấu phẩy
                u_clean = ",".join([i.strip() for i in custom_ans.split(",")])
                c_clean = ",".join([i.strip() for i in question.blank_answers.split(",")])
                if u_clean == c_clean:
                    is_correct = True
            correct_display = question.blank_answers

        # --- CHẤM ĐIỂM TYPE 3: SẮP XẾP DÒNG CODE (HARD) ---
        elif question.question_type == 'sort_code':
            if custom_ans and question.correct_lines_order:
                # Loại bỏ toàn bộ khoảng trống để tránh lỗi định dạng thụt lề đầu dòng
                u_clean = "".join(custom_ans.split())
                c_clean = "".join(question.correct_lines_order.split())
                if u_clean == c_clean:
                    is_correct = True
            correct_display = "Vui lòng xem thứ tự cấu trúc code chuẩn trên màn hình kết quả!"

        # Cộng điểm tích lũy toàn cục nếu trả lời đúng
        if is_correct:
            global_state["total_score_earned"] += 10
            global_state["total_correct_count"] += 1
            request.session.modified = True

        # Tăng chỉ số câu hỏi lên 1 câu tiếp theo
        state["current_index"] += 1
        request.session["game_state"] = state
        request.session.modified = True

        # Xác định bước chuyển tiếp tiếp theo hiển thị tại màn trung gian kết quả câu hỏi
        if state["current_index"] >= len(q_ids):
            if level == "easy":
                next_action = "medium"
                is_route_level = True
            elif level == "medium":
                next_action = "hard"
                is_route_level = True
            else:
                next_action = "result"
                is_route_level = False
        else:
            next_action = level
            is_route_level = False

        return render(request, "game/result.html", {
            "is_final": False,
            "is_correct": is_correct,
            "correct_answer": correct_display,
            "next_level": next_action,
            "is_route_level": is_route_level,
            "score_earned": global_state["total_score_earned"]
        })

    return render(request, "game/play.html", {
        "question": question,
        "level": level,
        "index": current_idx + 1,
        "total_q": len(q_ids),
        "score_earned": global_state["total_score_earned"]
    })


@login_required(login_url='login')
def game_result(request):
    global_state = request.session.get("game_state_global")
    if not global_state:
        return redirect("game_home")

    score_earned = global_state["total_score_earned"]
    correct_count = global_state["total_correct_count"]
    total_q = global_state["total_q_count"]

    # Lưu kết quả chơi game vào bảng Score lịch sử của hệ thống
    Score.objects.create(
        user=request.user,
        score=score_earned,
        total_correct=correct_count,
        total_question=total_q
    )

    # Khởi tạo hoặc tìm danh mục "Sách Lập Trình" đồng bộ với logic cũ của bạn
    prog_cat, _ = Category.objects.get_or_create(name="Sách Lập Trình")
    code_gen = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))

    # Tạo voucher lưu trực tiếp vào cơ sở dữ liệu
    voucher = Voucher.objects.create(
        user=request.user,
        code=f"CPP-{code_gen}",
        discount_percent=10,
        applicable_category=prog_cat
    )

    # Giải phóng hoàn toàn các session lưu vết đợt chơi game này
    if "game_state" in request.session:
        del request.session["game_state"]
    if "game_state_global" in request.session:
        del request.session["game_state_global"]

    return render(request, "game/result.html", {
        "is_final": True,
        "score_earned": score_earned,
        "correct_count": correct_count,
        "voucher": voucher
    })


# =======================================================
#             HỆ THỐNG XỬ LÝ GAME ĐUA XE CON TRỎ C++
# =======================================================

@login_required(login_url='login')
def pointer_game_home(request):
    """ Trang sảnh chính chuẩn bị đua xe """
    return render(request, "game_pointer/arena.html")


@login_required(login_url='login')
def get_pointer_questions_api(request, level):
    """ API lấy toàn bộ câu hỏi của Level được chọn để JS xử lý realtime """
    questions = PointerGameQuestion.objects.filter(level=level).order_by('id')
    data = []
    for q in questions:
        data.append({
            "id": q.id,
            "title": q.title,
            "code": q.code_context if q.code_context else "",
            "options": [q.option_1, q.option_2, q.option_3, q.option_4, q.option_5, q.option_6],
            "correct": q.correct_option
        })
    return JsonResponse({"status": "success", "level": level, "questions": data})


@login_required(login_url='login')
def pointer_game_finish_api(request):
    """ API cứu cánh khi hoàn thành cả 3 level, tạo Voucher cộng dồn 10% """
    if request.method == "POST":
        # Tạo bản ghi lưu lịch sử phá đảo game
        PointerGameScore.objects.create(user=request.user, has_won=True)

        # Đồng bộ tạo Voucher giảm giá 10% cho danh mục Sách Lập Trình
        prog_cat, _ = Category.objects.get_or_create(name="Sách Lập Trình")
        code_gen = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))

        voucher = Voucher.objects.create(
            user=request.user,
            code=f"PTR-{code_gen}",
            discount_percent=10,
            applicable_category=prog_cat
        )

        return JsonResponse({
            "status": "success",
            "message": "Chúc mừng bạn đã hoàn thành đường đua xuất sắc!",
            "voucher_code": voucher.code,
            "discount": voucher.discount_percent
        })
    return JsonResponse({"status": "error", "message": "Yêu cầu bất hợp lệ!"})



#
# @login_required(login_url='login')
# def game_home(request):
#     # Dọn dẹp session game cũ khi quay lại sảnh chính
#     if "game_state" in request.session:
#         del request.session["game_state"]
#     if "game_state_global" in request.session:
#         del request.session["game_state_global"]
#
#     scores = Score.objects.filter(user=request.user)
#     total = sum(s.score for s in scores)
#     return render(request, "game/home.html", {"total": total})
#
#
# @login_required(login_url='login')
# def play_game(request, level):
#     level = level.lower()
#
#     # Khởi tạo điểm tích lũy toàn cục (xuyên suốt Easy -> Medium -> Hard) nếu chưa có
#     if "game_state_global" not in request.session:
#         request.session["game_state_global"] = {
#             "total_score_earned": 0,
#             "total_correct_count": 0,
#             "total_q_count": 0
#         }
#
#     # Khởi tạo trạng thái của riêng Level hiện tại
#     if "game_state" not in request.session or request.session["game_state"]["level"] != level:
#         all_questions = list(Question.objects.filter(level=level).order_by('id'))
#
#         if level == "easy":
#             selected_qs = [q for q in all_questions if q.question_type == "choice"][:3]
#         elif level == "medium":
#             choices = [q for q in all_questions if q.question_type == "choice"][:2]
#             drags = [q for q in all_questions if q.question_type == "drag"][:2]
#             selected_qs = choices + drags
#         elif level == "hard":
#             selected_qs = [q for q in all_questions if q.question_type == "sort"][:3]
#         else:
#             selected_qs = all_questions[:3]
#
#         if not selected_qs:
#             messages.warning(request, f"Hệ thống chưa cấu hình đủ câu hỏi cho nhóm {level.upper()}!")
#             return redirect("game_home")
#
#         request.session["game_state"] = {
#             "level": level,
#             "q_ids": [q.id for q in selected_qs],
#             "current_index": 0,
#         }
#         # Cộng dồn số lượng câu hỏi của cấp độ này vào tổng số câu toàn chặng
#         request.session["game_state_global"]["total_q_count"] += len(selected_qs)
#         request.session.modified = True
#
#     state = request.session["game_state"]
#     global_state = request.session["game_state_global"]
#     q_ids = state["q_ids"]
#     current_idx = state["current_index"]
#
#     # BIỆN PHÁP CHẶN AN TOÀN: Nếu chỉ số vượt mức câu hỏi, điều hướng ngay chặng tiếp theo
#     if current_idx >= len(q_ids):
#         if level == "easy":
#             return redirect("play_game", level="medium")
#         elif level == "medium":
#             return redirect("play_game", level="hard")
#         else:
#             return redirect("game_result")
#
#     question = get_object_or_404(Question, id=q_ids[current_idx])
#
#     if request.method == "POST":
#         user_answer = request.POST.get("answer", "").strip().upper()
#         # Hỗ trợ dạng nhập chuỗi liền nhau hoặc có gạch ngang cho câu sắp xếp (Hard)
#         if question.question_type == "sort":
#             user_answer = user_answer.replace("-", "")
#             correct_ans = question.correct.upper().replace("-", "")
#         else:
#             correct_ans = question.correct.upper()
#
#         is_correct = (user_answer == correct_ans)
#
#         if is_correct:
#             global_state["total_score_earned"] += 10
#             global_state["total_correct_count"] += 1
#             request.session.modified = True
#
#         # Tăng chỉ số index lên 1 câu câu hỏi tiếp theo
#         state["current_index"] += 1
#         request.session["game_state"] = state
#         request.session.modified = True
#
#         # Xác định nút chuyển tiếp tiếp theo hiển thị ở trang trung gian kết quả câu hỏi
#         if state["current_index"] >= len(q_ids):
#             if level == "easy":
#                 next_action = "medium"
#                 is_route_level = True
#             elif level == "medium":
#                 next_action = "hard"
#                 is_route_level = True
#             else:
#                 next_action = "result"
#                 is_route_level = False
#         else:
#             next_action = level
#             is_route_level = False
#
#         # Hiển thị trang kết quả trung gian thông báo Đúng/Sai từng câu
#         return render(request, "game/result.html", {
#             "is_final": False,
#             "is_correct": is_correct,
#             "correct_answer": question.correct,
#             "next_level": next_action,
#             "is_route_level": is_route_level,
#             "score_earned": global_state["total_score_earned"]
#         })
#
#     return render(request, "game/play.html", {
#         "question": question,
#         "level": level,
#         "index": current_idx + 1,
#         "total_q": len(q_ids),
#         "score_earned": global_state["total_score_earned"]
#     })
#
#
# @login_required(login_url='login')
# def game_result(request):
#     global_state = request.session.get("game_state_global")
#     if not global_state:
#         return redirect("game_home")
#
#     score_earned = global_state["total_score_earned"]
#     correct_count = global_state["total_correct_count"]
#     total_q = global_state["total_q_count"]
#
#     # Ghi nhận thành tích cuối cùng vào lịch sử điểm của sinh viên
#     Score.objects.create(
#         user=request.user,
#         score=score_earned,
#         total_correct=correct_count,
#         total_question=total_q
#     )
#
#     # Cấp phát Voucher 10% cho danh mục "Sách Lập Trình"
#     prog_cat, _ = Category.objects.get_or_create(name="Sách Lập Trình")
#     code_gen = "".join(random.choices(string.ascii_uppercase + string.digits, k=10))
#     voucher = Voucher.objects.create(
#         user=request.user,
#         code=f"CPP-{code_gen}",
#         discount_percent=10,
#         applicable_category=prog_cat
#     )
#
#     # Giải phóng hoàn toàn bộ nhớ đệm session của đợt chơi game này
#     if "game_state" in request.session:
#         del request.session["game_state"]
#     if "game_state_global" in request.session:
#         del request.session["game_state_global"]
#
#     return render(request, "game/result.html", {
#         "is_final": True,
#         "score_earned": score_earned,
#         "correct_count": correct_count,
#         "voucher": voucher
#     })
#
#
#
#
#
# # Giả lập hoặc dùng Session để lưu trữ thông tin màn chơi hiện tại của User
# def play_game_view(request, level='easy'):
#     # Khởi tạo trạng thái bộ câu hỏi trong Session nếu là lượt chơi mới
#     if 'game_questions_ids' not in request.session or request.GET.get('restart'):
#         # Lọc cấu trúc: Easy lấy 3 câu, Medium lấy 4 câu (2 trắc nghiệm, 2 kéo thả), Hard lấy toàn bộ
#         if level == 'easy':
#             q_ids = list(GameQuestion.objects.filter(level='easy').values_list('id', flat=True)[:3])
#         elif level == 'medium':
#             # Bạn có thể sắp xếp ID trong Admin sao cho 2 câu trắc nghiệm xếp trước, 2 câu kéo thả xếp sau
#             q_ids = list(GameQuestion.objects.filter(level='medium').values_list('id', flat=True)[:4])
#         else:
#             q_ids = list(GameQuestion.objects.filter(level='hard').values_list('id', flat=True))
#
#         request.session['game_questions_ids'] = q_ids
#         request.session['current_index'] = 0
#         request.session['score_earned'] = 0
#
#     q_ids = request.session.get('game_questions_ids', [])
#     current_idx = request.session.get('current_index', 0)
#     score_earned = request.session.get('score_earned', 0)
#
#     # Nếu đã trả lời hết bộ câu hỏi của Level này
#     if current_idx >= len(q_ids):
#         if level == 'easy':
#             return redirect('game_result_route', next_level='medium')  # Chuyển tiếp màn
#         elif level == 'medium':
#             return redirect('game_result_route', next_level='hard')
#         else:
#             return redirect('game_final_result')  # Thắng cuộc hoàn toàn -> Nhận voucher
#
#     # Lấy câu hỏi hiện tại ra xử lý
#     question = get_object_or_404(GameQuestion, id=q_ids[current_idx])
#
#     if request.method == 'POST':
#         is_correct = False
#         user_ans = request.POST.get('answer')  # Dành cho Trắc nghiệm
#         custom_ans = request.POST.get('custom_answer')  # Dành cho Điền khuyết / Sắp xếp dòng
#
#         # 1. Chấm điểm Trắc Nghiệm
#         if question.question_type == 'multiple_choice':
#             if user_ans == question.correct_option:
#                 is_correct = True
#
#         # 2. Chấm điểm Điền khuyết (Medium)
#         elif question.question_type == 'drag_drop_blank':
#             # So sánh chuỗi đáp án phân tách bằng dấu phẩy
#             if custom_ans and question.blank_answers:
#                 if custom_ans.strip() == question.blank_answers.strip():
#                     is_correct = True
#
#         # 3. Chấm điểm Sắp xếp dòng code (Hard)
#         elif question.question_type == 'sort_code':
#             # So sánh chuỗi thứ tự dòng code ghép bởi dấu "||"
#             if custom_ans and question.correct_lines_order:
#                 if custom_ans.replace(" ", "") == question.correct_lines_order.replace(" ", ""):
#                     is_correct = True
#
#         # Cập nhật điểm số
#         if is_correct:
#             request.session['score_earned'] = score_earned + 10
#
#         # Tăng index để chuyển sang câu tiếp theo ở lượt sau
#         request.session['current_index'] = current_idx + 1
#
#         # Trả về kết quả giao diện đúng/sai trung gian
#         return render(request, 'game/result.html', {
#             'is_correct': is_correct,
#             'correct_answer': question.correct_option if question.question_type == 'multiple_choice' else (
#                 question.blank_answers if question.question_type == 'drag_drop_blank' else "Xem thứ tự code chuẩn tại tài liệu"),
#             'next_level': level
#         })
#
#     return render(request, 'game/play.html', {
#         'question': question,
#         'index': current_idx + 1,
#         'total_q': len(q_ids),
#         'score_earned': score_earned
#     })


