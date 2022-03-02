BOT_NAME = 'online_arbitrage'

SPIDER_MODULES = ['online_arbitrage.spiders']
NEWSPIDER_MODULE = 'online_arbitrage.spiders'

ROBOTSTXT_OBEY = False

# Splash Setup
SPLASH_URL = 'http://127.0.0.1:8050'

DOWNLOADER_MIDDLEWARES = {
    #'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
    #'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 620,
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,



}

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

FAKEUSERAGENT_PROVIDERS = [
    'scrapy_fake_useragent.providers.FakeUserAgentProvider',  # this is the first provider we'll try
    'scrapy_fake_useragent.providers.FakerProvider',  # if FakeUserAgentProvider fails, we'll use faker to generate a user-agent string for us
    'scrapy_fake_useragent.providers.FixedUserAgentProvider',  # fall back to USER_AGENT value
]
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'


DOWNLOAD_DELAY = 3
COOKIES_ENABLED = False

#FEEDS = {"overwrite": True}

FEED_EXPORTERS = {
    'csv': 'online_arbitrage.exporters.CsvCustomSeperator'
}

#PROXY_POOL_ENABLED = True