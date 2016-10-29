"""
@copyright   Copyright (c) 2016  Devhres Team
@author      Angel Sullon (@asullom)
@package     utils

Descripcion: serializers
"""

from rest_framework import serializers


class RecursiveSerializer(serializers.Serializer):

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data
