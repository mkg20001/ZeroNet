try:
    from Site import Site
    from SiteStorage import SiteStorage
except Exception as err:
    from Site.Site import Site
    from Site.SiteStorage import SiteStorage
