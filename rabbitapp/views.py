from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import FormView, ListView, DetailView
from django.urls import reverse_lazy
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage

from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import RabbitPost, Cart, Record

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

# 問い合わせページを表示するビュー
class ContactView(FormView):
    template_name ='contact.html'
    form_class= ContactForm
    success_url = reverse_lazy('rabbitapp:contact')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']

        subject = 'お問い合わせ: {}'.format(title)
        message = \
            '送信者名：{0}\nメールアドレス：{1}\nタイトル：{2}\nメッセージ：\n{3}'\
                .format(name, email, title, message)
        from_email = 'abc@example.com'
        to_list = ['abc@example.com']
        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list,)
        message.send()
        messages.success(self.request, 'お問い合わせは正常に送信しましたよ！')
        return super().form_valid(form=form)


class ShopView(ListView):
    template_name ='shop.html'
    queryset = RabbitPost.objects.order_by('posted_at')
    paginate_by = 4

@method_decorator(csrf_exempt, name='dispatch')
class AddToCartView(View):
    def post(self, request, *args, **kwargs):
        rabbit_post_id = request.POST.get('rabbit_post_id')  # Assuming you pass the RabbitPost ID from the frontend
        rabbit_post = RabbitPost.objects.get(pk=rabbit_post_id)
        user = request.user

        # 対象アイテム存在するのか確認
        existing_cart_entry = Cart.objects.filter(
            title=rabbit_post.title,
            user=user
        ).first()

        if rabbit_post.qty > 0:
            if existing_cart_entry: # もしカートに同じもの存在してる場合
                existing_cart_entry.qty += 1
                existing_cart_entry.save()
            else: # カートにアイテムが存在しない場合は、新しいアイテムを追加する
                Cart.objects.create(
                    title=rabbit_post.title,
                    price=rabbit_post.price,
                    qty=1,
                    user=request.user,
                )
            # ショップの対象アイテムの数量減少
            rabbit_post.qty -= 1
            rabbit_post.save()

            return JsonResponse({'message': 'Item added to cart successfully.', 'instock': True})
        else: 
            return JsonResponse({'message': 'Item is out of stock.', 'instock': False})

    def get(self, request, *args, **kwargs):
        return JsonResponse({'message': 'Invalid request method.'}, status=400)

class DetailView(DetailView):
    template_name = 'detail.html'
    model = RabbitPost

class CartView(ListView):
    template_name = 'cart.html'
    model = RabbitPost
    context_object_name = 'cart_items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username

        # Calculate total price for each item
        for record in context['cart_items']:
            record.amount = record.price * record.qty

        total_amount = sum(record.price * record.qty for record in context['cart_items'])
        context['total_amount'] = total_amount

        return context

    def get_queryset(self):
        # Retrieve cart items for the currently logged-in user
        return Cart.objects.filter(user=self.request.user)
    
class GoToRecordView(View):
    def post(self, request, *args, **kwargs):
        cart_id = request.POST.get('cart_id')  # Assuming you pass the cart ID from the frontend
        try:
            cart_item = Cart.objects.get(pk=cart_id, user=request.user)
        except Cart.DoesNotExist:
            return JsonResponse({'message': 'Error buying. Cart item not found.'}, status=400)

        # Move items from the Cart to the Record
        Record.objects.create(
            title=cart_item.title,
            qty=cart_item.qty,
            price=cart_item.price,
            user=request.user,  # Set the user for the Record
        )

        # Clear the Cart for the current user
        cart_item.delete()

        # Redirect to a success page or another appropriate page
        return JsonResponse({'message': 'Bought already, thanks for your support!'})

class RecordView(ListView):
    template_name = 'record.html'
    model = RabbitPost
    context_object_name = 'record_items'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username

        # Calculate total price for each item
        for record in context['record_items']:
            record.amount = record.price * record.qty

        return context
    
    def get_queryset(self):
        # Retrieve cart items for the currently logged-in user
        return Record.objects.filter(user=self.request.user)
