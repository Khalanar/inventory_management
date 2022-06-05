# Inventory Manager

App created for the Backend Developer Intern - Fall 2022 (Remote - UK, Ireland, or Germany) position

---

## App

### How to Run
1. Open replit repo [inventory_management](https://replit.com/@PabloSanSeg/inventorymanagement?v=1)
2. Click *Open website* or preview directly from [inventorymanagement.pablosanseg.repl.co](https://inventorymanagement.pablosanseg.repl.co)

### How to use
Users can:
|  Functionality 	|  Action	|  Screenshots 	|
|---	|---	|---	|
|  View products in inventory 	|  Directly in homepage 	|  [homepage](https://screenshot.click/05-39-86333-76882.png) 	|
|  Create products 	|  *Add button* in homepage 	|  [add button](https://screenshot.click/05-40-69397-20518.png) - [new product form](https://screenshot.click/05-41-23771-39344.png)
|Edit products |Through *edit* button next to a product | [edit button](https://screenshot.click/05-43-44052-26502.png) - [edit product form](https://screenshot.click/05-44-36297-7004.png)|
|  Delete products	|  Products can be *deleted** after leaving a comment 	|   [delete button](https://screenshot.click/05-46-91843-31258.png) - [deletion form](https://screenshot.click/05-47-41206-59774.png)	|
| Recover products | *Deleted** products can be recovered directly from the home page | [recover button](https://screenshot.click/05-48-41526-38351.png) |

*deleting products - Deleted products aren't totally removed fromt the database. They are changed into a *deleted* status which allows users to see any deletion comments and revert the deletion, which automatically publishes products again.

--- 

## Technology

- [Python](https://www.python.org/) with the [Django](https://www.djangoproject.com/) framework for quick app prototyping.
- [Bootstrap](https://getbootstrap.com/) to quickly make the app presentable without having to do much frontend.
- [CrispyForms](https://django-crispy-forms.readthedocs.io/en/latest/) to quickly style and create web forms.

--- 

## Notes

- Allowed for negative inventory numbers purpusefully, as I want to clone this project and play around with the idea of pulling a list of *oversold* items that the merchant can use to prioritise purchasing or creating.
- Please do not preview directly in replit's renderer as it refuses to connect and does not load bootstrap on the best case scenario. If you have any questions reach out to me at Shopify's Slack at @poblolo