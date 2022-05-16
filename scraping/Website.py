class Website():
    ATTRIBUTE_NAMES = [
        "url",
        "isBlog",
        "isWordpress",
        "isBlogSpot",
        "isUrlIncludeDate",
        "isUrlIncludeDomainPostTitle",
        "isUrlIncludeYearMonthPostTitle",
        "urlLen",
        "numOfKeywords",
        "isPrefixBlog",
        "isMetaTagIncludeBlogKeyword",
        "isUrlSuffixHTML",
        "domainLen",
        "pathNumberCount",
        "lenOfPath",
    ]
    def __init__(self, url="http://example.com", isBlog = 0):
        self.url = url
        self.isBlog = isBlog
        self.isWordpress = 0
        self.isBlogSpot = 0
        self.isUrlIncludeDate = 0
        self.isUrlIncludeDomainPostTitle = 0
        self.isUrlIncludeYearMonthPostTitle = 0
        self.urlLen = 0
        self.numOfKeywords = 0
        self.isPrefixBlog = 0
        self.isMetaTagIncludeBlogKeyword = 0
        self.isUrlSuffixHTML = 0
        self.numOfBlogKeywords = 0 
        self.domainLen = 0
        self.pathNumberCount = 0
        self.lenOfPath = 0
        
        

