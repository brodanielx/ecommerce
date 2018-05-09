from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from analytics.signals import object_viewed_signal
from carts.models import Cart

from .models import Product



class ProductFeaturedListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self, ):
        request = self.request
        return Product.objects.all().featured()

class ProductFeaturedDetailView(DetailView):
    template_name = "products/featured-detail.html"

    def get_queryset(self, ):
        request = self.request
        return Product.objects.all().featured()

class ProductListView(ListView):
    template_name = "products/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_queryset(self, ):
        request = self.request
        return Product.objects.all()

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'products/list.html', context)


class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')

        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404('Not found')
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404('other error')

        # object_viewed_signal.send(instance.__class__, instance=instance, request=request)
        return instance

class ProductDetailView(DetailView):
    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance is None:
            raise Http404('product does not exist**')
        return instance

def product_detail_view(request, pk=None, *args, **kwargs):
    # instance = Product.objects.get(pk=pk)
    # instance = get_object_or_404(Product, pk=pk)
    # try:
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print('no product here')
    #     raise Http404('product does not exist')
    # except:
    #     print('error')

    instance = Product.objects.get_by_id(pk)
    if instance is None:
        raise Http404('product does not exist**')

    context = {
        'object': instance
    }
    return render(request, 'products/detail.html', context)
