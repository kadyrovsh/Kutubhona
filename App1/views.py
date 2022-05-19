from django.shortcuts import render, redirect
from .models import *

def all_students(request):
    if request.method == "POST":
        Student.objects.create(
            ism=request.POST.get("i"),
            guruh=request.POST.get("g"),
            kitob_soni=request.POST.get("k_s")
        )
        return redirect("/talabalar/")
    talabalar = Student.objects.all()
    return render(request, "students.html", {"Studentlar" : talabalar})

def all_books(request):
    kitoblar = Kitob.objects.all()
    sahifa = Kitob.objects.order_by("-sahifa")[:3]
    return render(request, "books.html", {"kitoblar" : kitoblar, "sahifasi_kop" : sahifa})

def all_mualliflar(request):
    if request.method == "POST":
        Muallif.objects.create(
            ism=request.POST.get("i"),
            yosh=request.POST.get("y"),
            kitoblar_soni=request.POST.get("k_s"),
            trik=request.POST.get("live"),
            jins=request.POST.get("jins")
        )
        return redirect("/mualliflar/")
    muallflar = Muallif.objects.all()
    kitobi_kop = Muallif.objects.order_by("-kitoblar_soni")[:3]
    return render(request, "muallif.html", {"mualliflar" : muallflar, "kitobi_kop" : kitobi_kop})

def all_records(request):
    if request.method == "POST":
        Record.objects.create(
            student = Student.objects.get(id=request.POST.get("s")),
            kitob = Kitob.objects.get(id=request.POST.get("k")),
            sana = request.POST.get("sana"),
            qaytardi = request.POST.get("q"),
            qaytarish_sana = request.POST.get("q_s")
        )
        return redirect("/recordlar/")
    data = {
        "records": Record.objects.all(),
        "talabalar": Student.objects.all(),
        "kitoblar": Kitob.objects.all()
    }
    return render(request, "record.html", data)

def Student_ochir(requests, pk):
    Student.objects.get(id=pk).delete()
    return redirect("/talabalar/")

def muallif_ochir(requests, m):
    Muallif.objects.filter(id=m).delete()
    return redirect("/mualliflar/")

def record_ochir(requests, r):
    Record.objects.filter(id=r).delete()
    return redirect("/recordlar/")

def tan_student(request):
    data = {
        "st" : Student.objects.all().first()
    }
    return render(request, "student.html", data)

def student_edit(request, pk):
    if request.method == "POST":
        Student.objects.filter(id=pk).update(
            ism=request.POST.get("i"),
            guruh=request.POST.get("g"),
            kitob_soni=request.POST.get("k_s")
        )
        return redirect("/talabalar/")
    data = {
        "s": Student.objects.get(id=pk)
    }
    return render(request, "st_edit.html", data)

def muallif_edit(request, pk):
    if request.method == "POST":
        Muallif.objects.filter(id=pk).update(
            ism = request.POST.get("i"),
            yosh = request.POST.get("y"),
            kitoblar_soni = request.POST.get("k_s"),
            jins = request.POST.get("j")
        )
        return redirect("/mualliflar/")
    data = {
        "m" : Muallif.objects.get(id=pk)
    }
    return render(request, "muallif_edit.html", data)

def kitob_edit(request, pk):
    if request.method == "POST":
        Kitob.objects.filter(id=pk).update(
            nom = request.POST.get("n"),
            muallif = request.POST.get("m"),
            sahifa = request.POST.get("s"),
            janr = request.POST.get("j")
        )
        return redirect("/kitoblar/")
    data = {
        "k": Kitob.objects.get(id=pk),
        "mualliflar": Muallif.objects.all()
    }
    return render(request, "kitob_edit.html", data )