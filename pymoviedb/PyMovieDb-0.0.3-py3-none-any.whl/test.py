"""
example code to check API working
"""

from PyMovieDb import IMDB

imdb = IMDB()
# res = imdb.get_by_name('Devil In Ohio', year=2022, tv=True)
# res = imdb.get_by_id("tt12593682")
# res = imdb.search('liger', year=2022)
# res = imdb.get_by_name('liger', year=2022)
# res = imdb.get_by_name('Cinderella', year=2015)
res = imdb.get_by_name('She Hulk: Attorney At Law', year=2022, tv=True)
# res = imdb.get_by_name('Wild District', year=2018)
# res = imdb.person_by_name('Rajkummar Rao')
# res = imdb.person_by_id("nm3822770")
# res = imdb.popular_movies(genre="comedy", start_id=0)
# res = imdb.upcoming()

print(res)



# ..........for parser.py..........
res = """
{"@context":"https://schema.org","@type":"Movie","url":"/title/tt10954984/","name":"Nope","image":"https://m.media-amazon.com/images/M/MV5BNGM1MDc3ZjgtODlkOS00NmZjLWJlOTItNGQ5OGFhN2JlNjgxXkEyXkFqcGdeQXVyNjk1Njg5NTA@._V1_.jpg","description":"The residents of a lonely gulch in inland California bear witness to an uncanny and chilling discovery.","review":{"@type":"Review","itemReviewed":{"@type":"CreativeWork","url":"/title/tt10954984/"},"author":{"@type":"Person","name":"seansoulo73"},"dateCreated":"2022-07-25","inLanguage":"English","name":"Not Sure Where Jordan Was Going","reviewBody":"I hope we are not about to see the Shyamalan effect with Jordan Peele, where the debut film is amazing and everything that follows leaves you scratching your head. I feel like I&apos;m on that road with Peele&apos;s body of silver screen work. "Get Out" was a masterpiece, while "Us" jus didn&apos;t do it for me and now "Nope!"\n\nKeke Palmer did her thing in the role she played (she is the star of this movie for sure) and Daniel kept up with a good performance in his own right, but the film itself was something outta the Twilight Zone. More of a sci-fi thriller than a horror flick, it had too many holes and unanswered questions for my liking. Peele&apos;s approach to filmmaking is amazing, much like Shyamalan, but the stories, like Shyamalan&apos;s are starting to fall short of being good films.\n\nJordan may have dreamt this story and woke up at 5am and jotted down every detail he could remember. And like our weird dreams, they never make any sense and we forget a lot of the details by the time we wake up! Nope was like one of those weird a... dreams!","reviewRating":{"@type":"Rating","worstRating":1,"bestRating":10,"ratingValue":6}},"aggregateRating":{"@type":"AggregateRating","ratingCount":87673,"bestRating":10,"worstRating":1,"ratingValue":7},"contentRating":"A","genre":["Horror","Mystery","Sci-Fi"],"datePublished":"2022-08-19","keywords":"horse,unidentified flying object,alien,cloud,eaten alive","trailer":{"@type":"VideoObject","name":"Final Trailer","embedUrl":"https://www.imdb.com/video/imdb/vi1273872921","thumbnail":{"@type":"ImageObject","contentUrl":"https://m.media-amazon.com/images/M/MV5BMGQ5MmVkZTMtOWNhMy00YmM5LWIwNmQtMmViZjBlZGU3NWVhXkEyXkFqcGdeQXNuZXNodQ@@._V1_.jpg"},"thumbnailUrl":"https://m.media-amazon.com/images/M/MV5BMGQ5MmVkZTMtOWNhMy00YmM5LWIwNmQtMmViZjBlZGU3NWVhXkEyXkFqcGdeQXNuZXNodQ@@._V1_.jpg","url":"https://www.imdb.com/video/vi1273872921","description":"The residents of a lonely gulch in inland California bear witness to an uncanny and chilling discovery.","duration":"PT3M2S","uploadDate":"2022-06-09T15:07:56.355Z"},"actor":[{"@type":"Person","url":"/name/nm2257207/","name":"Daniel Kaluuya"},{"@type":"Person","url":"/name/nm1551130/","name":"Keke Palmer"},{"@type":"Person","url":"/name/nm5155952/","name":"Brandon Perea"}],"director":[{"@type":"Person","url":"/name/nm1443502/","name":"Jordan Peele"}],"creator":[{"@type":"Organization","url":"/company/co0005073/"},{"@type":"Organization","url":"/company/co0169264/"},{"@type":"Organization","url":"/company/co0369235/"},{"@type":"Person","url":"/name/nm1443502/","name":"Jordan Peele"}],"duration":"PT2H10M"}

"""


# ip = ImdbParser(res)
# res = ip.remove_trailer
# res = ip.remove_description
# print(res)
