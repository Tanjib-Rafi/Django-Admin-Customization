from django.contrib import admin
from django.contrib.auth.models import Group
import django.apps
from .models import random
from django.utils.html import format_html


class randomAdmin(admin.ModelAdmin):
    #exclude use for disappearing table content from admin dashboard
    #exclude = ('created_at',) 
    

    #display fields
    list_display = ('name','colored_name','address','less_content','imageShow','created_at','button',)

    #fields= ['name',('address','created_at')] #this will display same as list display


     # TEXT = 'some text for description'
    '''fieldset = (
        ('section 1',{
            'fields':('title', 'author',),
            'description': '%s' % TEXT,
            'classes' : ('collapse',),
        }),
     )'''

    #filte by created time
    list_filter = ('created_at',)

    #search by name
    search_fields = ('name',)

    #edit address field
    list_editable = ('address',)

    #now by clicking colorned name we can go to the edit page
    list_display_links = ('colored_name',)

    #readonly field,can't write or edit this field
    readonly_fields = ('name','imageShow')

    #radio button vertically, another option is horizantally
    radio_fields = {"gender": admin.VERTICAL}

    #set the save button on the top of the page
    save_on_top= True

    #default we have only one section which is delete,let's make another one for change address 
    actions = ('change_address',)

    #a function for actions event
    def change_address(self, request, queryset):
        count = queryset.update(address='ctg')
        self.message_user(request, '{} posts updated'.format(count))
    change_address.short_description='Change Address to ctg'

    #a function for showing less content(30) from address in the bar
    def less_content(self,obj):
        return obj.address[:30]

    #a function for creating a button to go to the next page
    def button(self,obj):
        return format_html(f'<a href="admin/customization/random/{obj.id}/change/">View</a>')

    #a function for showing image
    def imageShow(self,obj):
         return format_html(f'<img src="/images/{obj.image}" style="height :100px; width:100px;">')
   

    #changing color of name fields
    def colored_name(self, obj):
        return format_html(
            f'<span style="font-size: 30px; color:green;"> {obj.name}</span>'
        )


admin.site.site_title="Admin"
admin.site.site_header="Admin Dashboard"
admin.site.index_title =  "Welcome to the Dashboard"
#admin.site.register(random,randomAdmin)

models = django.apps.apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

admin.site.unregister(Group)

