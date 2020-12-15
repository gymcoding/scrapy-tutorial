import scrapy

class MovieSpider(scrapy.Spider):
    name = "movie"

    def start_requests(self):
        urls = [
            'https://movie.naver.com/movie/running/current.nhn',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        try:
            item = {}
            movie_sels = response.css('ul.lst_detail_t1 > li')
            for movie_sel in movie_sels:
                # 영화제목
                item['title'] = movie_sel.css('.tit > a::text').get()
                # 나이제한
                item['age_limit'] = movie_sel.css('.tit > span::text').get()
                # 평점
                item['rating'] = movie_sel.css('.star_t1 > a > span.num::text').get()
                # 평점 참여자 수
                item['rating_count'] = movie_sel.css('.star_t1 > a > span.num2>em::text').get()
                # 장르
                if len(movie_sel.css('.info_txt1 > dd')) >= 1:
                    item['genre'] = ''
                    genre_sels = movie_sel.css('.info_txt1 > dd')[0].css('.link_txt>a')
                    for index, genre_sel in enumerate(genre_sels):
                        if index != 0:
                            item['genre'] += ', '
                        item['genre'] += genre_sel.css('::text').get()
                # 감독
                if len(movie_sel.css('.info_txt1 > dd')) >= 2:
                    item['director'] = ''
                    director_sels = movie_sel.css('.info_txt1 > dd')[1].css('.link_txt>a')
                    for index, director_sel in enumerate(director_sels):
                        if index != 0:
                            item['director'] += ', '
                        item['director'] += director_sel.css('::text').get()
                # 배우
                if len(movie_sel.css('.info_txt1 > dd')) >= 3:
                    item['actor'] = ''
                    actor_sels = movie_sel.css('.info_txt1 > dd')[2].css('.link_txt>a')
                    for index, actor_sel in enumerate(actor_sels):
                        if index != 0:
                            item['actor'] += ', '
                        item['actor'] += actor_sel.css('::text').get()

                yield item
        except Exception as e:
            print('e: ', e)