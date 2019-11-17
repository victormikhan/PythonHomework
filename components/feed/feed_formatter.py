import json


class FeedFormatter:

    is_json = False

    @classmethod
    def generate_output(cls, feeds, limit, title):
        if not cls.is_json:
            return cls._default_output(feeds, limit, title)

        return cls._json_output(feeds, limit, title)

    @classmethod
    def _default_output(cls, feeds, limit, title):
        formatted_feeds = ''.join(cls._single_feed_format_default(feed) for feed in feeds[:limit])

        return 'Feed: {0}\n\n{1}'.format(title, formatted_feeds)

    @classmethod
    def _json_output(cls, feeds, limit, title):
        formatted_feeds = ',\n'.join(cls._single_feed_format_json(feed) for feed in feeds[:limit])

        #tmp
        output =  json.dumps({
            "title" : title,
            "items" : formatted_feeds
        }, indent=4, sort_keys=True)

        return formatted_feeds

    @classmethod
    def _single_feed_format_default(self,feed):
        return f'\
            \rTitle: {feed.title}\n\
            \rDate: {feed.date}\n\
            \rLink: {feed.link}\n\n\
            \r{feed.description}\n\n\
            \rLinks:\n\r{feed.links}\n\n'

    @classmethod
    def _single_feed_format_json(cls, feed):
        return json.dumps({
            "item": {
                "link": feed.link,
                "body": {
                     "title": feed.title,
                     "date": feed.date,
                     "links": feed.links,
                     "description": feed.description
                }
            }
        }, indent=4)