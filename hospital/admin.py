from flask_admin.babel import lazy_gettext
from flask_admin.contrib.sqla import ModelView, filters
from flask_admin import BaseView, expose
from flask_admin.contrib.sqla.filters import BaseSQLAFilter
from flask_admin.contrib.sqla.filters import *
from flask_admin.model.filters import BaseFilter
from flask_login import current_user, logout_user
from flask import redirect
from sqlalchemy import func

from hospital.models import Assistant, Policy, Patient, Medicine, Time, Books, ClinicalRecords, Disease
from hospital import db, admin





class PolyModel(ModelView):
    excluded_form_columns = ('type',)

    def is_accessible(self):
        return current_user.is_authenticated


class AuthenticatedView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


class DoctorModelView(PolyModel):
    can_export = True


class AssistantModelView(PolyModel):
    can_export = True


class PolicyModelView(AuthenticatedView):
    can_export = True


class MedicineModelView(AuthenticatedView):
    can_export = True


class PatientModelView(AuthenticatedView):
    can_export = True


class TimeModelView(AuthenticatedView):
    can_export = True


class ClinicalRecordsModelView(AuthenticatedView):
    can_export = True


class ListBookView(AuthenticatedView):
    can_edit = False
    can_create = False
    can_delete = False

    # column_searchable_list = ('booked_date',)
    column_filters = ('booked_date',)


class BookModelView(AuthenticatedView):
    can_export = True


class DiseaseModelView(AuthenticatedView):
    can_export = True


class StatsView(BaseView):
    @expose("/")
    def index(self):
        return self.render("admin/stats.html")

    def is_accessible(self):
        return current_user.is_authenticated


class InformationView(BaseView):
    @expose("/")
    def index(self):
        return self.render("admin/information.html")

    def is_accessible(self):
        return current_user.is_authenticated


class ChangePassView(BaseView):
    @expose("/")
    def index(self):
        return self.render("admin/ChangePassword.html")

    def is_accessible(self):
        return current_user.is_authenticated


class LogoutView(BaseView):
    @expose("/")
    def index(self):
        logout_user()
        return redirect('/admin')

    def is_accessible(self):
        return current_user.is_authenticated


admin.add_view(TimeModelView(Time, db.session, name="Thoi gian"))
admin.add_view(MedicineModelView(Medicine, db.session, name="Danh sach thuoc", category='Danh sách'))
admin.add_view(PatientModelView(Patient, db.session, name="Danh sach benh nhan", category='Danh sách'))
admin.add_view(AssistantModelView(Assistant, db.session, name="Danh sach nhân viên", category='Danh sách'))
admin.add_view(ListBookView(Books, db.session, name="Danh sach dat lich", endpoint='ListBooks', category='Danh sách'))
admin.add_view(ClinicalRecordsModelView(ClinicalRecords, db.session, name="Nhập bệnh", endpoint="Record"))
admin.add_view(PolicyModelView(Policy, db.session, name="Quy dinh"))
admin.add_view(DiseaseModelView(Disease, db.session, name="Loại bệnh"))
admin.add_view(BookModelView(Books, db.session, name="Book"))
admin.add_view(StatsView(name="Bao cao thang"))
admin.add_view(InformationView(name="Info", endpoint='Information', category='Profile'))
admin.add_view(ChangePassView(name="Doi mat khau", endpoint='ChangePassword', category='Profile'))
admin.add_view(LogoutView(name="Dang xuat", endpoint='Logout', category='Profile'))




