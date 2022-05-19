
from django.contrib import admin
from django.urls import path
from App1.views import all_students, all_books, all_mualliflar, all_records, Student_ochir, muallif_ochir, record_ochir, tan_student, student_edit, muallif_edit, kitob_edit


urlpatterns = [
    path('admin/', admin.site.urls),
    path('talabalar/', all_students),
    path('kitoblar/', all_books),
    path('mualliflar/', all_mualliflar),
    path('recordlar/', all_records),
    path('student/<int:pk>/', Student_ochir),
    path('muallif/<int:m>/', muallif_ochir),
    path('record/<int:r>/', record_ochir),
    path('talaba/', tan_student),
    path('student/<int:pk>/edit/', student_edit),
    path('muallif/<int:pk>/edit/', muallif_edit),
    path('kitob/<int:pk>/edit/', kitob_edit),
]


