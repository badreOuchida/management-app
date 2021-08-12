from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Conge, Employee, Paie, Prime, Utilisateur


class UtilisateurAdmin(UserAdmin):
	list_display = ('username',)
	search_fields = ('pk', 'email','username',)
	readonly_fields=('pk', 'date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(Utilisateur, UtilisateurAdmin)

admin.site.register(Employee)
admin.site.register(Paie)
admin.site.register(Conge)

admin.site.register(Prime)
