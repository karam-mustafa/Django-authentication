from django.db import models


# class AbstractDateModel(models.Model):
#     # A timestamp representing when this object was created.
#     date_created = models.DateTimeField(auto_now_add=True)

#     # A timestamp reprensenting when this object was last updated.
#     date_updated = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True
#         ordering = ["-date_created", "-date_updated"]


class AbstractAuditModel(models.Model):
    # A field to know who created the record.
    createdBy = models.CharField(max_length=200, default="System")

    # A timestamp representing when this object was created.
    createdDate = models.DateTimeField(auto_now_add=True)

    # A timestamp reprensenting when this object was last updated.
    updatedDate = models.DateTimeField(auto_now=True)

    # A field to know who updated the record.
    updatedBy =  models.CharField(max_length=200, null=True, blank=True)

    # A field to know who deleted the record.
    deletedBy =  models.CharField(max_length=200, null=True, blank=True)

    # A timestamp reprensenting when this object was deleted.
    deletedDate = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True
        # ordering = ["-date_created", "-date_updated"]
