# """
# URL configuration for project_lib project.
#
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/6.0/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path
#
# from django.contrib import admin
# from django.urls import path
#
# from firstApp import views
#
# from django.conf import settings
# from django.conf.urls.static import static
# urlpatterns = [
#     path('admin/', admin.site.urls),
#
#     path('', views.index, name='home'),
#
#     path('about/', views.about, name='about'),
#
#     path('books/', views.books, name='books'),
# path("register/", views.register, name="register"),
# path("login/", views.user_login, name="login"),
# path("logout/", views.user_logout, name="logout"),
# path(
#     "profile/",
#     views.profile,
#     name="profile"
# ),
# path(
#     "book/<int:id>/",
#     views.book_detail,
#     name="book_detail"
# ),
# path('dashboard/', views.student_dashboard, name='dashboard'),
# path('book/<int:id>/borrow/', views.borrow_book, name='borrow_book'),
# path('cart/', views.view_cart, name='view_cart'),
# path('cart/add/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
# path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
# path('cart/update/<int:item_id>/', views.update_cart_quantity, name='update_cart_quantity'),
# path("search-books/",views.search_books,name="search_books"),
# path("game/",views.game_home,name="game_home"),
# path("game/<str:level>/",views.play_game,name="play_game"),
# path("game/result/", views.game_result, name="game_result"),
# ]
# # Cho phép đọc ảnh trong media khi chạy Development Server
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,
#                           document_root=settings.MEDIA_ROOT)
"""
URL configuration for project_lib project.
"""
from django.contrib import admin
from django.urls import path
from firstApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('books/', views.books, name='books'),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("book/<int:id>/", views.book_detail, name="book_detail"),
    path('dashboard/', views.student_dashboard, name='dashboard'),
    path('book/<int:id>/borrow/', views.borrow_book, name='borrow_book'),
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/add/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:item_id>/', views.update_cart_quantity, name='update_cart_quantity'),
    path("search-books/", views.search_books, name="search_books"),

    # === KHU VỰC ĐỒNG BỘ GAME (ĐÃ ĐỔI THỨ TỰ ƯU TIÊN) ===
    path("game/", views.game_home, name="game_home"),
    path("game/result/", views.game_result, name="game_result"),  # Đã đưa lên trên tham số level
    path("game/<str:level>/", views.play_game, name="play_game"),

path('game-pointer/', views.pointer_game_home, name='pointer_game_home'),
    path('game-pointer/api/questions/<int:level>/', views.get_pointer_questions_api, name='pointer_questions_api'),
    path('game-pointer/api/finish/', views.pointer_game_finish_api, name='pointer_game_finish_api'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)