from poynt import API


class Catalog():

    @classmethod
    def get_catalogs(cls, business_id, start_at=None, start_offset=None,
                     end_at=None, limit=None):
        """
        Get all catalogs at a business.

        Arguments:
        business_id (str): the business ID

        Keyword arguments:
        start_at (int, optional): get catalogs created after this time in seconds
        start_offset (int, optional): the numeric offset to start the list (for pagination)
        end_at (int, optional): get catalogs created before this time in seconds
        limit (int, optional): how many catalogs to return (for pagination)
        """

        params = {}
        if start_at is not None:
            params['startAt'] = start_at
        if start_offset is not None:
            params['startOffset'] = start_offset
        if end_at is not None:
            params['endAt'] = end_at
        if limit is not None:
            params['limit'] = limit

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/catalogs' % business_id,
            method='GET',
            params=params,
        )

    @classmethod
    def get_catalog(cls, business_id, catalog_id):
        """
        Get a single catalog for a business.

        Arguments:
        business_id (str): the business ID
        catalog_id (str): the catalog ID
        """

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/catalogs/%s' % (business_id, catalog_id),
            method='GET'
        )

    @classmethod
    def get_full_catalog(cls, business_id, catalog_id):
        """
        Get a catalog by id with all product details info embedded in
        the Catalog.

        Arguments:
        business_id (str): the business ID
        catalog_id (str): the catalog ID
        """

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/catalogs/%s/full' % (business_id, catalog_id),
            method='GET'
        )

    @classmethod
    def get_category(cls, business_id, catalog_id, category_id):
        """
        Get a single category in a catalog for a business.

        Arguments:
        business_id (str): the business ID
        catalog_id (str): the catalog ID
        category_id (str): the category ID
        """

        api = API.shared_instance()
        return api.request(
            url='/businesses/%s/catalogs/%s/categories/%s' % (
                business_id, catalog_id, category_id),
            method='GET'
        )
