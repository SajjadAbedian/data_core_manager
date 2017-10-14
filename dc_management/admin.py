from django.contrib import admin

from .models import Access_Log, AccessPermission, Audit_Log, Data_Log
from .models import DC_Administrator, DC_User, EnvtSubtype, External_Access_Log
from .models import Governance_Doc, Project, Server, Server_Change_Log, SN_Ticket
from .models import Software, Software_License_Type, Software_Log, Software_Purchase
from .models import Storage_Log, SubFunction

# customize the look of the admin site:
admin.site.site_header = 'Data Core Management Site'
admin.site.site_title = "DCMS"
admin.site.index_title = "Back end administration"

# customize the individual model views:
@admin.register(Governance_Doc)
class GovDocAdmin(admin.ModelAdmin):
    date_hierarchy = 'expiry_date'
    list_display = ('doc_id', 
                    'expiry_date',
                    'project', 
                    'defers_to_doc', 
                    'allowed_user_string',
                    )
    list_filter = ('governance_type',)


admin.site.register(Access_Log)
admin.site.register(AccessPermission)
admin.site.register(Audit_Log)
admin.site.register(Data_Log)
admin.site.register(DC_Administrator)
admin.site.register(DC_User)
admin.site.register(EnvtSubtype)
admin.site.register(External_Access_Log)
admin.site.register(Project)
admin.site.register(Server)
admin.site.register(SN_Ticket)
admin.site.register(Software)
admin.site.register(Software_License_Type)
admin.site.register(Software_Log)
admin.site.register(Software_Purchase)
admin.site.register(Storage_Log)
admin.site.register(SubFunction)