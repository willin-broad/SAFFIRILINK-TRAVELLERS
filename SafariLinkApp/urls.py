from django.template.context_processors import static
from django.urls import path

from SafiriLink import settings
from . import views, admin
from .views import index_view,dashboard_view,register_view,login_view,book_view, daraja_view,home_view,logout_view,callback_view,AboutUs_view

urlpatterns = [
    path('SafariLinkApp/', views.safariLinkApp, name='SafariLinkApp'),
    path('', index_view, name='index'),  # Home page redirects to index.html
    path('dashboard/', dashboard_view, name='dashboard'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('book/', book_view, name='booki'),
    path('homeDashboard/', home_view, name='home'),
    path('daraja_view/',daraja_view, name='daraja'),
    path('logout/', logout_view, name='logout'),
    path('book_view/', views.book_view, name='book'),
    path('booking_receipt/', views.booking_receipt, name='receipt'),
    path('contact/', views.contact_view, name='contact'),
    path('notifications/', views.notifications_view, name='notifications'),
    path('e-citizen/', views.e_citizen_view, name='e_citizen'),
    path('callback/', callback_view, name='callback'),
    path('aboutUs',AboutUs_view,name='aboutUs'),
    # path('bookForm',bookForm_view,name='bookingForm'),

    path('edit-booking/<int:bus_id>/', views.edit_booking, name='edit_booking'),
    path('delete-booking/<int:bus_id>/', views.delete_booking, name='delete_booking'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



    # path('password/',views.passwordChangeView,name='passChange')
    # 