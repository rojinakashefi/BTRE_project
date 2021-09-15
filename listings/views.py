from django.shortcuts import get_object_or_404, render
from .models import Listing
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .choices import bedroom_choices,price_choices,state_choices
# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True )
    paginator = Paginator(listings,6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {'listings':paged_listings}
    return render(request,'listings/listings.html',context)

def listing(request,listing_id):
    listing = get_object_or_404(Listing,pk=listing_id) 
    context = {'listing':listing}
    return render(request,'listings/listing.html',context)

def search(request):
    queryset_list = Listing.objects.order_by('-list_date').filter(is_published = True)
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword :
            queryset_list = queryset_list.filter(description__icontains=keyword)
    if 'city' in request.GET:
        city = request.GET['city']
        if city :
            queryset_list = queryset_list.filter(city__iexact=city)
    if 'state' in request.GET:
        state = request.GET['state']
        if state :
            queryset_list = queryset_list.filter(state__iexact=state)
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms :
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms )
    if 'price' in request.GET:
        price = request.GET['price']
        if price :
            queryset_list = queryset_list.filter(price__lte=price )

    context = {
    'price_choices':price_choices,
    'state_choices':state_choices,
    'bedroom_choices':bedroom_choices,
    'listings':queryset_list,
    'values':request.GET
    }
    return render(request,'listings/search.html',context)
