from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.http import JsonResponse, Http404
from .models import Article, Source, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@cache_page(60 * 5)
def init_articles(request):
    articles = Article.objects.all()

    page_number = request.GET.get('page')
    if page_number is not None:  # Check if page number is provided
        paginator = Paginator(articles, 50)  # Paginate with 50 articles per page
        try:
            page_articles = paginator.page(page_number)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page
            page_articles = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g., 9999), deliver last page
            page_articles = paginator.page(paginator.num_pages)

        data = [
                {
                        'title': article.title,
                        'description': article.description,
                        'url': article.url,
                        'url_to_image': article.url_to_image,
                        'source': article.source.name if article.source else 'undefined',
                        'source_url': article.source.url if article.source else 'undefined',
                        'author': article.author,
                        'published_at': article.published_at,
                        'category': article.category.name if article.category else 'undefined'
                } 
                for article in page_articles
                ]
    else:
        # If no page number is provided, return all articles
        data = [
                {
                        'title': article.title,
                        'description': article.description,
                        'url': article.url,
                        'url_to_image': article.url_to_image,
                        'source': article.source.name if article.source else 'undefined',
                        'source_url': article.source.url if article.source else 'undefined',
                        'author': article.author,
                        'published_at': article.published_at,
                        'category': article.category.name if article.category else 'undefined'
                } 
                for article in articles
                ]

    return JsonResponse(data, safe=False)


def getArticleById(request, id):
    try:
        article = Article.objects.get(pk=id)
    except Article.DoesNotExist:
        raise Http404("Article does not exist")

    data = {
        'title': article.title,
        'description': article.description,
        'url': article.url,
        'url_to_image': article.url_to_image,
        'source': article.source.name if article.source else 'undefined',
        'source_url': article.source.url if article.source else 'undefined',
        'author': article.author,
        'published_at': article.published_at,
        'category': article.category.name if article.category else 'undefined'
    }

    return JsonResponse(data)

def init_sources(request):
    sources = Source.objects.all()
    data = [{'name': source.name, 'description': source.description, 'url': source.url} for source in sources]
    return JsonResponse(data, safe=False)

def init_categories(request):
    categories = Category.objects.all()
    data = [{'id': category.id,'name': category.name} for category in categories]
    return JsonResponse(data, safe=False)

# Cache the articles by category view for 5 minutes
@cache_page(60 * 5)
def articles_by_category(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
    except:
        raise Http404("Source matching query does not exist")
    articles = Article.objects.filter(category=category)
    paginator = Paginator(articles, 50)  # Paginate with 50 articles per page

    page_number = request.GET.get('page')
    try:
        page_articles = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        page_articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page
        page_articles = paginator.page(paginator.num_pages)

    data = [
        {
                'title': article.title,
                'description': article.description,
                'url': article.url,
                'url_to_image': article.url_to_image,
                'source': article.source.name if article.source else 'undefined',
                'source_url': article.source.url if article.source else 'undefined',
                'author': article.author,
                'published_at': article.published_at,
                'category': article.category.name if article.category else 'undefined'
        } 
        for article in page_articles
        ]
    return JsonResponse(data, safe=False)

def articles_by_category_name(request, category_name):
    try:
        category = Category.objects.get(name=category_name)
    except:
        raise Http404("Source matching query does not exist")
    articles = Article.objects.filter(category=category)
    paginator = Paginator(articles, 50)  # Paginate with 50 articles per page

    page_number = request.GET.get('page')
    try:
        page_articles = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        page_articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page
        page_articles = paginator.page(paginator.num_pages)

    data = [
        {
                'title': article.title,
                'description': article.description,
                'url': article.url,
                'url_to_image': article.url_to_image,
                'source': article.source.name if article.source else 'undefined',
                'source_url': article.source.url if article.source else 'undefined',
                'author': article.author,
                'published_at': article.published_at,
                'category': article.category.name if article.category else 'undefined'
        } 
        for article in page_articles
        ]
    return JsonResponse(data, safe=False)

# Cache the articles by source view for 5 minutes
@cache_page(60 * 5)
def articles_by_source(request, source_id):
    try:
        source = Source.objects.get(pk=source_id)
    except:
        raise Http404("Source matching query does not exist")
    
    articles = Article.objects.filter(source=source)
    paginator = Paginator(articles, 50)  # Paginate with 50 articles per page

    page_number = request.GET.get('page')
    try:
        page_articles = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        page_articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page
        page_articles = paginator.page(paginator.num_pages)

    data = [
        {
                'title': article.title,
                'description': article.description,
                'url': article.url,
                'url_to_image': article.url_to_image,
                'source': article.source.name if article.source else 'undefined',
                'source_url': article.source.url if article.source else 'undefined',
                'author': article.author,
                'published_at': article.published_at,
                'category': article.category.name if article.category else 'undefined'
        } 
        for article in page_articles
        ]
    return JsonResponse(data, safe=False)

@cache_page(60 * 5)
def articles_by_source_name(request, source_name):
    try:
        source = Source.objects.get(name=source_name)
    except Source.DoesNotExist:
        raise Http404("Source matching query does not exist")
    
    articles = Article.objects.filter(source=source)
    paginator = Paginator(articles, 50)  # Paginate with 50 articles per page

    page_number = request.GET.get('page')
    try:
        page_articles = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        page_articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page
        page_articles = paginator.page(paginator.num_pages)

    data = [
        {
                'title': article.title,
                'description': article.description,
                'url': article.url,
                'url_to_image': article.url_to_image,
                'source': article.source.name if article.source else 'undefined',
                'source_url': article.source.url if article.source else 'undefined',
                'author': article.author,
                'published_at': article.published_at,
                'category': article.category.name if article.category else 'undefined'
        } 
        for article in page_articles
        ]
    return JsonResponse(data, safe=False)

# Cache the articles by country view for 5 minutes
@cache_page(60 * 5)
def articles_by_country(request, country_code):
    articles = Article.objects.filter(source__country=country_code)
    paginator = Paginator(articles, 50)  # Paginate with 50 articles per page
    page_number = request.GET.get('page')
    try:
        page_articles = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        page_articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page
        page_articles = paginator.page(paginator.num_pages)

    data = [
        {
                'title': article.title,
                'description': article.description,
                'url': article.url,
                'url_to_image': article.url_to_image,
                'source': article.source.name if article.source else 'undefined',
                'source_url': article.source.url if article.source else 'undefined',
                'author': article.author,
                'published_at': article.published_at,
                'category': article.category.name if article.category else 'undefined'
        } 
        for article in page_articles
        ]
    return JsonResponse(data, safe=False)

# Cache the search articles view for 5 minutes
@cache_page(60 * 5)
def search_articles(request):
    query = request.GET.get('query')
    articles = Article.objects.filter(title__icontains=query) | Article.objects.filter(description__icontains=query)
    paginator = Paginator(articles, 50)  # Paginate with 50 articles per page

    page_number = request.GET.get('page')
    try:
        page_articles = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        page_articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page
        page_articles = paginator.page(paginator.num_pages)

    data = [
        {
                'title': article.title,
                'description': article.description,
                'url': article.url,
                'url_to_image': article.url_to_image,
                'source': article.source.name if article.source else 'undefined',
                'source_url': article.source.url if article.source else 'undefined',
                'author': article.author,
                'published_at': article.published_at,
                'category': article.category.name if article.category else 'undefined'
        } 
        for article in page_articles
        ]
    return JsonResponse(data, safe=False)

