import requests
from django.core.management.base import BaseCommand
# from django.conf import settings
from celery import shared_task, Celery
from NewsProxy.news_proxy_app.models import Category, Article, Source

app = Celery('news_proxy_app')

@shared_task
class Command(BaseCommand):
    help = 'Fetch news for a specific country and create/update articles'

    def handle(self, *args, **kwargs):
        # Fetch news sources for a specific country
        languages = ['ar','sq', 'fr', 'en', 'en-US', 'it', 'gb', 'de', 'it']
        country_codes = ['us', 'fr', 'gb', 'de', 'it'] 

        # Fetch news for each country
        for language in languages:
            for country_code in country_codes:
                self.fetch_sources(language, country_code)
                self.fetch_news_for_country(country_code, language)
        
    def fetch_sources(self, language, country_code):
        api_key = "119a8762bd6a4278aea317a5a307baf1"
        sources_url = 'https://newsapi.org/v2/sources'
        sources_params = {'country':country_code,'language': language, 'apiKey': api_key}
        sources_response = requests.get(sources_url, params=sources_params)
        print("response : ", sources_response.status_code)
        if sources_response.status_code == 200:
            sources_data = sources_response.json().get('sources', [])
            
            # Create categories and sources
            for source_data in sources_data:
                category_name = source_data.get('category')
                category, created = Category.objects.get_or_create(name=category_name)
                
                source_name = source_data.get('name')
                source_country = source_data.get('country')
                source_url = source_data.get('url')
                source_language = source_data.get('language')
                source_description = source_data.get('description')

                source, _ = Source.objects.get_or_create(name=source_name, country=source_country, category__name=category_name, url=source_url, language=source_language, description=source_description)

                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created article: {source.name}'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Updated article: {source.name}'))
        
        else:
            self.stderr.write(self.style.ERROR(f'Failed to fetch news sources: {sources_response.status_code}'))

        
        
    def fetch_news_for_country(self, country_code, language):
    # Fetch news articles for a specific country
        articles_url = 'https://newsapi.org/v2/top-headlines'
        api_key = "119a8762bd6a4278aea317a5a307baf1"
        articles_params = {'apiKey': api_key, 'country': country_code, 'language': language}  # Replace 'YOUR_API_KEY_HERE' with your actual API key
        articles_response = requests.get(articles_url, params=articles_params)
        
        if articles_response.status_code == 200:
            articles_data = articles_response.json().get('articles', [])
            
            # Create or update articles
            for article_data in articles_data:
                source_name = article_data.get('source', {}).get('name')
                source_country = article_data.get('source', {}).get('country')
                try:
                    source = Source.objects.get(name=source_name, country=source_country)
                    category = source.category
                except Source.DoesNotExist:
                    source = None
                    category = None

                article, created = Article.objects.update_or_create(
                    title=article_data.get('title'),
                    defaults={
                        'source': source,
                        'author': article_data.get('author', 'null'),
                        'description': article_data.get('description'),
                        'url': article_data.get('url'),
                        'url_to_image': article_data.get('urlToImage'),
                        'published_at': article_data.get('publishedAt'),
                        'category': category
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created article: {article.title}'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Updated article: {article.title}'))
        else:
            self.stderr.write(self.style.ERROR(f'Failed to fetch news articles: {articles_response.status_code}'))
