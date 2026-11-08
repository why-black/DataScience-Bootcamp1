import pytest
import os
import sys
import urllib
import requests
from bs4 import BeautifulSoup
import json
import collections
import functools
import datetime
import re


@pytest.mark.ratings
class TestRatings:
    """TESTS FOR <Ratings> CLASS"""
    CURRENT_DIR = os.path.dirname(__file__)
    RATINGS_PATH = os.path.join(CURRENT_DIR, "..", "datasets", "ratings.csv")

    @pytest.fixture
    def ratings_object(self):
        ratings = Ratings(self.RATINGS_PATH) # добавил 
        movies_path = os.path.join(os.path.dirname(__file__), "..", "datasets", "movies.csv")
        ratings.movies = Movies(movies_path)
        return ratings

    @pytest.fixture
    def movies_object(self, ratings_object):
        return ratings_object.Movies(ratings_object)

    @pytest.fixture
    def users_object(self, ratings_object):
        return ratings_object.Users(ratings_object)

    """TESTS FOR <Movies> SUBCLASS"""
    """TESTS FOR <dist_by_year> METHOD"""

    def test_dist_by_year_correct_return(self, movies_object):
        result = movies_object.dist_by_year()
        assert isinstance(result, dict)

    def test_dist_by_year_correct_elements(self, movies_object):
        result = movies_object.dist_by_year()
        assert all(isinstance(key, int) for key in result.keys())
        assert all(isinstance(value, int) for value in result.values())

    def test_dist_by_year_correct_sort(self, movies_object):
        result = movies_object.dist_by_year()
        keys = list(result.keys())
        assert keys == sorted(keys)

    """TESTS FOR <dist_by_rating> METHOD"""

    def test_dist_by_rating_correct_return(self, movies_object):
        result = movies_object.dist_by_rating()
        assert isinstance(result, dict)

    def test_dist_by_rating_correct_elements(self, movies_object):
        result = movies_object.dist_by_rating()
        assert all(isinstance(key, float) for key in result.keys())
        assert all(isinstance(value, int) for value in result.values())

    def test_dist_by_rating_correct_sort(self, movies_object):
        result = movies_object.dist_by_rating()
        keys = list(result.keys())
        assert keys == sorted(keys)

    """TESTS FOR <top_by_num_of_ratings> METHOD"""

    def test_top_by_num_of_ratings_correct_return(self, movies_object):
        result = movies_object.top_by_num_of_ratings(n=5)
        assert isinstance(result, dict)

    def test_top_by_num_of_ratings_correct_elements(self, movies_object):
        result = movies_object.top_by_num_of_ratings(n=5)
        assert len(result) == 5
        assert all(isinstance(key, str) for key in result.keys())
        assert all(isinstance(value, int) for value in result.values())

    def test_top_by_num_of_ratings_correct_sort(self, movies_object):
        result = movies_object.top_by_num_of_ratings(n=5)
        values = list(result.values())
        assert values == sorted(values, reverse=True)

    """TESTS FOR <top_by_ratings> METHOD"""

    def test_top_by_ratings_correct_return(self, movies_object):
        result = movies_object.top_by_ratings(
            n=5, metric=movies_object.average)
        assert isinstance(result, dict)

    def test_top_by_ratings_correct_elements(self, movies_object):
        result = movies_object.top_by_ratings(
            n=5, metric=movies_object.average)
        assert len(result) == 5
        assert all(isinstance(key, str) for key in result.keys())
        for value in result.values():
            assert isinstance(value, float)
            assert value == round(value, 2)

    def test_top_by_ratings_correct_sort(self, movies_object):
        result = movies_object.top_by_ratings(
            n=5, metric=movies_object.average)
        values = list(result.values())
        assert values == sorted(values, reverse=True)

    """TESTS FOR <top_controversial> METHOD"""

    def test_top_controversial_correct_return(self, movies_object):
        result = movies_object.top_controversial(n=5)
        assert isinstance(result, dict)

    def test_top_controversial_correct_elements(self, movies_object):
        result = movies_object.top_controversial(n=5)
        assert len(result) == 5
        assert all(isinstance(key, str) for key in result.keys())
        for value in result.values():
            assert isinstance(value, float)
            assert value == round(value, 2)

    def test_top_controversial_correct_sort(self, movies_object):
        result = movies_object.top_controversial(n=5)
        values = list(result.values())
        assert values == sorted(values, reverse=True)

    """TESTS FOR <Users> SUBCLASS"""
    """TESTS FOR <dist_by_num_of_ratings> METHOD"""

    def test_dist_by_num_of_ratings_correct_return(self, users_object):
        result = users_object.dist_by_num_of_ratings()
        assert isinstance(result, dict)

    def test_dist_by_num_of_ratings_correct_elements(self, users_object):
        result = users_object.dist_by_num_of_ratings()
        assert all(isinstance(key, int) for key in result.keys())
        assert all(isinstance(value, int) for value in result.values())

    def test_dist_by_num_of_ratings_correct_sort(self, users_object):
        result = users_object.dist_by_num_of_ratings()
        keys = list(result.keys())
        assert keys == sorted(keys)

    """TESTS FOR <dist_by_average_or_median> METHOD"""

    def test_dist_by_average_or_median_correct_return(self, users_object):
        result = users_object.dist_by_average_or_median(
            metric=users_object.average)
        assert isinstance(result, dict)

    def test_dist_by_average_or_median_correct_elements(self, users_object):
        result = users_object.dist_by_average_or_median(
            metric=users_object.average)
        assert all(isinstance(key, int) for key in result.keys())
        for value in result.values():
            assert isinstance(value, float)

    def test_dist_by_average_or_median_correct_sort(self, users_object):
        result = users_object.dist_by_average_or_median(
            metric=users_object.average)
        keys = list(result.keys())
        assert keys == sorted(keys)

    """TESTS FOR <top_by_variance> METHOD"""

    def test_top_by_variance_correct_return(self, users_object):
        result = users_object.top_by_variance(n=5)
        assert isinstance(result, dict)

    def test_top_by_variance_correct_elements(self, users_object):
        result = users_object.top_by_variance(n=5)
        assert len(result) == 5
        assert all(isinstance(key, int) for key in result.keys())
        for value in result.values():
            assert isinstance(value, float)
            assert value == round(value, 2)

    def test_top_by_variance_correct_sort(self, users_object):
        result = users_object.top_by_variance(n=5)
        values = list(result.values())
        assert values == sorted(values, reverse=True)


@pytest.mark.tags
class TestTags:
    """TESTS FOR <Tags> CLASS"""
    CURRENT_DIR = os.path.dirname(__file__)
    TAGS_PATH = os.path.join(CURRENT_DIR, "..", "datasets", "tags.csv")

    @pytest.fixture
    def tags_object(self):
        return Tags(self.TAGS_PATH)

    """TESTS FOR <most_words> METHOD"""

    def test_most_words_correct_return(self, tags_object):
        result = tags_object.most_words(n=5)
        assert isinstance(result, dict)

    def test_most_words_correct_elements(self, tags_object):
        result = tags_object.most_words(n=5)
        assert len(result) == 5
        assert len(result.keys()) == len(set(result.keys()))
        assert all(isinstance(key, str) for key in result.keys())
        assert all(isinstance(value, int) for value in result.values())

    def test_most_words_correct_sort(self, tags_object):
        result = tags_object.most_words(n=5)
        values = list(result.values())
        assert values == sorted(values, reverse=True)

    """TESTS FOR <longest> METHOD"""

    def test_longest_correct_return(self, tags_object):
        result = tags_object.longest(n=5)
        assert isinstance(result, list)

    def test_longest_correct_elements(self, tags_object):
        result = tags_object.longest(n=5)
        assert len(result) == 5
        assert len(result) == len(set(result))
        assert all(isinstance(item, str) for item in result)

    def test_longest_correct_sort(self, tags_object):
        result = tags_object.longest(n=5)
        assert result == sorted(result, key=len, reverse=True)

    """TESTS FOR <most_words_and_longest> METHOD"""

    def test_most_words_and_longest_correct_return(self, tags_object):
        result = tags_object.most_words_and_longest(n=5)
        assert isinstance(result, list)

    def test_most_words_and_longest_correct_elements(self, tags_object):
        result = tags_object.most_words_and_longest(n=5)
        assert len(result) == len(set(result))
        assert all(isinstance(item, str) for item in result)

    def test_most_words_and_longest_correct_sort(self, tags_object):
        pass

    """TESTS FOR <most_popular> METHOD"""

    def test_most_popular_correct_return(self, tags_object):
        result = tags_object.most_popular(n=5)
        assert isinstance(result, dict)

    def test_most_popular_correct_elements(self, tags_object):
        result = tags_object.most_popular(n=5)
        assert len(result) == 5
        assert len(result.keys()) == len(set(result.keys()))
        assert all(isinstance(key, str) for key in result.keys())
        assert all(isinstance(value, int) for value in result.values())

    def test_most_popular_correct_sort(self, tags_object):
        result = tags_object.most_popular(n=5)
        values = list(result.values())
        assert values == sorted(values, reverse=True)

    """TESTS FOR <tags_with> METHOD"""

    def test_tags_with_correct_return(self, tags_object):
        result = tags_object.tags_with(word='comedy')
        assert isinstance(result, list)

    def test_tags_with_correct_elements(self, tags_object):
        result = tags_object.tags_with(word='comedy')
        assert len(result) == len(set(result))
        assert all(isinstance(item, str) for item in result)

    def test_tags_with_correct_sort(self, tags_object):
        result = tags_object.tags_with(word='comedy')
        assert result == sorted(result)


@pytest.mark.movies
class TestMovies:
    """TESTS FOR <Movies> CLASS"""
    CURRENT_DIR = os.path.dirname(__file__)
    MOVIES_PATH = os.path.join(CURRENT_DIR, "..", "datasets", "movies.csv")

    @pytest.fixture
    def movies_object(self):
        return Movies(self.MOVIES_PATH)

    """TESTS FOR <dist_by_release> METHOD"""

    def test_dist_by_release_correct_return(self, movies_object):
        result = movies_object.dist_by_release()
        assert isinstance(result, (dict, collections.OrderedDict))

    def test_dist_by_release_correct_elements(self, movies_object):
        result = movies_object.dist_by_release()
        assert all(isinstance(key, str) for key in result.keys())
        assert all(int(key) for key in result.keys())
        assert all(isinstance(value, int) for value in result.values())

    def test_dist_by_release_correct_sort(self, movies_object):
        result = movies_object.dist_by_release()
        values = list(result.values())
        assert values == sorted(values, reverse=True)

    """TESTS FOR <dist_by_genres> METHOD"""

    def test_dist_by_genres_correct_return(self, movies_object):
        result = movies_object.dist_by_genres()
        assert isinstance(result, dict)

    def test_dist_by_genres_correct_elements(self, movies_object):
        result = movies_object.dist_by_genres()
        assert all(isinstance(key, str) for key in result.keys())
        assert all(isinstance(value, int) for value in result.values())

    def test_dist_by_genres_correct_sort(self, movies_object):
        result = movies_object.dist_by_genres()
        values = list(result.values())
        assert values == sorted(values, reverse=True)

    """TESTS FOR <most_genres> METHOD"""

    def test_most_genres_correct_return(self, movies_object):
        result = movies_object.most_genres(n=5)
        assert isinstance(result, dict)

    def test_most_genres_correct_elements(self, movies_object):
        result = movies_object.most_genres(n=5)
        assert len(result) == 5
        assert all(isinstance(key, str) for key in result.keys())
        assert all(isinstance(value, int) for value in result.values())

    def test_most_genres_correct_sort(self, movies_object):
        result = movies_object.most_genres(n=5)
        values = list(result.values())
        assert values == sorted(values, reverse=True)


@pytest.mark.links
class TestLinks:
    """TESTS FOR Links CLASS"""
    CURRENT_DIR = os.path.dirname(__file__)
    LINKS_PATH = os.path.join(CURRENT_DIR, "..", "datasets", "links.csv")

    @pytest.fixture
    def links_object(self):
        return Links(self.LINKS_PATH)

    @pytest.fixture
    def links_with_data(self, links_object):
        links_object.get_imdb(
            ['Director', 'Budget', 'Gross worldwide', 'Runtime', 'Lable'])
        return links_object

    """TESTS FOR get_imdb METHOD"""

    def test_get_imdb_correct_return(self, links_object):
        result = links_object.get_imdb(['Director', 'Budget', 'Runtime'])
        assert isinstance(result, list)

    def test_get_imdb_correct_elements(self, links_object):
        result = links_object.get_imdb(['Director', 'Budget', 'Runtime'])
        assert all(isinstance(item, list) for item in result)
        for item in result:
            assert isinstance(item[0], (int, str))
            for field in item[1:]:
                assert field is None or isinstance(
                    field, (str, int, float, list))

    def test_get_imdb_correct_sort(self, links_object):
        result = links_object.get_imdb(['Director', 'Budget', 'Runtime'])
        movie_ids = [item[0] for item in result]
        movie_ids_int = [int(mid) if isinstance(mid, str)
                         else mid for mid in movie_ids]
        assert movie_ids_int == sorted(movie_ids_int)

    """TESTS FOR top_directors METHOD"""

    def test_top_directors_correct_return(self, links_with_data):
        result = links_with_data.top_directors(n=3)
        assert isinstance(result, dict)

    def test_top_directors_correct_elements(self, links_with_data):
        result = links_with_data.top_directors(n=3)
        assert len(result) <= 3
        assert all(isinstance(key, (str, list)) for key in result.keys())
        assert all(isinstance(value, int) for value in result.values())

    def test_top_directors_correct_sort(self, links_with_data):
        result = links_with_data.top_directors(n=3)
        values = list(result.values())
        assert values == sorted(values, reverse=True)

    """TESTS FOR most_expensive METHOD"""

    def test_most_expensive_correct_return(self, links_with_data):
        result = links_with_data.most_expensive(n=3)
        assert isinstance(result, dict)

    def test_most_expensive_correct_elements(self, links_with_data):
        result = links_with_data.most_expensive(n=3)
        assert len(result) <= 3
        assert all(isinstance(key, str) for key in result.keys())
        assert all(isinstance(value, int) for value in result.values())

    def test_most_expensive_correct_sort(self, links_with_data):
        result = links_with_data.most_expensive(n=3)
        values = list(result.values())
        assert values == sorted(values, reverse=True)

    """TESTS FOR most_profitable METHOD"""

    def test_most_profitable_correct_return(self, links_with_data):
        result = links_with_data.most_profitable(n=3)
        assert isinstance(result, dict)

    def test_most_profitable_correct_elements(self, links_with_data):
        result = links_with_data.most_profitable(n=3)
        assert len(result) <= 3
        assert all(isinstance(key, str) for key in result.keys())
        assert all(isinstance(value, int) for value in result.values())

    def test_most_profitable_correct_sort(self, links_with_data):
        result = links_with_data.most_profitable(n=3)
        values = list(result.values())
        assert values == sorted(values, reverse=True)

    """TESTS FOR longest METHOD"""

    def test_longest_correct_return(self, links_with_data):
        result = links_with_data.longest(n=3)
        assert isinstance(result, dict)

    def test_longest_correct_elements(self, links_with_data):
        result = links_with_data.longest(n=3)
        assert len(result) <= 3
        assert all(isinstance(key, str) for key in result.keys())
        assert all(isinstance(value, int) for value in result.values())

    def test_longest_correct_sort(self, links_with_data):
        result = links_with_data.longest(n=3)
        values = list(result.values())
        assert values == sorted(values, reverse=True)

    """TESTS FOR top_cost_per_minute METHOD"""

    def test_top_cost_per_minute_correct_return(self, links_with_data):
        result = links_with_data.top_cost_per_minute(n=3)
        assert isinstance(result, dict)

    def test_top_cost_per_minute_correct_elements(self, links_with_data):
        result = links_with_data.top_cost_per_minute(n=3)
        assert len(result) <= 3
        assert all(isinstance(key, str) for key in result.keys())
        for value in result.values():
            assert isinstance(value, float)
            assert value == round(value, 2)

    def test_top_cost_per_minute_correct_sort(self, links_with_data):
        result = links_with_data.top_cost_per_minute(n=3)
        values = list(result.values())
        assert values == sorted(values, reverse=True)


class Links:
    """
    Analyzing data from links.csv
    """

    def __init__(self, path_to_the_file):
        """
        Put here any fields that you think you will need.
        """
        self.__path = path_to_the_file
        self.lines = []
        self.imdb_info = []
        self.__LINES_LIMIT = 10
        self.__DEFAULT_FIELDS = ['movieId', 'Lable', 'Director', 'Writers', 'Stars', 'Nominated for 3 Oscars', 'Release date', 'Country of origin', 'Official sites', 'Language', 'Also known as',
                                 'Filming locations', 'Production companies', 'Budget', 'Gross US & Canada', 'Opening weekend US & Canada', 'Gross worldwide', 'Runtime', 'Sound mix']
        self.imdb_fields = []
        self.lines = self._load_links()

    def _load_links(self):
        '''
        Loads data from csv file
        '''
        COLUMNS = 3
        data = []
        with open(self.__path, 'r') as f:
            for i, line in enumerate(f):
                if i == 0:
                    if not line.startswith("movieId,imdbId,tmdbId"):
                        raise ValueError(
                            f"Line {i}: Invalid header. Expected 'movieId,imdbId,tmdbId', "
                            f"got: {line[:60]}..."
                        )
                    continue
                if i >= self.__LINES_LIMIT + 1:
                    break
                splitted = line.strip().split(',')
                if not len(splitted) == COLUMNS:
                    raise ValueError('Incorrect file format.')
                data.append(splitted)
        return data

    def get_imdb(self, list_of_fields=None):
        """
        The method returns a list of lists [movieId, field1, field2, field3, ...] for the list of movies given as the argument (movieId).
        For example, [movieId, Director, Budget, Cumulative Worldwide Gross, Runtime].
        The values should be parsed from the IMDB webpages of the movies.
        Sort it by movieId descendingly.
        """

        if list_of_fields == None:
            list_of_fields = self.__DEFAULT_FIELDS

        if 'movieId' not in list_of_fields:
            list_of_fields = ['movieId'] + list_of_fields

        self.imdb_fields = list_of_fields

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive'
        }
        url = 'https://www.imdb.com/title/tt{0}'

        MOVIE_ID_COL = 0
        IMDB_ID_COL = 1
        TMDB_ID_COL = 2

        pages_missed = 0

        for movie in self.lines:
            final_url = url.format(
                movie[IMDB_ID_COL])
            page = requests.get(final_url, headers=headers)
            if not page.ok:
                pages_missed += 1
                print(final_url)
                print(page.status_code)
                continue
            d = Links._get_all_metrics(page.text)
            d['movieId'] = movie[MOVIE_ID_COL]

            self.imdb_info.append(
                [d[field] if field in d else None for field in list_of_fields])

        print(f'Pages missed: {pages_missed}')

        self.imdb_info.sort(key=lambda x: int(x[0]))

        self.parse_numeric_fields()

        return self.imdb_info

    def parse_numeric_fields(self, field_names=None):
        """
        Converts string numeric fields (Budget, Gross worldwide, Runtime, etc.)
        from strings like "$250,000,000 (estimated)" → int 250000000
        or "2h 30min" → 150 (minutes)

        If field_names is None — tries to auto-detect and parse all known numeric fields.
        Modifies self.imdb_info in place.

        Supported fields (auto-detected):
            - Budget
            - Gross US & Canada
            - Opening weekend US & Canada
            - Gross worldwide
            - Runtime (converts to minutes)
        """
        if not self.imdb_info or not self.imdb_fields:
            raise ValueError("No IMDb data to parse. Run get_imdb() first.")

        # автоматически определяем числовые поля
        if field_names is None:
            numeric_keywords = [
                'Budget', 'Gross', 'Opening weekend', 'Runtime'
            ]
            field_names = [
                field for field in self.imdb_fields
                if any(kw in field for kw in numeric_keywords)
            ]

        field_indices = {}
        for field in field_names:
            try:
                field_indices[field] = self.imdb_fields.index(field)
            except ValueError:
                print(
                    f"Warning: Field '{field}' not found in imdb_fields. Skipping.")
                continue

        if not field_indices:
            return

        # Вспомогательные функции
        def extract_number(s):
            """
            '$200,000,000 (estimated)' → 200000000
            """
            if not s or not isinstance(s, str):
                return 0
            numbers = re.findall(r'\d+', s.replace(',', ''))
            return int(''.join(numbers)) if numbers else 0

        def runtime_to_minutes(s):
            """
            '2h 30min' → 150, '142 min' → 142
            """
            if not s or not isinstance(s, str):
                return 0
            total = 0
            if 'h' in s:
                hours = re.search(r'(\d+)h', s)
                if hours:
                    total += int(hours.group(1)) * 60
            if 'm' in s:
                minutes = re.search(r'(\d+)m', s)
                if minutes:
                    total += int(minutes.group(1))
            # если просто "142 min"
            if total == 0:
                nums = re.findall(r'\d+', s)
                total = int(nums[0]) if nums else 0
            return total

        for row in self.imdb_info:
            for field_name, idx in field_indices.items():
                if idx >= len(row):
                    continue
                value = row[idx]

                if value is None:
                    continue

                if 'Runtime' in field_name:
                    row[idx] = runtime_to_minutes(value)
                else:
                    # денежные поля
                    row[idx] = extract_number(value)

        print(f"Parsed numeric fields: {', '.join(field_indices.keys())}")

    @staticmethod
    def _get_all_metrics(page: str):
        soup = BeautifulSoup(page, "html.parser")

        d = dict()

        # find lable
        movie_lable = soup.find('span', class_='hero__primary-text').text

        d['Lable'] = movie_lable

        # other metrics
        rows = soup.find_all(
            'li', class_=["ipc-metadata-list__item", "ipc-metadata-list__item--align-end"])

        for row in rows:
            lable = row.find(class_='ipc-metadata-list-item__label')
            if not lable:
                continue
            lable = lable.text
            # print(f'lable: {lable}')

            container = row.find('ul', class_=["ipc-inline-list", "ipc-inline-list--show-dividers",
                                               "ipc-inline-list--inline", "ipc-metadata-list-item__list-content", "base"])

            if not container:
                continue

            values = container.find_all(
                class_='ipc-metadata-list-item__list-content-item')

            if not values or len(values) <= 0:
                continue

            values = list(map(lambda x: x.text, values))

            if len(values) == 1:
                values = values[0]

            d[lable] = values

        return d

    def top_directors(self, n):
        """
        The method returns a dict with top-n directors where the keys are directors and
        the values are numbers of movies created by them. Sort it by numbers descendingly.
        """
        try:
            director_ind = self.imdb_fields.index('Director')
        except ValueError:
            raise ValueError(
                "The field 'Director' is not present. Can not execute this method.")
        counter = collections.Counter(
            movie[director_ind] for movie in self.imdb_info)
        return dict(counter.most_common(n))

    def most_expensive(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are their budgets. Sort it by budgets descendingly.
        """

        try:
            title_idx = self.imdb_fields.index(
                'Lable')
            budget_idx = self.imdb_fields.index('Budget')
        except ValueError as e:
            field = 'Lable' if 'Lable' in str(e) else 'Budget'
            raise ValueError(
                f"The field '{field}' is not present. Cannot execute this method.")

        movies_with_budget = []
        for row in self.imdb_info:
            title = row[title_idx]
            budget_cell = row[budget_idx]

            if budget_cell:
                movies_with_budget.append((title, budget_cell))

        if not movies_with_budget:
            raise ValueError("No movies with budget information found.")

        movies_with_budget.sort(
            key=lambda x: x[1],
            reverse=True
        )

        top_n = movies_with_budget[:n]
        return dict(top_n)

    def most_profitable(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are the difference between cumulative worldwide gross and budget.
        Sort it by the difference descendingly.
        """
        try:
            title_idx = self.imdb_fields.index('Lable')
            budget_idx = self.imdb_fields.index('Budget')
            worldwide_gross_idx = self.imdb_fields.index('Gross worldwide')
        except ValueError as e:
            field = 'Lable' if 'Lable' in str(
                e) else 'Budget' if 'Budget' in str(e) else 'Gross worldwide'
            raise ValueError(
                f"The field '{field}' is not present. Cannot execute this method.")

        movies_with_budget = []
        for row in self.imdb_info:
            title = row[title_idx]
            budget_cell = row[budget_idx]
            gross_cell = row[worldwide_gross_idx]

            if budget_cell and gross_cell:
                movies_with_budget.append((title, gross_cell - budget_cell))

        if not movies_with_budget:
            raise ValueError(
                "No movies with budget and gross information found.")

        movies_with_budget.sort(
            key=lambda x: x[1],
            reverse=True
        )

        top_n = movies_with_budget[:n]
        profits = dict(top_n)

        return profits

    def longest(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are their runtime. If there are more than one version – choose any.
        Sort it by runtime descendingly.
        """
        try:
            title_idx = self.imdb_fields.index('Lable')
            runtime_idx = self.imdb_fields.index('Runtime')
        except ValueError as e:
            field = 'Lable' if 'Lable' in str(e) else 'Runtime'
            raise ValueError(
                f"The field '{field}' is not present. Cannot execute this method.")

        movies_with_runtime = []

        for row in self.imdb_info:
            title = row[title_idx] if title_idx < len(row) else "Unknown"
            runtime_cell = row[runtime_idx] if runtime_idx < len(row) else None

            if runtime_cell:
                if runtime_cell > 0:
                    movies_with_runtime.append((title, runtime_cell))

        if not movies_with_runtime:
            raise ValueError("No movies with runtime information found.")

        movies_with_runtime.sort(key=lambda x: x[1], reverse=True)

        top_n = movies_with_runtime[:n]
        runtimes = dict(top_n)

        return runtimes

    def top_cost_per_minute(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are the budgets divided by their runtime. The budgets can be in different currencies – do not pay attention to it.
        The values should be rounded to 2 decimals. Sort it by the division descendingly.
        """

        try:
            title_idx = self.imdb_fields.index('Lable')
            budget_idx = self.imdb_fields.index('Budget')
            runtime_idx = self.imdb_fields.index('Runtime')
        except ValueError as e:
            missing = 'Lable' if 'Lable' in str(
                e) else 'Budget' if 'Budget' in str(e) else 'Runtime'
            raise ValueError(
                f"The field '{missing}' is not present. Cannot execute this method.")

        movies_data = []

        for row in self.imdb_info:
            # if (title_idx >= len(row) or budget_idx >= len(row) or runtime_idx >= len(row)):
            #     continue

            title = row[title_idx]
            budget_cell = row[budget_idx]
            runtime_cell = row[runtime_idx]

            # Пропускаем, если нет бюджета или длительности
            if not budget_cell or not runtime_cell:
                continue

            if budget_cell <= 0 or runtime_cell <= 0:
                continue

            cost_per_minute = budget_cell / runtime_cell
            cost_per_minute = round(cost_per_minute, 2)

            movies_data.append((title, cost_per_minute))

        if not movies_data:
            raise ValueError(
                "No movies with both Budget and Runtime found to calculate cost per minute.")

        movies_data.sort(key=lambda x: x[1], reverse=True)

        costs = dict(movies_data[:n])

        return costs


class Movies:
    """
    Analyzing data from movies.csv
    """
    def __init__(self, path_to_the_file):
        """
        Put here any fields that you think you will need.
        """
        self.__LINES_LIMIT = 100
        self.__LINES_FIELDS = ['id', 'title', 'year', 'genres']
        self.__path = path_to_the_file
        self.lines = self._load_movies()

        self.id_to_title = {line[0]: line[1] for line in self.lines}
        
    def _load_movies(self):
        '''
        Loads data from csv file
        '''
        data = []
        csv_pattern = re.compile(r'^(\d+),(?:"(.+)"|([^,]+)),(.+)$')
        year_pattern = re.compile(r'^(.*)\s\((\d{4})\)$')

        with open(self.__path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                line = line.strip()

                if i == 0:
                    if not line.startswith("movieId,title,genres"):
                        raise ValueError(
                            f"Line {i}: Invalid header. Expected 'movieId,title,genres', "
                            f"got: {line[:60]}..."
                        )
                    continue

                if i >= self.__LINES_LIMIT + 1:
                    break

                if not line:
                    continue

                match = csv_pattern.match(line)
                if not match:
                    raise ValueError(
                        f"Line {i}: Format mismatch. Expected 'id,title,genres', got: {line}")

                movie_id = match.group(1)
                # заголовок попадает либо в группу 2 (если был в кавычках), либо в группу 3
                full_title = match.group(2) if match.group(
                    2) else match.group(3)
                genres_str = match.group(4)

                title_match = year_pattern.match(full_title)
                if not title_match:
                    raise ValueError(
                        f"Line {i}: Title format mismatch. Expected 'Title (YYYY)', "
                        f"got: '{full_title}'"
                    )

                title = title_match.group(1).strip()
                year = title_match.group(2)
                genres = genres_str.split('|')

                data.append([movie_id, title, year, genres])

        return data

    def dist_by_release(self):
        """
        The method returns a dict or an OrderedDict where the keys are years and the values are counts.
        You need to extract years from the titles. Sort it by counts descendingly.
        """
        year_idx = self.__LINES_FIELDS.index('year')
        counter = collections.Counter(line[year_idx] for line in self.lines)
        sorted_items = sorted(
            counter.items(), key=lambda x: x[1], reverse=True)

        return dict(sorted_items)

    def dist_by_genres(self):
        """
        The method returns a dict where the keys are genres and the values are counts.
        Sort it by counts descendingly.
        """
        genres_idx = self.__LINES_FIELDS.index('genres')
        counter = collections.Counter()
        for line in self.lines:
            genres = line[genres_idx]
            for genre in genres:
                if genre in counter:
                    counter[genre] += 1
                else:
                    counter[genre] = 1

        sorted_items = sorted(
            counter.items(), key=lambda x: x[1], reverse=True)
        return dict(sorted_items)

    def most_genres(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are the number of genres of the movie. Sort it by numbers descendingly.
        """
        title_idx = self.__LINES_FIELDS.index('title')
        genres_idx = self.__LINES_FIELDS.index('genres')

        title_genres = []

        for line in self.lines:
            title_genres.append((line[title_idx], len(line[genres_idx])))

        d = collections.Counter(dict(title_genres)).most_common(n)

        return dict(d)

class Ratings:
    """
    Analyzing data from ratings.csv
    """

    def __init__(self, path_to_the_file):
        self.data = []
        self.by_movies = {}
        self.by_users = {}

        with open(path_to_the_file, 'r', encoding='utf-8') as f:
            headers = f.readline().strip().split(',')
            for i, line in enumerate(f):
                if i >= 1000:
                    break
                values = line.strip().split(',')

                if len(values) != 4:
                    raise ValueError(f"invalid syntax at line {i+2}: {line}")
                
                try:
                    rating = {
                        headers[0]: int(values[0]),  # userId
                        headers[1]: int(values[1]),  # movieId
                        headers[2]: float(values[2]),  # rating
                        headers[3]: int(values[3])  # timestamp
                    }
                    self.data.append(rating)
                except ValueError:
                    raise ValueError(f"invalid syntax at line {i+2}: {line}")
                
                movie_id = rating["movieId"]
                user_id = rating["userId"]
                score = rating["rating"]

                self.by_movies.setdefault(movie_id, []).append(score)
                self.by_users.setdefault(user_id, []).append(score)

    class Movies:
        def __init__(self, ratings_type):
            self.ratings = ratings_type

        def dist_by_year(self):
            """
            The method returns a dict where the keys are years and the values are counts. 
            Sort it by years ascendingly. You need to extract years from timestamps.
            """
            from datetime import datetime
            year_count = {}
            for rating in self.ratings.data:
                year = datetime.fromtimestamp(rating['timestamp']).year
                year_count[year] = year_count.get(year, 0) + 1

            ratings_by_year = dict(sorted(year_count.items()))
            return ratings_by_year

        def dist_by_rating(self):
            """
            The method returns a dict where the keys are ratings and the values are counts.
            Sort it by ratings ascendingly.
            """
            ratings_count = {}
            for rating in self.ratings.data:
                value = rating['rating']
                ratings_count[value] = ratings_count.get(value, 0) + 1
            ratings_distribution = dict(sorted(ratings_count.items()))
            return ratings_distribution

        def top_by_num_of_ratings(self, n):
            """
            The method returns top-n movies by the number of ratings. 
            It is a dict where the keys are movie titles and the values are numbers.
            Sort it by numbers descendingly.
            """
            if not hasattr(self.ratings, 'movies') or self.ratings.movies is None:
                raise Exception(
                    "must have atribute 'movies' from calss Movies.\n"
                    "Template:\n"
                    "movies = Movies('path/to/movies.csv')\n"
                    "ratings = Ratings('path/to/ratings.csv')\n" 
                    "ratings.movies = movies"
                )
            counts = {}
            for movie_id, ratings in self.ratings.by_movies.items():
                title = self.ratings.movies.id_to_title.get(str(movie_id), f"UNKNOWN_{movie_id}")
                counts[title] = len(ratings)

            sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
            top_movies = dict(sorted_counts[:n])
            return top_movies

        @staticmethod
        def average(ratings):
            return sum(ratings)/len(ratings)

        @staticmethod
        def median(ratings):
            sorted_r = sorted(ratings)
            n = len(ratings)
            mid = n//2
            if n % 2 == 0:
                return (sorted_r[mid-1]+sorted_r[mid])/2
            else:
                return sorted_r[mid]

        def top_by_ratings(self, n, metric=average):
            """
            The method returns top-n movies by the average or median of the ratings.
            It is a dict where the keys are movie titles and the values are metric values.
            Sort it by metric descendingly.
            The values should be rounded to 2 decimals.
            """
            if not hasattr(self.ratings, 'movies') or self.ratings.movies is None:
                raise Exception(
                    "must have atribute 'movies' from calss Movies.\n"
                    "Template:\n"
                    "movies = Movies('path/to/movies.csv')\n"
                    "ratings = Ratings('path/to/ratings.csv')\n" 
                    "ratings.movies = movies"
                )
            avg_ratings = {}
            top_movies = {}
            for movie_id, values in self.ratings.by_movies.items():
                title = self.ratings.movies.id_to_title.get(str(movie_id), f"UNKNOWN_{movie_id}")
                avg_ratings[title] = round(metric(values), 2)

            avg_ratings = sorted(avg_ratings.items(), key=lambda x: x[1], reverse=True)
            top_movies = dict(avg_ratings[:n])
            return top_movies

        def top_controversial(self, n):
            """
            The method returns top-n movies by the variance of the ratings.
            It is a dict where the keys are movie titles and the values are the variances.
            Sort it by variance descendingly.
            The values should be rounded to 2 decimals.
            """
            if not hasattr(self.ratings, 'movies') or self.ratings.movies is None:
                raise Exception(
                    "must have atribute 'movies' from calss Movies.\n"
                    "Template:\n"
                    "movies = Movies('path/to/movies.csv')\n"
                    "ratings = Ratings('path/to/ratings.csv')\n" 
                    "ratings.movies = movies"
                )
            variances = {}
            for movie_id, rlist in self.ratings.by_movies.items():
                avg = sum(rlist) / len(rlist)
                var = sum((x - avg)**2 for x in rlist) / len(rlist)
                title = self.ratings.movies.id_to_title.get(str(movie_id), f"UNKNOWN_{movie_id}")
                variances[title] = round(var, 2)

            sorted_vars = sorted(variances.items(), key=lambda x: x[1], reverse=True)
            top_movies = dict(sorted_vars[:n])
            return top_movies

    class Users(Movies):
        """
        In this class, three methods should work. 
        The 1st returns the distribution of users by the number of ratings made by them.
        The 2nd returns the distribution of users by average or median ratings made by them.
        The 3rd returns top-n users with the biggest variance of their ratings.
        Inherit from the class Movies. Several methods are similar to the methods from it.
        """

        def __init__(self, ratings_type):
            super().__init__(ratings_type)
            self.by_user = ratings_type.by_users

        def dist_by_num_of_ratings(self):
            counts = {}
            for user_id, ratings in self.by_user.items():
                counts[user_id] = len(ratings)
            return dict(sorted(counts.items()))

        def dist_by_average_or_median(self, metric=None):
            if metric is None:
                metric = self.average
            result = {}
            for user_id, ratings in self.by_user.items():
                result[user_id] = metric(ratings)
            return dict(sorted(result.items()))

        def top_by_variance(self, n):
            variances = {}
            for user_id, ratings in self.by_user.items():
                avg = sum(ratings) / len(ratings)
                var = sum((x - avg)**2 for x in ratings) / len(ratings)
                variances[user_id] = round(var, 2)

            sorted_vars = sorted(
                variances.items(), key=lambda x: x[1], reverse=True)
            return dict(sorted_vars[:n])


class Tags:
    """
    Analyzing data from tags.csv
    """

    def __init__(self, path_to_the_file):
        """
        Put here any fields that you think you will need.
        """
        self.data = []
        self.tag_counts = {}

        with open(path_to_the_file, 'r', encoding='utf-8') as f:
            headers = f.readline().strip().split(',')
            for i, line in enumerate(f):
                values = line.strip().split(',')
                tags = {
                    headers[0]: int(values[0]),  # userId
                    headers[1]: int(values[1]),  # movieId
                    headers[2]: values[2].strip(),  # tag
                    headers[3]: int(values[3])    # timestamp
                }
                self.data.append(tags)

                tag = tags['tag']
                if tag not in self.tag_counts:
                    self.tag_counts[tag] = 0
                self.tag_counts[tag] += 1

    def most_words(self, n):
        """
        The method returns top-n tags with most words inside. It is a dict 
        where the keys are tags and the values are the number of words inside the tag.
        Drop the duplicates. Sort it by numbers descendingly.
        """
        tags_lens = {tag: len(tag.split()) for tag in self.tag_counts}
        tags_sorted = dict(
            sorted(tags_lens.items(), key=lambda x: x[1], reverse=True))
        big_tags = dict(list(tags_sorted.items())[:n])

        return big_tags

    def longest(self, n):
        """
        The method returns top-n longest tags in terms of the number of characters.
        It is a list of the tags. Drop the duplicates. Sort it by numbers descendingly.
        """
        tags_lens = {tag: len(tag) for tag in self.tag_counts}
        tags_sorted = dict(
            sorted(tags_lens.items(), key=lambda x: x[1], reverse=True))
        big_tags = list(tags_sorted.keys())[:n]

        return big_tags

    def most_words_and_longest(self, n):
        """
        The method returns the intersection between top-n tags with most words inside and 
        top-n longest tags in terms of the number of characters.
        Drop the duplicates. It is a list of the tags.
        """
        top_words = set(self.most_words(n).keys())
        top_longest = set(self.longest(n))
        big_tags = list(top_words & top_longest)
        return big_tags

    def most_popular(self, n):
        """
        The method returns the most popular tags. 
        It is a dict where the keys are tags and the values are the counts.
        Drop the duplicates. Sort it by counts descendingly.
        """
        tags_sorted = dict(sorted(self.tag_counts.items(),
                           key=lambda x: x[1], reverse=True))
        popular_tags = dict(list(tags_sorted.items())[:n])
        return popular_tags

    def tags_with(self, word):
        """
        The method returns all unique tags that include the word given as the argument.
        Drop the duplicates. It is a list of the tags. Sort it by tag names alphabetically.
        """
        tags_with_word = [
            tag for tag in self.tag_counts if word.lower() in tag.lower()]
        tags_with_word.sort()
        return tags_with_word
