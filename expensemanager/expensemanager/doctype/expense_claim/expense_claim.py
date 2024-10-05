# Copyright (c) 2024, priya and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ExpenseClaim(Document):
	def validate(self):
		total = 0
		for item in self.expense_list:
			total += item.amount

		self.total_expense_amount = total
		