from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse
from .forms import ContactUsForm
from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
    FormView,
    UpdateView,
    DeleteView
)
from .models import (
    Questionnaire,
)

# Create your views here.


@login_required
def home(request):
    return render(request, 'blog/home.html')


class ReportListView(LoginRequiredMixin, ListView):
    model = Questionnaire
    template_name = 'blog/report_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'reports'
    ordering = ['-date_posted']

    def get_queryset(self):
        user = self.request.user
        return Questionnaire.objects.filter(author=user)


class ReportDetailView(LoginRequiredMixin, DetailView):
    model = Questionnaire  # <app>/<model>_<viewtype>.html
    context_object_name = 'report'


class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Questionnaire  # <app>/<model>_form.html
    fields = ['nilai_satu', 'keterangan_satu', 'rekomendasi_satu',
              'nilai_dua', 'keterangan_dua', 'rekomendasi_dua',
              'nilai_tiga', 'keterangan_tiga', 'rekomendasi_tiga',
              'nilai_empat', 'keterangan_empat', 'rekomendasi_empat',
              'nilai_lima', 'keterangan_lima', 'rekomendasi_lima',
              'nilai_enam', 'keterangan_enam', 'rekomendasi_enam', ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ReportUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Questionnaire  # <app>/<model>_form.html
    context_object_name = 'report'
    fields = ['nilai_satu', 'keterangan_satu', 'rekomendasi_satu',
              'nilai_dua', 'keterangan_dua', 'rekomendasi_dua',
              'nilai_tiga', 'keterangan_tiga', 'rekomendasi_tiga',
              'nilai_empat', 'keterangan_empat', 'rekomendasi_empat',
              'nilai_lima', 'keterangan_lima', 'rekomendasi_lima',
              'nilai_enam', 'keterangan_enam', 'rekomendasi_enam', ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        questionnaire = self.get_object()
        if self.request.user == questionnaire.author:
            return True
        return False


class ReportDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Questionnaire  # <app>/<model>_<viewtype>.html
    context_object_name = 'report'
    success_url = '/report'

    def test_func(self):
        questionnaire = self.get_object()
        if self.request.user == questionnaire.author:
            return True
        return False


def about(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Terima kasih telah menghubungi One Health Laboratory')
    else:
        form = ContactUsForm()
    return render(request, 'blog/about.html', {'form': form})
