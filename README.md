# poynt-python

This SDK helps you connect to the Poynt API from your Python apps. You can easily get/create business information, subscribe to webhooks, and send cloud messages to your terminal app.

## Documentation

After you've [signed up for a Poynt developer account](https://poynt.net/auth/signup/developer), check out our [API reference](https://poynt.com/docs/api/) or our [developer guides](https://poynt.com/tag/guides/)!

## Installation

Install this package:

```
pip install poynt
```

## Usage

You can connect to the Poynt API by passing either a filename or a string containing your PEM-encoded private key you downloaded from Poynt.net.

```python
import poynt

poynt.application_id = 'urn:aid:your-application-id'
poynt.filename = '/path/to/your/key.pem'
```
or

```python
import poynt

poynt.application_id = 'urn:aid:your-application-id'
poynt.key = '-----BEGIN RSA PRIVATE KEY-----\n.....\n-----END RSA PRIVATE KEY-----'
```

Then, make a request signed with your app private key:

```python
business, status_code = poynt.Business.get_business('00000000-0000-0000-0000-000000000000')

if status_code is 200:
    # do something with business
else:
    # throw an error
```

We'll handle all the request signing, token refresh, etc. for you!

## Namespaces and methods

### [CloudMessages](https://poynt.com/docs/api/#cloudmessages-index)

* `poynt.CloudMessage.send_cloud_message`
* `poynt.CloudMessage.send_raw_cloud_message`

### [Hooks](https://poynt.com/docs/api/#hooks-index)

* `poynt.Hook.get_hooks`
* `poynt.Hook.create_hook`

### [Businesses](https://poynt.com/docs/api/#businesses-index)

* `poynt.Business.get_business`

### [Stores](https://poynt.com/docs/api/#stores-index)

* `poynt.Store.get_store`

### [Orders](https://poynt.com/docs/api/#orders-index)

* `poynt.Order.get_orders`
* `poynt.Order.get_order`

### [Transactions](https://poynt.com/docs/api/#transactions-index)

* `poynt.Transaction.get_transactions`
* `poynt.Transaction.get_transaction`

### [Customers](https://poynt.com/docs/api/#customers-index)

* `poynt.Customer.get_customers`
* `poynt.Customer.get_customer`

### [Catalogs](https://poynt.com/docs/api/#catalogs-index)

* `poynt.Catalog.get_catalogs`
* `poynt.Catalog.get_catalog`
* `poynt.Catalog.get_full_catalog`
* `poynt.Catalog.create_catalog`
* `poynt.Catalog.create_full_catalog`
* `poynt.Catalog.update_catalog`
* `poynt.Catalog.get_category`
* `poynt.Catalog.create_category`
* `poynt.Catalog.lookup_categories`
* `poynt.Catalog.delete_category`
* `poynt.Catalog.update_category`

### [Products](https://poynt.com/docs/api/#products-index)

* `poynt.Product.get_products`
* `poynt.Product.get_products_summary`
* `poynt.Product.lookup_products`
* `poynt.Product.get_product`
* `poynt.Product.create_product`
* `poynt.Product.delete_product`
* `poynt.Product.update_product`

### [Taxes](https://poynt.com/docs/api/#taxes-index)

* `poynt.Tax.get_taxes`
* `poynt.Tax.get_tax`
* `poynt.Tax.create_tax`
* `poynt.Tax.delete_tax`
* `poynt.Tax.update_tax`

### [Business Users](https://poynt.com/docs/api/#business-users-index)

* `poynt.BusinessUser.get_business_users`
* `poynt.BusinessUser.get_business_user`
