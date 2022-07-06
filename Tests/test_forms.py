from django.test import TestCase
from accounts.forms import *


class Test_forms(TestCase):

    def test_patient_form(self):
        form=PatientForm(data={})
        self.assertFalse(form.is_valid())

    def test_bed_form(self):
        form=BedForm(data={})
        self.assertFalse(form.is_valid())

    def test_ven_form(self):
        form=VenForm(data={})
        self.assertFalse(form.is_valid())

    def test_concentration_form(self):
        form=ConcentrationForm(data={})
        self.assertFalse(form.is_valid())

    def test_equip_form(self):
        form=EquipForm(data={})
        self.assertFalse(form.is_valid())

    def test_req_form(self):
        form=ReqForm(data={})
        self.assertFalse(form.is_valid())

    def test_rep_form(self):
        form = RepForm(data={})
        self.assertFalse(form.is_valid())

    def test_create_user_form(self):
        form = CreateUserForm(data={})
        self.assertFalse(form.is_valid())

    def test_employee_form(self):
        form = EmployeeForm(data={})
        self.assertFalse(form.is_valid())