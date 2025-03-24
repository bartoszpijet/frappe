import frappe
from frappe import _
from frappe.model.document import Document

class OutlookCalendar(Document):
	# begin: semi-auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		authorization_code: DF.Password | None
		calendar_name: DF.Data
		enable: DF.Check
		outlook_calendar_id: DF.Data | None
		next_sync_token: DF.Password | None
		pull_from_outlook_calendar: DF.Check
		sync_as_public: DF.Check
		push_to_outlook_calendar: DF.Check
		refresh_token: DF.Password | None
		user: DF.Link
	# end: semi-auto-generated types