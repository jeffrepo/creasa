# -*- coding: utf-8 -*-

from odoo import api, fields, models, tools, _

class CreasaMarca(models.Model):
    _name = "creasa.marca"

    name = fields.Char('Name')
