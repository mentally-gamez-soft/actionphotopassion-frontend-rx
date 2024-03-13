
class ServiceCacheArticleReader:

    cache_article:list = [] 
    
    def exists_article_id_in_cache(self, article_id:int) -> dict:
        element = [article for article in self.cache_article if article.get_id_article() == article_id]
        return {"status":len(element) > 0, "article":element[:]}
    
    def exists_article_in_cache(self, article_reader:ArticleParser) -> bool:
        element = [article for article in self.cache_article if article.get_id_article() == article_reader.get_id_article()]
        return len(element) > 0

    def add_article_to_cache(self, article_reader:ArticleParser):
        if not self.exists_article_in_cache(article_reader):
            self.cache_article.append(article_reader)

    def get_article_from_cache(self, article_id:int):
        res = self.exists_article_id_in_cache(article_id)
        if res["status"]:
            return res["article"]
