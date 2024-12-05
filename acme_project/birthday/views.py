# from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (ListView, CreateView, UpdateView,
                                  DeleteView, DetailView)
from django.urls import reverse_lazy

from .forms import BirthdayForm
from .utils import calculate_birthday_countdown
from .models import Birthday


class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 10


class BirthdayCreateView(CreateView):
    model = Birthday
    form_class = BirthdayForm


class BirthdayUpdateView(UpdateView):
    model = Birthday
    form_class = BirthdayForm


class BirthdayDeleteView(DeleteView):
    model = Birthday
    success_url = reverse_lazy('birthday:list')


class BirthdayDetailView(DetailView):
    model = Birthday

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['birthday_countdown'] = calculate_birthday_countdown(
            self.object.birthday
        )
        return context


# def birthday(request, id=None):
#     template = 'birthday/birthday.html'
#     if id is not None:
#         instance = get_object_or_404(Birthday, id=id)
#     else:
#         instance = None
#     form = BirthdayForm(
#         request.POST or None,
#         files=request.FILES or None,
#         instance=instance
#     )
#     context = {'form': form}
#     if form.is_valid():
#         form.save()
#         birthday_countdown = calculate_birthday_countdown(
#             form.cleaned_data['birthday']
#         )
#         context.update({'birthday_countdown': birthday_countdown})
#     return render(request, template, context)


# def birthday_list(request):
#     template = 'birthday/birthday_list.html'
#     birthdays = Birthday.objects.order_by('id')
#     paginator = Paginator(birthdays, 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {'page_obj': page_obj}
#     return render(request, template, context)


# def delete_birthday(request, id):
#     template = 'birthday/birthday.html'
#     instance = get_object_or_404(Birthday, id=id)
#     form = BirthdayForm(instance=instance)
#     context = {'form': form}
#     if request.method == 'POST':
#         instance.delete()
#         return redirect('birthday:list')
#     return render(request, template, context)
