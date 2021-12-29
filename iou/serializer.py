from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Debt

class UserSerializer(serializers.ModelSerializer):
    owes = serializers.SerializerMethodField()
    owed_by = serializers.SerializerMethodField()
    balance = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id','username', 'password','owes','owed_by','balance',)
        extra_kwargs = {'password':{'write_only': True, 'required':True}}

    def get_owes(self, obj):
        if Debt.objects.filter(creditor_id=obj.id):
            # there is a problem with that solution... write now the query get first debtor...
            # it may accoure that the same user borrow to the same user additional money, then it will not be listed
            # becouse of the lack of the time i may show may way of thinking
            # In DebtViewSet if would overwrite create method to change balance if the same user borrow money to the same user
            # def create(self, request, *args, **kwargs):
            owes = {User.objects.filter(id=debt.debtor_id)[0].username: debt.debt for debt in Debt.objects.filter(creditor_id=obj.id)}
            return owes
        else: 
            return []

    def get_owed_by(self, obj):
        if Debt.objects.filter(creditor_id=obj.id):
            owes = {User.objects.filter(id=debt.creditor_id)[0].username: debt.debt for debt in Debt.objects.filter(debtor_id=obj.id)}
            return owes
        else: 
            return []

    def get_balance(self, obj):
        if Debt.objects.filter(creditor_id=obj.id):
            borrowed = 0
            debtsum = 0
            for debt in Debt.objects.filter(creditor_id=obj.id):
                borrowed += debt.debt
            for debt in Debt.objects.filter(debtor_id=obj.id):
                debtsum += debt.debt    
            return {borrowed - debtsum}
        else: 
            return []       

class DebtSerializer(serializers.ModelSerializer):
    # dynamic_data = serializers.SerializerMethodField()
    class Meta:
        model = Debt
        fields = ('id','creditor','debtor','debt',)        