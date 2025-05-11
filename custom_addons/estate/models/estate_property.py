import requests
from odoo import models, fields, api

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name = fields.Char("Title", required=True)
    description = fields.Text("Description")
    postcode = fields.Char("Postcode")
    date_availability = fields.Date("Available from", copy=False, default=fields.Date.today)
    expected_price = fields.Float("Expected Price", required=True)
    selling_price = fields.Float("Selling Price", readonly=True, copy=False, default=0.0)
    bedrooms = fields.Integer("Bedrooms", default=2)
    living_area = fields.Integer("Living Area (sqm)", default=50)
    facades = fields.Integer("Facades", default=3)
    garage = fields.Boolean("Garage", default=False)
    garden = fields.Boolean("Garden", default=False)
    garden_area = fields.Integer("Garden Area (sqm)", default=0)
    garden_orientation = fields.Selection(
        [('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        string="Garden Orientation",
        default='north'
    )
    state = fields.Selection(
        [("new", "New"), ("offer", "Offer"), ("received", "Received"), ("offer_accepted", "Offer Accepted"), ("sold", "Sold"), ("cancelled", "Cancelled")],
        string="State",
        required=True,
        copy=False,
        default="new"
    )
    active = fields.Boolean("Active", default=True)
    property_type_id = fields.Many2one("estate.property.type", string="Type")
    buyer_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    salesperson_id = fields.Many2one("res.users", string="Salesperson", default=lambda self: self.env.user)

    @api.model
    def import_properties_from_api(self, api_token):
        url = "http://localhost:3000/api/users/1094c217-874b-4578-b0e3-dc57071bf45f/results"
        headers = {"Authorization": f"Bearer {api_token}"}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            properties = response.json()

            for prop in properties:
                self.create({
                    "name": prop.get("name"),
                    "description": prop.get("description"),
                    "postcode": prop.get("postcode"),
                    "date_availability": prop.get("date_availability"),
                    "expected_price": prop.get("expected_price"),
                    "selling_price": prop.get("selling_price", 0.0),
                    "bedrooms": prop.get("bedrooms", 2),
                    "living_area": prop.get("living_area", 50),
                    "facades": prop.get("facades", 1),
                    "garage": prop.get("garage", False),
                    "garden": prop.get("garden", False),
                    "garden_area": prop.get("garden_area", 0),
                    "garden_orientation": prop.get("garden_orientation", "north"),
                    "state": "new",
                })

            return {
                'type': 'ir.actions.client',
                'tag': 'reload',
            }
        except requests.exceptions.RequestException as e:
            raise models.ValidationError(f"Failed to fetch properties: {e}")